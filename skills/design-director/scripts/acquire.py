"""Bounded, resumable acquisition of explicitly observed approved-gallery assets.

No recursive crawl, guessed asset URL, automatic source expansion, or model calls.
Run only after checking current source terms/robots and selecting useful candidates.
"""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import io
import json
import os
from pathlib import Path
import tempfile
import time
from urllib.parse import urljoin, urlsplit, parse_qs
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError

import intelligence
import reference_policy
import session


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Redirect requires explicit review of the new page/asset URL')


def fetch(url, maximum=session.MAX_BYTES):
    url = session.url(url)
    request = Request(url, headers={'User-Agent': 'DesignKit/0.4 (user-directed local design reference research)'})
    with build_opener(NoRedirect).open(request, timeout=25) as response:
        body = response.read(maximum + 1)
        if len(body) > maximum:
            raise ValueError('Response exceeds acquisition bound')
        return body


class GalleryHTML(HTMLParser):
    """Extract only visible HTML images, anchors and article grouping."""
    def __init__(self):
        super().__init__()
        self.articles, self.images, self.links = [], [], []
        self.article = None
        self.anchor = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'article':
            self.article = {'images': [], 'links': []}
        if tag == 'a':
            self.anchor = {'href': a.get('href', ''), 'title': a.get('aria-label', ''), 'text': ''}
            self.links.append(self.anchor)
            if self.article is not None: self.article['links'].append(self.anchor)
        if tag == 'img' and a.get('src'):
            item = {**a, 'anchor': self.anchor}
            self.images.append(item)
            if self.article is not None: self.article['images'].append(item)

    def handle_data(self, value):
        if self.anchor is not None: self.anchor['text'] += value

    def handle_endtag(self, tag):
        if tag == 'a': self.anchor = None
        if tag == 'article' and self.article is not None:
            self.articles.append(self.article)
            self.article = None


def discover(page, html, specialist=False):
    source = reference_policy.source_for(page, specialist=specialist)
    if not source:
        raise ValueError('Discovery page is outside approved sources')
    if reference_policy.acquisition_for(source)['retention'] == 'link-only':
        raise ValueError('Use permitted source-context research/bookmarks; automated asset extraction is disabled for this source')
    parser = GalleryHTML(); parser.feed(html)
    candidates = []
    def add(image, link=None):
        asset = urljoin(page, image['src'])
        host=urlsplit(page).hostname.removeprefix('www.')
        if host=='recent.design' and not ('/items/' in asset and '/poster/' in asset):
            return  # Avatars, sponsor logos and ads are not curated visual posts.
        if host in ('httpster.net','a1.gallery') and (not link or '/website/' not in link['href']):
            return
        # A1's public optimizer embeds the exact original source URL in its query.
        if urlsplit(page).hostname.removeprefix('www.') == 'a1.gallery' and urlsplit(asset).path == '/_next/image':
            original = parse_qs(urlsplit(asset).query).get('url', [''])[0]
            if original.startswith('https://'): asset = original
        try: asset = session.url(asset)
        except ValueError: return
        target = urljoin(page, link['href']) if link else page
        if not reference_policy.source_for(target, specialist=specialist): return
        title = (link.get('title') or link.get('text') or '') if link else ''
        candidates.append({'page': target, 'asset': asset, 'observed_on': page,
            'source_metadata': {'title': title.strip()[:200], 'description': (image.get('alt') or '')[:1200], 'evidence_url': page},
            'status': 'discovered'})
    for article in parser.articles:
        links = [l for l in article['links'] if l['href'] and reference_policy.source_for(urljoin(page,l['href']),specialist=specialist)]
        link = next((l for l in links if '/website/' in l['href']), links[0] if links else None)
        if not link:
            continue  # A sponsor/advertisement is not a curated reference entry.
        for im in article['images']:
            add(im,link)
    if not candidates:
        for im in parser.images:
            # Gallery-only fallbacks omit logos/avatars/sponsors, without inferring design facts.
            if '/items/' in im['src'] and '/poster/' in im['src']:
                add(im)
            elif im.get('anchor') and any(x in im['anchor']['href'] for x in ['/websites/', '/rebrand/']):
                add(im,im['anchor'])
    unique = {c['asset']: c for c in candidates}
    return {'source': source['name'], 'page': page, 'candidates': list(unique.values()),
            'links': list(dict.fromkeys(urljoin(page,l['href']) for l in parser.links if l['href'] and reference_policy.source_for(urljoin(page,l['href']),specialist=specialist)))}


