#!/usr/bin/env python3
"""Plan catalog-scoped searches and check source URLs. No network or model calls."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

CATALOG = Path(__file__).resolve().parents[1] / "REFERENCES.md"
# Existing access policy: these are not automatic-discovery fallbacks.
RESTRICTED = {"a1.gallery", "mozaika.design", "swaggin.dev", "mobbin.com", "appllama.com"}


def host(url):
    try:
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            raise ValueError("Expected an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("Credential-bearing URLs are not source references")
        if parsed.port not in (None, 80 if parsed.scheme == "http" else 443):
            raise ValueError("Unexpected port for a public source URL")
        name = parsed.hostname.rstrip(".").encode("idna").decode("ascii").lower()
        return name[4:] if name.startswith("www.") else name
    except (ValueError, UnicodeError) as error:
        raise ValueError(str(error)) from error


def read_catalog(path=CATALOG):
    section = None
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        if section:
            for label, url in re.findall(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", line):
                records.append({"section": section, "label": label, "url": url, "host": host(url)})
    return records


def select(records, sections=(), source_urls=()):
    known = {record["section"] for record in records}
    unknown = set(sections) - known
    if unknown:
        raise ValueError("Unknown catalog section: " + ", ".join(sorted(unknown)))
    chosen = [r for r in records if not sections or r["section"] in sections]
    eligible, excluded = [], []
    for record in chosen:
        is_restricted = any(record["host"] == h or record["host"].endswith("." + h) for h in RESTRICTED)
        # Appllama's catalog entry is a GitHub repository, not its service host.
        is_restricted = is_restricted or "/appllama/" in record["url"].lower()
        (excluded if is_restricted else eligible).append(dict(record, provenance="catalog"))
    for url in source_urls:
        eligible.append({"section": "Explicit user source", "label": "Explicit user source",
                         "url": url, "host": host(url), "provenance": "explicit-user-source"})
    return eligible, excluded


def check(url, eligible):
    candidate_host = host(url)
    candidate_path = unquote(urlsplit(url).path)
    if "\\" in candidate_path or ".." in candidate_path.split("/"):
        raise ValueError("Ambiguous or traversing source path")
    matches = []
    for record in eligible:
        if record["host"] != candidate_host:
            continue
        if candidate_host == "github.com":
            # A cited repository does not whitelist every repository on GitHub.
            root = "/" + "/".join(urlsplit(record["url"]).path.strip("/").split("/")[:2])
            if not (candidate_path.lower() == root.lower() or candidate_path.lower().startswith(root.lower() + "/")):
                continue
        matches.append(record)
    return {"url": url, "allowed": bool(matches), "host": candidate_host,
            "matched_sources": [{"url": r["url"], "section": r["section"],
                                 "provenance": r["provenance"]} for r in matches],
            "meaning": "Catalog source membership (repository-scoped on GitHub); not visual fit, outbound-link provenance, or browser enforcement."}


def search_queries(eligible, traits):
    """Generate options using the same shared-host scope as candidate checks."""
    queries, seen = [], set()
    for record in eligible:
        source_scope = record["host"]
        if source_scope == "github.com":
            source_scope += "/" + "/".join(urlsplit(record["url"]).path.strip("/").split("/")[:2])
        if source_scope not in seen:
            seen.add(source_scope)
            queries.append({"source_host": record["host"], "source_scope": source_scope,
                            "query": "site:" + source_scope + " " + traits.strip()})
    return queries


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("sources", "queries", "check"))
    parser.add_argument("urls", nargs="*", help="Candidate source URLs for check")
    parser.add_argument("--section", action="append", default=[], help="Exact catalog heading; repeat to combine")
    parser.add_argument("--query", help="Search traits; queries operation only")
    parser.add_argument("--source-url", action="append", default=[],
                        help="Human-chosen source; queries use only these URLs and chosen sections, never an agent fallback")
    args = parser.parse_args(argv)
    try:
        records = read_catalog()
        # Query planning is opt-in: explicit URLs alone must not silently add
        # the entire catalog. Listing/checking retain their global defaults.
        scoped_records = records if args.operation != "queries" or args.section else []
        eligible, excluded = select(scoped_records, args.section, args.source_url)
        if args.operation == "sources":
            if args.urls or args.query:
                raise ValueError("sources does not take candidates or a query")
            result = {"sections": sorted({r["section"] for r in records}),
                      "sources": eligible, "excluded_automatic_sources": excluded}
        elif args.operation == "queries":
            if args.urls or not args.query or not args.query.strip():
                raise ValueError("queries requires --query and no candidate URLs")
            if not args.section and not args.source_url:
                raise ValueError("Choose a section or explicit user source before generating queries")
            # Build optional queries, never execute them or scan every source.
            result = {"queries": search_queries(eligible, args.query),
                      "instruction": "Choose relevant sources; do not run the whole list."}
        else:
            if not args.urls or args.query:
                raise ValueError("check requires candidate URLs and no query")
            result = {"results": [check(url, eligible) for url in args.urls]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if args.operation == "check" and any(not item["allowed"] for item in result["results"]) else 0
    except ValueError as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
