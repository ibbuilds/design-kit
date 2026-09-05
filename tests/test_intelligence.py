import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'skills/design-director/scripts'))
import acquire
import intelligence as memory
import reference_policy as policy
import session
from PIL import Image


class IntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name) / 'references'
        self.patch = patch.object(session, 'storage_base', return_value=self.base)
        self.patch.start(); self.addCleanup(self.patch.stop)
        self.defaults = policy.resolve(Path(self.temp.name)/'absent.json')
        self.policy = patch.object(policy, 'resolve', return_value=self.defaults)
        self.policy.start(); self.addCleanup(self.policy.stop)
        self.root = session.init()['session']

    def image(self, slug='one', color='red', page=None):
        page = page or 'https://httpster.net/website/'+slug
        asset = 'https://httpster.net/assets/'+slug+'.png'
        session.approve(self.root, page); session.grant(self.root,page,asset,True)
        buf=io.BytesIO();Image.new('RGB',(640,400),color).save(buf,format='PNG')
        return session.put_bytes(self.root,buf.getvalue(),page,asset)['path']

    def analysis(self,path,role='composition',surface='hero'):
        checksum=memory.checked(path)[2]['sha256']
        return {'inspection':{'sha256':checksum,'method':'primary-image-view',
            'evidence':'synthetic test fixture; no live visual analysis claimed','region':'full fixture',
            'observed_at':'2026-09-05T00:00:00+00:00'},
            'observations':['Photography anchors opposing visual masses around negative space.'],
            'mechanisms':[{'role':role,'visible':'Asymmetric image and type share repeated edge anchors.',
                           'effect':'The repeated anchors stabilize an unconventional composition.'}],
            'families':['architecture'],'surfaces':[surface], 'confidence':'medium',
            'limitations':['Synthetic fixture tests storage and ranking, not design quality.']}

    def test_legacy_preservation_idempotence_and_cache_rebuild(self):
        p=self.image();receipt=Path(self.root)/session.MARKER
        before=receipt.read_bytes();image=Path(p).read_bytes()
        memory.sync();memory.sync();memory.cache_path().unlink();memory.sync()
        self.assertEqual(before,receipt.read_bytes());self.assertEqual(image,Path(p).read_bytes())
        self.assertEqual(memory.search()['results'][0]['analysis_status'],'uninspected')

    def test_mechanism_retrieval_not_url_and_surface_filter(self):
        p=self.image();memory.analyze(p,self.analysis(p))
        result=memory.search('unconventional photography',surface='hero')
        self.assertEqual(result['results'][0]['path'],p)
        self.assertIn('photography',result['results'][0]['task_match']['observed'])
        self.assertEqual(memory.search('photography',surface='table')['total'],0)

    def test_metadata_is_not_visual_analysis(self):
        p=self.image();page=memory.checked(p)[2]['page']
        memory.source_metadata(p,{'title':'Photography','tags':['table'],'evidence_url':page})
        hit=memory.search('photography')['results'][0]
        self.assertEqual(hit['analysis_status'],'uninspected');self.assertEqual(hit['task_match']['observed'],[])
        self.assertEqual(hit['task_match']['metadata_only'],['photography'])
        self.assertEqual(memory.search('photography',analyzed_only=True)['total'],0)

    def test_compact_candidates_hydrate_complete_analysis_and_receipt(self):
        p=self.image(); analysis=self.analysis(p)
        analysis['mechanisms'] *= 3
        memory.analyze(p,analysis)
        before=memory.checked(p)[2]
        hit=memory.search('photography')['results'][0]
        self.assertEqual(len(hit['mechanisms']),2)
        self.assertNotIn('observations',hit)
        full=memory.hydrate(p,sha256=hit['sha256'])
        self.assertEqual(full['analysis'],before['analysis'])
        self.assertEqual(memory.hydrate(p,receipt=True)['record'],before)
        self.assertEqual(memory.search('photography',full=True)['results'][0]['observations'],analysis['observations'])
        self.assertEqual(memory.checked(p)[2],before)
        self.assertEqual(memory.hydrate_selected([p],[hit['sha256']])['results'][0],full)
        with self.assertRaises(ValueError):memory.hydrate_selected([p],[])

    def test_hydration_rechecks_scope_exclusion_and_changed_bytes(self):
        p=self.image();memory.analyze(p,self.analysis(p))
        memory.search('photography')
        for kw in ({'scopes':[]},{'policy':{'sources':[],'specialist_sources':[]}}, {'sha256':'0'*64}):
            with self.assertRaises(ValueError):memory.hydrate(p,**kw)
        memory.exclude(p,'Synthetic exclusion: irrelevant for this design task.')
        with self.assertRaises(ValueError):memory.hydrate(p)
        Path(p).write_bytes(b'changed')
        with self.assertRaises(ValueError):memory.hydrate(p)
        self.assertEqual(memory.search('photography')['total'],0)

    def test_receipt_reuse_is_bounded_to_one_operation(self):
        for i,color in enumerate(['red','green','blue','yellow','purple']):
            p=self.image(str(i),color);memory.analyze(p,self.analysis(p))
        with patch.object(session,'load',wraps=session.load) as load:
            r=memory.search('photography')
        # One receipt load for sync and one for byte checks, independent of image count.
        self.assertLessEqual(load.call_count,2)
        self.assertEqual(len(r['results']),4)
        self.assertEqual(r['total'],5)
        with patch.object(memory,'sync',wraps=memory.sync) as sync:
            memory.complementary(['composition','typography'])
        self.assertEqual(sync.call_count,1)

    def test_static_section_transition_is_not_motion_evidence(self):
        p=self.image();a=self.analysis(p)
        a['observations']=['A color transition separates the static page sections.']
        memory.analyze(p,a)
        self.assertEqual(memory.search('section transition')['total'],1)
        self.assertEqual(memory.search('interaction motion')['total'],0)
        self.assertEqual(memory.search(role='motion')['total'],0)

    def test_inspected_animation_remains_retrievable(self):
        page='https://httpster.net/website/moving'
        asset='https://httpster.net/assets/moving.gif'
        session.approve(self.root,page);session.grant(self.root,page,asset,True)
        buf=io.BytesIO()
        Image.new('RGB',(640,400),'red').save(buf,format='GIF',save_all=True,
            append_images=[Image.new('RGB',(640,400),'blue')],duration=100,loop=0)
        p=session.put_bytes(self.root,buf.getvalue(),page,asset)['path']
        a=self.analysis(p,'motion');a['inspection']['method']='primary-motion-view'
        a['observations']=['The animation changes red to blue.']
        a['sequence'] = self.sequence(states=2)
        memory.analyze(p,a)
        self.assertEqual(memory.search('interaction motion')['results'][0]['path'],p)

    def sequence(self, states=3):
        return {'method':'representative-frames',
            'states':[{'position':i/(states-1),'visible':f'Synthetic observed state {i}.'} for i in range(states)],
            'trigger':'Unknown in fixture.', 'continuity':'Frame bounds stay anchored.',
            'spatial_relationship':'Colored surface remains in the same region.',
            'purpose':'Synthetic evidence validation, not design judgment.',
            'transferable_mechanism':'A fixed region changes state without moving its context.',
            'repetition':'Unknown.', 'timing_basis':'No measured interaction timing.'}

    def high_analysis(self, path, scope='section', role='composition'):
        a=self.analysis(path,role)
        a['mechanisms'][0].update(scope=[scope],
            evidence={'strength':'clear','basis':'Synthetic fixture only; no visual quality claim.'},
            quality={'ambition':'high','basis':'Synthetic qualification used to test role-scoped selection.'})
        return a

    def test_elite_eligibility_is_not_source_tier_or_legacy_confidence(self):
        p=self.image(page='https://recent.design/i/synthetic');a=self.analysis(p);a['confidence']='high'
        memory.analyze(p,a)
        self.assertEqual(memory.search('photography',ambition='high')['total'],0)
        self.assertEqual(memory.search('photography')['total'],1)
        memory.analyze(p,self.high_analysis(p))
        self.assertEqual(memory.search('photography',ambition='high')['total'],1)

    def test_section_authority_cannot_expand_to_page(self):
        p=self.image(page='https://www.a1.gallery/section/synthetic-features')
        for scope in ('page','full-site'):
            with self.assertRaises(ValueError):memory.analyze(p,self.high_analysis(p,scope))
        memory.analyze(p,self.high_analysis(p,'section'))
        self.assertEqual(memory.search('photography',ambition='high',evidence_scope='page')['total'],0)
        self.assertEqual(memory.search('photography',ambition='high',evidence_scope='section')['total'],1)

    def test_quality_and_scope_are_per_mechanism_not_per_reference(self):
        p=self.image();a=self.high_analysis(p,scope='typography',role='typography')
        a['mechanisms'].append({'role':'materiality','visible':'Synthetic textured plane.',
                                'effect':'Material cue.', 'scope':['detail']})
        memory.analyze(p,a)
        self.assertEqual(memory.search(role='materiality',ambition='high')['total'],0)
        self.assertEqual(memory.search(role='typography',ambition='high')['total'],1)

    def test_siblings_do_not_inherit_elite_eligibility(self):
        page='https://www.a1.gallery/website/synthetic'
        hero=self.image('hero',color='red',page=page);footer=self.image('footer',color='blue',page=page)
        memory.analyze(hero,self.high_analysis(hero,'hero'));memory.analyze(footer,self.analysis(footer,surface='footer'))
        self.assertEqual([h['path'] for h in memory.search(ambition='high')['results']],[hero])
        self.assertEqual(memory.search()['total'],2)

    def test_tier3_semantic_match_cannot_displace_qualified_tier1(self):
        top=self.image('top',page='https://recent.design/i/synthetic')
        support=self.image('support',color='blue')
        memory.analyze(top,self.high_analysis(top,'page'))
        a=self.high_analysis(support,'page');a['families']=['SaaS software'];a['observations'].append('SaaS software product dashboard pricing landing.')
        memory.analyze(support,a)
        self.assertEqual(memory.search('SaaS software photography',ambition='high')['results'][0]['path'],top)
        self.assertEqual(memory.search('SaaS software photography',ambition='high',scopes=['https://httpster.net/'])['results'][0]['path'],support)

    def test_qualified_tier2_specialist_outranks_general_gallery(self):
        general=self.image('general',page='https://recent.design/i/synthetic')
        special=self.image('special',color='blue',page='https://www.typewolf.com/site-of-the-day/synthetic')
        for p in (general,special):memory.analyze(p,self.high_analysis(p,'typography','typography'))
        self.assertEqual(memory.search('typography',ambition='high')['results'][0]['path'],special)

    def test_siteinspire_requires_selected_membership_even_for_ordinary_use(self):
        p=self.image(page='https://www.siteinspire.com/website/synthetic')
        memory.analyze(p,self.high_analysis(p,'page'))
        self.assertEqual(memory.search()['total'],0)
        with self.assertRaises(ValueError):memory.hydrate(p)
        memory.source_metadata(p,{'curated_subset':'Selected','evidence_url':memory.checked(p)[2]['page']})
        self.assertEqual(memory.search(ambition='high')['total'],1)

    def animated_image(self, extension='GIF'):
        page='https://recent.design/i/synthetic-animation';asset='https://recent.design/synthetic.'+extension.lower()
        session.approve(self.root,page);session.grant(self.root,page,asset,True)
        buf=io.BytesIO();Image.new('RGB',(640,400),'red').save(buf,format=extension,save_all=True,
            append_images=[Image.new('RGB',(640,400),'green'),Image.new('RGB',(640,400),'blue')],duration=[100,200,300],loop=0)
        return session.put_bytes(self.root,buf.getvalue(),page,asset)['path']

    def test_first_frame_gif_and_webp_cannot_supply_motion(self):
        for fmt in ('GIF','WEBP'):
            with self.subTest(format=fmt):
                p=self.animated_image(fmt);a=self.analysis(p,'motion');a['inspection']['method']='primary-motion-view'
                with self.assertRaises(ValueError):memory.analyze(p,a)
                a['sequence']=self.sequence();a['sequence']['states']=a['sequence']['states'][:1]
                with self.assertRaises(ValueError):memory.analyze(p,a)
                static=self.analysis(p);memory.analyze(p,static)
                scoped=self.analysis(p);scoped['mechanisms'][0]['scope']=['motion-sequence']
                with self.assertRaises(ValueError):memory.analyze(p,scoped)
                self.assertFalse(memory.hydrate(p)['motion_claims_supported'])
                self.assertNotIn(p,[r['path'] for r in memory.search('gif')['results']])
                a['sequence']=self.sequence();memory.analyze(p,a)
                self.assertTrue(memory.hydrate(p)['motion_claims_supported'])

    def test_sequence_samples_span_animation_and_never_claim_inspection(self):
        p=self.animated_image();out=Path(self.temp.name)/'sequence.png'
        result=memory.frames(p,out)
        self.assertEqual(result['inspection_status'],'not-yet-viewed')
        self.assertEqual([s['frame'] for s in result['samples']],[0,1,2])
        self.assertEqual(result['encoded_duration_ms'],600)
        self.assertEqual(memory.coverage()['status'],{'uninspected':1})
        with Image.open(out) as im:
            self.assertEqual(im.getpixel((20,60)),(255,0,0))
            self.assertEqual(im.getpixel((680,60)),(0,128,0))
            self.assertEqual(im.getpixel((1340,60)),(0,0,255))
        still=memory.view([p],Path(self.temp.name)/'first.png')
        self.assertEqual(still['images'][0]['evidence_kind'],'first-frame-only')

    def test_old_motion_attestation_is_preserved_but_not_sequence_evidence(self):
        p=self.animated_image();a=self.analysis(p,'motion');a['inspection']['method']='primary-motion-view'
        root,data,record,_=memory.checked(p);record['analysis']=a;session.save(root,data)
        before=(Path(root)/session.MARKER).read_bytes()
        self.assertEqual(memory.search('motion')['total'],0)
        self.assertFalse(memory.hydrate(p)['motion_claims_supported'])
        self.assertEqual(before,(Path(root)/session.MARKER).read_bytes())

    def test_video_bookmark_keeps_transferable_sequence_and_legacy_data(self):
        page='https://www.landing.love/sites/synthetic/'
        old=acquire.bookmark(page,'Synthetic video','Prior access observation.')
        result=acquire.bookmark(page,'Synthetic video',sequence=self.sequence())
        self.assertEqual(result['access_note'],old['access_note'])
        self.assertEqual(result['sequence']['continuity'],'Frame bounds stay anchored.')
        self.assertEqual(acquire.links('anchored')['total'],1)
        revised=acquire.bookmark(page,'Revised title','Updated access note.')
        self.assertEqual(revised['sequence'],result['sequence'])
        self.assertEqual(acquire.links('anchored',scopes=[])['total'],0)
        bad=self.sequence();bad['states'][1]['position']=0
        with self.assertRaises(ValueError):acquire.bookmark(page,'Bad sequence',sequence=bad)

    def test_elite_filters_preserve_empty_user_scopes(self):
        p=self.image();memory.analyze(p,self.high_analysis(p))
        before=memory.checked(p)[1]
        self.assertEqual(memory.search(ambition='high',scopes=[])['total'],0)
        self.assertTrue(memory.complementary(['composition'],ambition='high',scopes=[])['roles'][0]['gap'])
        self.assertEqual(memory.checked(p)[1],before)

    def test_hash_binding_motion_and_task_pollution_rejected(self):
        p=self.image();a=self.analysis(p)
        for mutate in (lambda a:a['inspection'].update(sha256='0'*64),
                       lambda a:a.update(task_application='Use for client'),
                       lambda a:a['mechanisms'][0].update(role='motion'),
                       lambda a:a['inspection'].update(method='primary-motion-view')):
            b=json.loads(json.dumps(a));mutate(b)
            with self.assertRaises(ValueError):memory.analyze(p,b)
        memory.analyze(p,a);Path(p).write_bytes(b'changed by user')
        self.assertEqual(memory.search('photography')['total'],0)

    def test_complementary_roles_choose_different_projects(self):
        a=self.image();b=self.image('two','blue')
        memory.analyze(a,self.analysis(a,'composition'))
        memory.analyze(b,self.analysis(b,'typography'))
        r=memory.complementary(['composition','typography','motion'])['roles']
        self.assertEqual([x['reference']['path'] for x in r[:2]],[a,b]);self.assertTrue(r[2]['gap'])

    def test_detail_role_retrieves_visible_evidence_under_broad_label(self):
        p=self.image();a=self.analysis(p,'materiality')
        a['mechanisms']=[{'role':'materiality','visible':'A tight contact shadow anchors the raised panel.',
                          'effect':'Grounds the object against its supporting surface.'}]
        memory.analyze(p,a)
        hit=memory.search('shadows',role='shadow',analyzed_only=True)['results'][0]
        self.assertEqual(hit['path'],p)
        self.assertEqual(hit['mechanisms'][0]['visible'],a['mechanisms'][0]['visible'])
        self.assertEqual(hit['mechanisms'][0]['evidence'],{'strength':'unassessed'})
        self.assertIn('shadows',hit['task_match']['observed'])

    def test_complementary_reuses_stronger_detail_instead_of_incidental_page_edge(self):
        button=self.image('button'); poster=self.image('poster','blue')
        a=self.analysis(button)
        a['mechanisms']=[
            {'role':'shadow','visible':'A soft contact shadow grounds the control.', 'effect':'The raised plane remains connected to its base.'},
            {'role':'edge','visible':'A fine highlight traces the upper rim.', 'effect':'The touch face separates from the darker extrusion.'}]
        memory.analyze(button,a)
        b=self.analysis(poster)
        b['mechanisms']=[{'role':'composition','visible':'Small labels sit at the edges of the page.', 'effect':'They frame the central headline.'}]
        memory.analyze(poster,b)
        rows=memory.complementary(['shadow','edge'])['roles']
        self.assertEqual([r['reference']['path'] for r in rows],[button,button])
        self.assertTrue(rows[1]['reused_reference'])
        self.assertEqual(rows[1]['same_mechanism_as'],[])
        self.assertEqual(rows[1]['reference']['mechanisms'][0]['visible'],a['mechanisms'][1]['visible'])

    def test_complementary_exposes_partial_role_and_identical_evidence(self):
        p=self.image();a=self.analysis(p)
        a['mechanisms']=[{'role':'materiality depth','visible':'A translucent product is raised above a dark plane.', 'effect':'Occlusion separates the object from its background.'}]
        memory.analyze(p,a)
        rows=memory.complementary(['materiality','depth','product presentation','motion'])['roles']
        self.assertEqual(rows[1]['same_mechanism_as'],['materiality'])
        self.assertEqual(rows[2]['role_terms'],{'matched':['product'],'unmatched':['presentation']})
        self.assertTrue(rows[2]['gap'])  # Partial evidence stays available without closing the gap.
        self.assertEqual(rows[2]['reference']['contribution_match']['status'],'partial')
        self.assertTrue(rows[3]['gap'])
        self.assertIsNone(rows[3]['reference'])

    def test_complementary_keeps_scope_and_input_bounds_on_reuse(self):
        p=self.image();memory.analyze(p,self.analysis(p))
        self.assertTrue(memory.complementary(['composition'],scopes=[])['roles'][0]['gap'])
        for roles in ([],[''],['the'],['edge','EDGE'],['x'*121],['a']*9):
            with self.subTest(roles=roles), self.assertRaises(ValueError):memory.complementary(roles)
        with self.assertRaises(ValueError):memory.complementary(['composition'],query='x'*801)

    def test_complementary_shared_context_precedes_source_diversity(self):
        p=self.image('workspace'); q=self.image('unrelated','blue')
        a=self.analysis(p,'composition');a['observations']=['A dense analyst workspace shows comparison rows.']
        b=self.analysis(q,'composition');b['observations']=['A quiet landscape occupies the main region.']
        memory.analyze(p,a);memory.analyze(q,b)
        selected=memory.complementary(['composition'],query='analyst workspace')['roles'][0]['reference']
        self.assertEqual(selected['path'],p)

    def test_detail_role_does_not_promote_provider_claims(self):
        p=self.image();memory.analyze(p,self.analysis(p))
        memory.source_metadata(p,{'title':'Premium shadow layering transparency',
                                 'evidence_url':memory.checked(p)[2]['page']})
        for role in ('shadow','layering','transparency'):
            self.assertEqual(memory.search(role,role=role,analyzed_only=True)['total'],0)

    def test_texture_is_not_automatically_depth_or_tactility(self):
        p=self.image();a=self.analysis(p,'materiality')
        a['observations']=['Fine grain occupies a flat color field.']
        a['mechanisms']=[{'role':'materiality','visible':'Textured letters sit on a uniform field.',
                          'effect':'Grain gives the lettering an irregular visual character.'}]
        memory.analyze(p,a)
        self.assertEqual(memory.search('textures',role='texture')['total'],1)
        self.assertEqual(memory.search('depth',role='depth')['total'],0)
        self.assertEqual(memory.search('tactile',role='tactile')['total'],0)

    def test_compact_detail_keeps_requested_mechanism_and_full_record(self):
        p=self.image();a=self.analysis(p)
        wanted={'role':'materiality','visible':'A translucent foreground overlaps the image.',
                'effect':'Background detail remains visible through the foreground.'}
        a['mechanisms']=a['mechanisms']*3+[wanted]
        memory.analyze(p,a)
        hit=memory.search('transparency',role='transparency')['results'][0]
        self.assertEqual(hit['mechanisms'][0]['visible'],wanted['visible'])
        self.assertEqual(len(memory.hydrate(p)['analysis']['mechanisms']),4)

    def test_detail_motion_labels_cannot_attest_a_still(self):
        p=self.image()
        for role in ('microinteraction','microinteractions','swipe','choreography'):
            with self.assertRaises(ValueError):memory.analyze(p,self.analysis(p,role))
        a=self.analysis(p);a['observations']=['A scroll label appears on this still.']
        memory.analyze(p,a)
        self.assertEqual(memory.search('scroll')['total'],0)
        self.assertEqual(memory.search('microinteraction')['total'],0)

    def test_targeted_detail_enrichment_refreshes_index_without_losing_analysis(self):
        p=self.image();a=self.analysis(p);memory.analyze(p,a)
        self.assertEqual(memory.search(role='highlight')['total'],0)
        previous=memory.hydrate(p)['analysis']
        detail={'role':'surface edge','visible':'A fine highlight traces the upper edge.',
                'effect':'Separates the raised face from its supporting surface.'}
        a['mechanisms'].append(detail);memory.analyze(p,a)
        result=memory.search('edge highlight',role='edge')
        self.assertEqual(result['results'][0]['mechanisms'][0]['visible'],detail['visible'])
        current=memory.hydrate(p)['analysis']
        self.assertEqual(current['observations'],previous['observations'])
        self.assertEqual(current['mechanisms'][:-1],previous['mechanisms'])

    def test_source_denial_alias_and_user_restrictions(self):
        self.assertIsNone(policy.source_for('https://godly.website/work'))
        self.assertEqual(policy.source_for('https://godly.website/work', retained=True)['id'],'recent')
        self.assertIsNone(policy.source_for('https://recent.design.evil.org/'))
        self.assertIsNone(policy.source_for('https://dribbble.com/shots/1'))
        self.assertIsNone(policy.source_for('https://img.a1.gallery/'))
        p=self.image();memory.analyze(p,self.analysis(p))
        self.assertEqual(memory.search('photography',scopes=[])['total'],0)
        self.assertEqual(memory.gap('table',scopes=[])['discovery_if_needed'],[])

    def test_product_does_not_expand_to_commerce_but_recall_survives(self):
        p=self.image();a=self.analysis(p)
        a['mechanisms']=[{'role':'commerce','visible':'Shop collections group merchandise by color.',
                          'effect':'Customers compare retail options.'}]
        a['observations']=['A shop collection.'];memory.analyze(p,a)
        self.assertEqual(memory.search('product',role='product presentation')['total'],0)
        self.assertEqual(memory.search('ecommerce')['results'][0]['path'],p)

    def test_role_queries_retrieve_clear_cross_domain_contribution_before_task_fit(self):
        software=self.image('software'); spatial=self.image('architecture','blue')
        a=self.analysis(software);a['families']=['software']
        a['observations']=['A software workspace displays account data.']
        a['mechanisms']=[{'role':'materiality','visible':'A small surface sits behind the software screenshot.',
                          'effect':'Its tint separates the product from the page.',
                          'evidence':{'strength':'limited','basis':'Preview obscures the surface edge and shadow.'}}]
        memory.analyze(software,a)
        b=self.analysis(spatial);b['observations']=['An architectural volume rests on a dark plinth.']
        b['mechanisms']=[{'role':'materiality','visible':'A tight contact band and broad soft shadow separate the volume and plinth.',
                          'effect':'Contact anchors the volume while ambient shading establishes elevation.',
                          'evidence':{'strength':'clear','basis':'Both bands are distinguishable in the retained view.'}}]
        memory.analyze(spatial,b)
        hits=memory.search('software',role='materiality')['results']
        self.assertEqual([h['path'] for h in hits],[spatial,software])
        self.assertEqual(hits[0]['task_match']['observed'],[])
        self.assertEqual(hits[1]['task_match']['observed'],['software'])
        self.assertEqual(hits[0]['contribution_match']['status'],'candidate')
        self.assertEqual(memory.complementary(['materiality'],query='software')['roles'][0]['reference']['path'],spatial)

    def test_contribution_and_limitations_are_not_inferred_from_domain_or_provider(self):
        p=self.image();a=self.analysis(p)
        a['families']=['software','materiality']
        a['mechanisms'][0]['evidence']={'strength':'clear','basis':'Only composition is legible; subtle shadows are unresolved.'}
        memory.analyze(p,a)
        memory.source_metadata(p,{'title':'Layered product framing', 'evidence_url':memory.checked(p)[2]['page']})
        self.assertEqual(memory.search('software')['results'][0]['task_match']['observed'],['software'])
        for role in ('shadow','layering','materiality'):
            self.assertEqual(memory.search('software',role=role)['total'],0)
        self.assertEqual(memory.search('shadows')['total'],0)

    def test_strength_is_per_mechanism_not_reference_confidence_or_image_size(self):
        p=self.image();a=self.analysis(p);a['confidence']='high'
        a['mechanisms']=[
            {'role':'composition','visible':'Type and a product panel occupy opposite halves.', 'effect':'The split preserves hierarchy.',
             'evidence':{'strength':'clear','basis':'Massing remains legible.'}},
            {'role':'surface edge','visible':'A light border surrounds the visible upper panel.', 'effect':'It separates the product face.',
             'evidence':{'strength':'limited','basis':'Overlay hides the lower edge; subtle shadow cannot be resolved.'}}]
        memory.analyze(p,a)
        rows=memory.complementary(['composition','surface edge'])['roles']
        self.assertFalse(rows[0]['gap']);self.assertTrue(rows[1]['gap'])
        self.assertEqual(rows[1]['reference']['mechanisms'][0]['evidence'],a['mechanisms'][1]['evidence'])
        self.assertEqual(rows[0]['reference']['evidence']['image_size'],[640,400])

    def test_evidence_schema_validation_and_hash_bound_round_trip(self):
        p=self.image();a=self.analysis(p);before=memory.checked(p)[2]
        for evidence in ({'strength':'clear'}, {'strength':'excellent','basis':'A score.'},
                         {'strength':'clear','basis':''}, {'strength':'clear','basis':'x','quality':10}):
            a['mechanisms'][0]['evidence']=evidence
            with self.assertRaises(ValueError):memory.analyze(p,a)
            self.assertEqual(memory.checked(p)[2],before)
        a['mechanisms'][0]['evidence']={'strength':'clear','basis':'Visible composition in this synthetic fixture.'}
        memory.analyze(p,a)
        record=memory.hydrate(p)['analysis']
        self.assertEqual(record['schema'],3)
        self.assertEqual(record['mechanisms'],a['mechanisms'])
        a['mechanisms'][0]['role']='motion'
        with self.assertRaises(ValueError):memory.analyze(p,a)

    def test_compound_contribution_cannot_be_assembled_from_unrelated_mechanisms(self):
        p=self.image();a=self.analysis(p)
        a['mechanisms']=[{'role':'product','visible':'A physical object fills the frame.', 'effect':'It establishes subject scale.'},
                         {'role':'presentation','visible':'A section heading introduces the talk.', 'effect':'It identifies the speaker.'}]
        memory.analyze(p,a)
        row=memory.complementary(['product presentation'])['roles'][0]
        self.assertTrue(row['gap']);self.assertEqual(len(row['role_terms']['unmatched']),1)
        self.assertIsNotNone(row['reference'])

    def test_role_priority_is_applied_before_complementary_candidate_limit(self):
        # More than one retrieval page of close task matches must not hide a clear
        # contribution that has no domain match.
        for i in range(25):
            p=self.image('software'+str(i), (i*8,0,0));a=self.analysis(p,'layering')
            a['observations']=['A software panel.']
            a['mechanisms'][0]['evidence']={'strength':'limited','basis':'Preview does not show the full overlap.'}
            memory.analyze(p,a)
        p=self.image('spatial','blue');a=self.analysis(p,'layering')
        a['mechanisms'][0]['evidence']={'strength':'clear','basis':'All planes are distinguishable in the fixture.'}
        memory.analyze(p,a)
        row=memory.complementary(['layering'],query='software')['roles'][0]
        self.assertEqual(row['reference']['path'],p)
        self.assertFalse(row['gap'])

    def test_bounds_and_pagination(self):
        self.image();self.image('two','blue')
        self.assertEqual(memory.search(limit=1)['total'],2)
        self.assertNotEqual(memory.search(limit=1)['results'],memory.search(limit=1,offset=1)['results'])
        for kwargs in ({'limit':0},{'limit':25},{'offset':-1}):
            with self.assertRaises(ValueError):memory.search(**kwargs)

    def test_atomic_receipt_failure_preserves_last_state(self):
        p=self.image();root,data=session.load(self.root);before=(root/session.MARKER).read_bytes()
        data['scopes'].append('https://recent.design/')
        with patch.object(session.os,'replace',side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):session.save(root,data)
        self.assertEqual(before,(root/session.MARKER).read_bytes())
        self.assertTrue(Path(p).exists())

    def test_observed_discovery_and_resume_exact_dedup(self):
        html='<article><img src="https://httpster.net/assets/new.png"><a href="/website/new">New</a><a href="https://evil.org">Visit</a></article>'
        found=acquire.discover('https://httpster.net/',html)
        self.assertEqual(len(found['candidates']),1)
        self.assertNotIn('https://evil.org',found['links'])
        with self.assertRaises(ValueError):acquire.discover('https://dribbble.com/',html)
        acquire.enqueue('https://httpster.net/',html,'Test-only rights attestation, synthetic bytes; no network access.',intent='seed')
        buf=io.BytesIO();Image.new('RGB',(640,400),'green').save(buf,format='PNG')
        with patch.object(acquire,'fetch',return_value=buf.getvalue()),patch.object(acquire.time,'sleep'):
            first=acquire.run();second=acquire.run()
        self.assertEqual(first['outcomes'][0]['status'],'retained');self.assertEqual(second['outcomes'],[])
        self.assertEqual(memory.coverage()['retained'],1)
        self.assertEqual(memory.coverage()['status'],{'uninspected':1})

    def test_view_sheet_does_not_attest_inspection(self):
        p=self.image();out=Path(self.temp.name)/'sheet.png'
        result=memory.view([p],out)
        self.assertTrue(out.exists());self.assertEqual(result['inspection_status'],'not-yet-viewed')
        self.assertEqual(memory.coverage()['status'],{'uninspected':1})

    def test_all_sources_remain_approved_with_distinct_modes(self):
        sources=self.defaults['sources']+self.defaults['specialist_sources']
        self.assertEqual(len(sources),23)
        self.assertEqual(len({s['id'] for s in sources}),23)
        self.assertEqual({s['acquisition']['mode'] for s in sources},{'bounded','targeted','research'})
        for s in sources:
            self.assertIsNotNone(policy.source_for(s['url'],specialist=True))
            self.assertTrue(s['acquisition']['evidence'])

    def test_new_source_identity_and_curated_entry_points(self):
        expected = {'hoverstates','codrops','loadmore','60fps','landing-love','design-spells','typewolf','fonts-in-use','brand-identity','bpando','brand-new','letterform','details'}
        sources = self.defaults['sources'] + self.defaults['specialist_sources']
        self.assertEqual({s['id'] for s in sources} - expected,
                         {'recent','awwwards','landingfolio','siteinspire','minimal-gallery','httpster','site-of-sites','a1-gallery','refs-gallery','rebrand-gallery'})
        self.assertTrue(expected <= {s['id'] for s in sources})
        for s in sources:
            self.assertEqual(policy.source_for(s['url'], specialist=True), s)
        self.assertEqual(policy.source_for('https://www.the-brandidentity.com/')['id'], 'brand-identity')
        self.assertEqual(policy.source_for('https://oa.letterformarchive.org/')['id'], 'letterform')
        self.assertIsNone(policy.source_for('https://tympanus.net/unapproved/'))
        self.assertIsNone(policy.source_for('https://www.underconsideration.com/other/'))
        self.assertIsNone(policy.source_for('https://mobbin.com/'))
        for q, label in [('font pairing','Staff Picks'), ('brand-system reasoning','Reviewed')]:
            result = policy.select(q)
            subset = next(s['preferred_subset'] for s in result if s['preferred_subset'])
            self.assertEqual(subset['label'], label)
            self.assertTrue(subset['broader_use'])
        source = dict(next(s for s in sources if s['id']=='fonts-in-use'))
        source['preferred_subset'] = dict(source['preferred_subset'], url='https://unapproved.org/')
        with self.assertRaises(ValueError): policy.validate({'version':1,'sources':[source]})

    def test_sixteen_decision_routes_are_bounded_and_specialized(self):
        cases = {
            'experimental art direction':'HOVERSTAT.ES', 'unusual navigation':'HOVERSTAT.ES',
            'mobile-first design':'loadmo.re', 'product motion':'60fps.design',
            'full-page web animation':'Landing Love', 'tactile button microinteraction':'Design Spells',
            'typography-led composition':'Typewolf', 'unusual font pairing':'Fonts In Use',
            'branding identity':'The Brand Identity', 'brand-system reasoning':'BP&O',
            'historical graphic composition':'Letterform Archive', 'hero design':'Details.so',
            'navigation detail':'Details.so', 'modal':'Details.so',
            'page transition':'Landing Love', 'scroll interaction':'Codrops'}
        for query, expected in cases.items():
            with self.subTest(query=query):
                results = policy.select(query)
                self.assertIn(expected, [s['source'] for s in results[:3]])
                self.assertLessEqual(len(results), 4)
                self.assertTrue(all(s['matched_specialties'] for s in results))
        self.assertEqual(policy.select('modal', scopes=[]), [])
        self.assertEqual(policy.select('modal', policy={'sources':[], 'specialist_sources':[]}), [])
        self.assertEqual(memory.gap('modal')['discovery_if_needed'][0]['source'], 'Details.so')

    def test_restrictions_do_not_remove_editorial_authority(self):
        for domain in ('fontsinuse.com','www.details.so','the-brandidentity.com'):
            s = policy.source_for('https://'+domain+'/')
            self.assertIsNotNone(s)
            with self.assertRaises(ValueError): acquire.discover(s['url'], '<article></article>')
            with self.assertRaises(ValueError): acquire.check_mode(s,'task','Specific visual decision')
        self.assertIn('Design Spells', [s['source'] for s in policy.select('delight')])
        self.assertIn('Letterform Archive', [s['source'] for s in policy.select('historical graphic composition')])

    def test_typography_facts_and_editorial_claims_are_not_visual_evidence(self):
        p=self.image();page=memory.checked(p)[2]['page']
        memory.source_metadata(p, {'typefaces':['Source-reported Typeface'], 'medium':'poster',
            'editorial_context':'Source author describes playful lettering.', 'evidence_url':page})
        record=memory.checked(p)[2]
        self.assertNotIn('analysis',record)
        self.assertEqual(record['source_metadata']['typefaces'], ['Source-reported Typeface'])
        self.assertEqual(memory.search('lettering',analyzed_only=True)['total'],0)

    def test_targeted_research_and_link_only_are_not_seed_permission(self):
        for domain in ('www.a1.gallery','minimal.gallery','www.rebrand.gallery','refs.gallery'):
            s=policy.source_for('https://'+domain+'/',specialist=True)
            with self.subTest(domain=domain),self.assertRaises(ValueError):acquire.check_mode(s,'seed','')
        a1=policy.source_for('https://www.a1.gallery/')
        acquire.check_mode(a1,'task','Relevant pricing comparison reference')
        with self.assertRaises(ValueError):acquire.check_mode(a1,'task','')
        uncertain=policy.source_for('https://www.siteofsites.co/')
        with self.assertRaises(ValueError):acquire.check_mode(uncertain,'task','Relevant portfolio reference')
        acquire.check_mode(uncertain,'task','Relevant portfolio reference','Synthetic test: individual retention permission verified for this asset.')

    def test_bookmarks_preserve_research_sources_without_fake_retention(self):
        r=acquire.bookmark('https://minimal.gallery/denmu/','Denmu','Research only; no image copied.')
        self.assertEqual(r['visual_status'],'not-retained')
        self.assertEqual(acquire.links('Denmu')['total'],1)
        self.assertEqual(acquire.links('copied')['total'],1)
        self.assertEqual(acquire.links('unrelated')['total'],0)
        self.assertEqual(acquire.links('Denmu',scopes=[])['total'],0)
        self.assertEqual(acquire.links('Denmu',scopes=['https://minimal.gallery/denmu/'])['total'],1)
        self.assertEqual(memory.coverage()['retained'],0)
        with self.assertRaises(ValueError):acquire.bookmark('https://mobbin.com/','Denied')

    def test_ads_and_targeted_unobserved_assets_rejected(self):
        ad='<article><img src="https://httpster.net/assets/ad.png"><a href="https://mobbin.com/">Sponsor</a></article>'
        self.assertEqual(acquire.discover('https://httpster.net/',ad)['candidates'],[])
        html='<article><a href="/website/example">Example</a><img src="https://img.a1.gallery/example.webp"></article>'
        with self.assertRaises(ValueError):acquire.enqueue('https://www.a1.gallery/',html,'Synthetic rights check for test only.',need='Useful pricing reference',assets=['https://evil.org/guessed.png'])
        with self.assertRaises(ValueError):acquire.enqueue('https://www.a1.gallery/',html,'Synthetic rights check for test only.',need='Useful pricing reference')

    def test_rate_restriction_stops_source_across_resumption(self):
        from urllib.error import HTTPError
        html=''.join(f'<article><a href="/website/{i}">Item</a><img src="https://httpster.net/assets/{i}.png"></article>' for i in range(2))
        acquire.enqueue('https://httpster.net/',html,'Synthetic rights check for testing only.',intent='seed')
        with patch.object(acquire,'fetch',side_effect=HTTPError('https://httpster.net/',429,'Rate limit',{},None)) as fetch:
            first=acquire.run();second=acquire.run(retry=True)
        self.assertEqual(fetch.call_count,1)
        self.assertEqual(first['outcomes'][0]['status'],'restricted')
        self.assertEqual(second['outcomes'][0]['status'],'waiting-access')

    def test_http_403_records_method_failure_and_legitimate_browser_fallback(self):
        from urllib.error import HTTPError
        html='<article><a href="/website/example">Example</a><img src="https://httpster.net/assets/example.png"></article>'
        acquire.enqueue('https://httpster.net/',html,'Synthetic rights check for testing only.',intent='seed')
        with patch.object(acquire,'fetch',side_effect=HTTPError('https://httpster.net/assets/example.png',403,'Forbidden',{},None)) as fetch:
            first=acquire.run();second=acquire.run(retry=True)
        self.assertEqual(fetch.call_count,1)
        self.assertEqual(first['outcomes'][0]['http_status'],403)
        self.assertIn('normal browser',first['outcomes'][0]['next_access'])
        self.assertEqual(second['outcomes'],[])
        self.assertIsNotNone(policy.source_for('https://httpster.net/'))


if __name__=='__main__':unittest.main()