def atomic(path, data):
    path = Path(path)
    if path.exists(): session.ordinary(path)
    fd, scratch = tempfile.mkstemp(prefix='.acquisition-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2); f.flush(); os.fsync(f.fileno())
        os.replace(scratch, path)
    finally:
        if os.path.exists(scratch): os.unlink(scratch)


def check_mode(source, intent, need, retention_permission=''):
    a=reference_policy.acquisition_for(source)
    if intent not in ('seed','task'):
        raise ValueError('Acquisition intent must be seed or task')
    if a['retention']=='link-only' or a['mode']=='link-only':
        raise ValueError('Source remains approved for research; retain a bookmark, not image bytes')
    if intent=='seed' and a['mode'] not in ('broad','bounded'):
        raise ValueError('This approved source requires targeted/research use, not corpus seeding')
    if intent=='task' and (not isinstance(need,str) or len(need.strip())<10):
        raise ValueError('Name the current reference need for targeted acquisition')
    if a['retention']=='per-item' and len(retention_permission.strip())<30:
        raise ValueError('Individual visual-retention permission is unverified; research in source context or bookmark')


def enqueue(page, html, rights, specialist=False, intent='task', need='', assets=None, retention_permission=''):
    """rights records a real human/primary check, not a license supplied by this tool."""
    if not isinstance(rights, str) or not 20 <= len(rights) <= 2000:
        raise ValueError('Record current terms/robots evidence and permitted local use')
    found = discover(page, html, specialist)
    source=reference_policy.source_for(page,specialist=specialist)
    check_mode(source,intent,need,retention_permission)
    if reference_policy.acquisition_for(source)['mode'] in ('targeted','research') and not assets:
        raise ValueError('Select exact observed asset URLs for this targeted/research source')
    if assets is not None:
        observed={c['asset'] for c in found['candidates']}
        if not set(assets) <= observed:
            raise ValueError('Selected assets must occur in the observed source page')
        found['candidates']=[c for c in found['candidates'] if c['asset'] in assets]
    base = session.storage_base(); base.mkdir(parents=True, exist_ok=True)
    session.ordinary(base, directory=True)
    path = base / 'acquisition.json'
    if path.exists(): session.ordinary(path)
    queue = json.loads(path.read_text()) if path.exists() else {'schema': 1, 'items': []}
    keys = {(c['page'], c['asset']) for c in queue['items']}
    for c in found['candidates']:
        c.update(intent=intent,need=need,retention_permission=retention_permission)
        if (c['page'], c['asset']) not in keys:
            queue['items'].append({**c, 'rights': rights, 'specialist': specialist, 'discovered_at': intelligence.now(), 'attempts': 0})
        else:
            old=next(x for x in queue['items'] if (x['page'],x['asset'])==(c['page'],c['asset']))
            if old['status'] not in ('retained','restricted'):
                old.update(c,rights=rights)
    atomic(path, queue)
    return {'queue': str(path), 'pending': sum(c['status']=='discovered' for c in queue['items']), 'observed': len(found['candidates'])}


def bookmark(page, title, note='', specialist=False, sequence=None):
    source=reference_policy.source_for(page,specialist=specialist)
    if not source: raise ValueError('Bookmark must be inside an approved source')
    if not isinstance(title,str) or not 1 <= len(title) <= 200 or len(note)>1000:
        raise ValueError('Use a compact source title and access note')
    base=session.storage_base();base.mkdir(parents=True,exist_ok=True);session.ordinary(base,directory=True)
    path=base/'bookmarks.json'
    if path.exists():session.ordinary(path)
    rows=json.loads(path.read_text()) if path.exists() else []
    item={'page':session.url(page),'source':source.get('id',source['name']),'title':title,'access_note':note,
          'retention':'link-only','visual_status':'not-retained','recorded_at':intelligence.now()}
    if sequence is not None:
        item['sequence'] = intelligence.validate_sequence(sequence)
        item['sequence_observed_at'] = intelligence.now()
    old = next((r for r in rows if r['page'] == item['page']), {})
    if not note and old.get('access_note'):
        item['access_note'] = old['access_note']
    # Updating access/title must not erase an earlier inspected sequence.
    item = {**old, **item}
    rows=[r for r in rows if r['page']!=item['page']]+[item];atomic(path,rows)
    return item


def links(query='',limit=6,specialist=False,scopes=None):
    if not 1<=limit<=24:raise ValueError('Use a bounded bookmark result set')
    if scopes is not None:
        scopes = [session.url(s) for s in scopes]
    path=session.storage_base()/'bookmarks.json'
    if not path.exists():return {'results':[]}
    session.ordinary(path);rows=json.loads(path.read_text())
    terms=intelligence.tokens(query)
    policy = reference_policy.resolve()
    hits=[r for r in rows if reference_policy.source_for(r['page'],policy,specialist=specialist)
          and (scopes is None or any(session.in_scope(r['page'],s) for s in scopes))
          and (not terms or terms & intelligence.tokens(r['title']+' '+r['page']+' '+r.get('access_note','')+' '+json.dumps(r.get('sequence',{}))))]
    return {'total':len(hits),'results':hits[:limit],'next':'Open the source and inspect actual visuals. A bookmark is not retained visual evidence.'}


def run(limit=24, retry=False, delay=1.0):
    from PIL import Image, ImageOps
    if not 1 <= limit <= 100 or delay < 0.5:
        raise ValueError('Bound each run to 1–100 assets and >=0.5 seconds between requests')
    path = session.storage_base() / 'acquisition.json'
    session.ordinary(path)
    queue = json.loads(path.read_text())
    # Reuse an existing ingestion session when resuming, preserving every old receipt.
    root = queue.get('session')
    if root is None:
        root = session.init()['session']; queue['session'] = root; atomic(path, queue)
    session.load(root)
    outcomes = []
    restricted_hosts={urlsplit(c['page']).hostname for c in queue['items'] if c['status']=='restricted' and c.get('http_status',429)==429}
    for c in queue['items']:
        if len(outcomes) >= limit: break
        if c['status'] != 'discovered' and not (retry and c['status'] == 'failed'): continue
        if urlsplit(c['page']).hostname in restricted_hosts:
            outcomes.append({'asset':c['asset'],'status':'waiting-access','error':'This source previously restricted access; no automatic retry.'})
            continue
        try:
            source = reference_policy.source_for(c['page'], specialist=c['specialist'])
            observed_source = reference_policy.source_for(c['observed_on'], specialist=c['specialist'])
            if not source or source != observed_source:
                raise ValueError('Candidate no longer permitted by source policy')
            try:
                check_mode(source,c.get('intent','seed'),c.get('need',''),c.get('retention_permission',''))
            except ValueError as exc:
                c.update(status='blocked-policy',error=str(exc));atomic(path,queue)
                outcomes.append({'asset':c['asset'],'status':c['status'],'error':str(exc)})
                continue
            c['attempts'] += 1
            # Resume a successful import even if the previous run died before queue save.
            existing = next((p for p,r in intelligence.records() if r['page']==c['page'] and r['asset']==c['asset']), None)
            if existing:
                intelligence.checked(existing)
                c.update(status='retained', path=existing)
            else:
                time.sleep(max(delay, source.get('request_interval_seconds', 0.5)))
                content = fetch(c['asset'])
                c['download_sha256']=session.digest(content)
                with Image.open(io.BytesIO(content)) as im:
                    im.load()
                    if min(im.size) < 180 or max(im.size) < 500:
                        raise ValueError('Preview too small to provide useful design evidence')
                    gray = ImageOps.grayscale(ImageOps.fit(im, (9, 8)))
                    px = [gray.getpixel((x,y)) for y in range(8) for x in range(9)]
                    dhash = sum((px[y*9+x] > px[y*9+x+1]) << (y*8+x) for y in range(8) for x in range(8))
                    c['visual_fingerprint'] = f'{dhash:016x}'
                    c['dimensions'] = list(im.size)
                    try: session.image_extension(content)
                    except ValueError:
                        if getattr(im, 'n_frames', 1) > 1:
                            raise ValueError('Unsupported animation must not be silently flattened; use source playback')
                        converted = io.BytesIO(); im.convert('RGB').save(converted, format='PNG'); content = converted.getvalue()
                session.approve(root, source['url'])
                # The exact observed page is approved to accommodate explicit aliases.
                session.approve(root, c['page'])
                session.grant(root,c['page'],c['asset'],True)
                result = session.put_bytes(root,content,c['page'],c['asset'])
                c.update(status='retained', path=result['path'], duplicate=result['duplicate'])
                rroot,data,record,_=intelligence.checked(c['path'])
                record.setdefault('acquisition_provenance', [])
                provenance = {k:c[k] for k in ('page','asset','observed_on','rights','discovered_at','download_sha256')}
                if provenance not in record['acquisition_provenance']: record['acquisition_provenance'].append(provenance)
                record['visual_fingerprint'] = c['visual_fingerprint']
                session.save(rroot,data)
                if not result['duplicate']:
                    intelligence.source_metadata(c['path'],{**c['source_metadata'], 'evidence_url': c['observed_on']})
        except (ValueError, OSError) as exc:
            c.update(status='failed', error=str(exc))
            if isinstance(exc, HTTPError) and exc.code in (401,403,429):
                c.update(status='restricted', http_status=exc.code, access_method='HTTP asset fetch')
                if exc.code==403:
                    c['next_access']='Try normal browser navigation to the official page, then relevant official canonical/versioned or available authorized API/MCP access. This method failed; source approval remains. Never bypass controls.'
                atomic(path,queue)
                outcomes.append({k:c[k] for k in ('asset','status','error','http_status','next_access') if k in c})
                break
        atomic(path,queue)
        outcomes.append({k:c[k] for k in ('asset','status','path','error') if k in c})
    return {'outcomes':outcomes, 'pending':sum(c['status']=='discovered' for c in queue['items']), 'inspection': 'Retained images remain uninspected until actually viewed and analyzed by the primary session.'}


def duplicates(distance=5):
    if not 0 <= distance <= 12: raise ValueError('Use a conservative Hamming distance 0–12')
    rows=[(p,r) for p,r in intelligence.records() if r.get('visual_fingerprint')]
    candidates=[]
    for i,(p,r) in enumerate(rows):
        for q,s in rows[:i]:
            d=(int(r['visual_fingerprint'],16)^int(s['visual_fingerprint'],16)).bit_count()
            if d <= distance: candidates.append({'a':p,'b':q,'distance':d})
    return {'possible_duplicates':candidates[:100], 'total':len(candidates), 'action':'Review pixels; no automatic deletion or merging. Fingerprints can collide.'}


def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='command',required=True)
    for cmd in ('discover','enqueue'):
        q=sub.add_parser(cmd);q.add_argument('--page',required=True);q.add_argument('--html',required=True);q.add_argument('--specialist',action='store_true')
        if cmd=='enqueue':
            q.add_argument('--rights',required=True);q.add_argument('--intent',choices=('seed','task'),default='task')
            q.add_argument('--need',default='');q.add_argument('--asset',action='append',dest='assets')
            q.add_argument('--retention-permission',default='')
    q=sub.add_parser('bookmark');q.add_argument('--page',required=True);q.add_argument('--title',required=True);q.add_argument('--note',default='');q.add_argument('--specialist',action='store_true')
    q.add_argument('--sequence', help='JSON file containing actual primary sequence observations')
    q=sub.add_parser('links');q.add_argument('--query',default='');q.add_argument('--limit',type=int,default=6);q.add_argument('--specialist',action='store_true')
    q.add_argument('--scope',action='append',dest='scopes')
    q=sub.add_parser('run');q.add_argument('--limit',type=int,default=24);q.add_argument('--retry',action='store_true');q.add_argument('--delay',type=float,default=1.0)
    q=sub.add_parser('duplicates');q.add_argument('--distance',type=int,default=5)
    a=vars(p.parse_args());cmd=a.pop('command')
    try:
        if 'html' in a:a['html']=Path(a['html']).read_text(encoding='utf-8')
        if a.get('sequence'):a['sequence']=json.loads(Path(a['sequence']).read_text(encoding='utf-8'))
        print(json.dumps(globals()[cmd](**a),indent=2))
    except (ValueError,OSError,KeyError,TypeError) as exc:p.exit(2,f'{type(exc).__name__}: {exc}\n')


if __name__=='__main__':main()
