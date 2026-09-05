"""Synthetic lifecycle tests; never touch real retained reference data."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('session', ROOT / 'skills/design-director/scripts/session.py')
session = importlib.util.module_from_spec(spec)
spec.loader.exec_module(session)


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='design-kit-synthetic-tests-')
        self.base = Path(self.tmp.name) / 'retained'
        self.mock = patch.object(session, 'storage_base', return_value=self.base)
        self.mock.start()
        self.root = Path(session.init()['session'])
        self.original = Path(self.tmp.name) / 'original.png'
        self.original.write_bytes(b'\x89PNG\r\n\x1a\nsynthetic fixture')
        self.page = 'https://approved.example/gallery/item'
        self.asset = 'https://cdn.example/image.png'
        session.approve(self.root, 'https://approved.example/gallery')
        session.grant(self.root, self.page, self.asset, True)

    def tearDown(self):
        self.mock.stop()
        # TemporaryDirectory owns this synthetic fixture tree, never user references.
        self.tmp.cleanup()

    def put(self):
        return Path(session.put(self.root, self.original, self.page, self.asset)['path'])

    def clear(self):
        return session.cleanup(self.root, session.plan(self.root)['approval_digest'], True)

    def test_retention_and_reuse_across_reload(self):
        first = self.put()
        self.assertTrue(first.exists())
        self.assertEqual(session.list_sessions()[0]['session'], str(self.root))
        result = session.put(self.root, self.original, self.page, self.asset)
        self.assertTrue(result['duplicate'])
        self.assertEqual(result['path'], str(first))
        self.assertEqual(len(session.load(self.root)[1]['files']), 1)

    def test_cleanup_requires_explicit_request(self):
        owned = self.put()
        with self.assertRaisesRegex(ValueError, 'Explicit user'):
            session.cleanup(self.root, session.plan(self.root)['approval_digest'])
        self.assertTrue(owned.exists())

    def test_library_deduplicates_across_sessions(self):
        first = self.put()
        second = Path(session.init()['session'])
        session.approve(second, 'https://approved.example/gallery')
        session.grant(second, self.page, self.asset, True)
        result = session.put(second, self.original, self.page, self.asset)
        self.assertTrue(result['duplicate'])
        self.assertEqual(Path(result['path']), first)
        self.assertEqual(session.load(second)[1]['files'], {})

    def test_library_metadata_retrieval_preserves_image(self):
        image = self.put()
        original = image.read_bytes()
        session.annotate(self.root, image.name, 'Courtyard retreat',
                         ['hospitality', 'architecture'], 'Image-led horizon composition')
        result = session.search('retreat horizon', 'https://approved.example/gallery')
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['results'][0]['path'], str(image))
        self.assertEqual(image.read_bytes(), original)
        self.assertEqual(session.search('retreat', 'https://other.example/')['total'], 0)

    def test_legacy_index_and_pagination(self):
        self.put()
        self.assertEqual(session.search('gallery item')['total'], 1)
        self.assertEqual(session.search(offset=1)['results'], [])
        with self.assertRaises(ValueError):
            session.search(limit=0)
        with self.assertRaises(ValueError):
            session.annotate(self.root, '../original.png', 'unsafe')

    def test_cleanup_removes_only_owned_copy(self):
        owned = self.put()
        self.assertTrue(self.clear()['session_removed'])
        self.assertFalse(owned.exists())
        self.assertTrue(self.original.exists())

    def test_changed_and_foreign_files_preserved(self):
        owned = self.put()
        owned.write_bytes(b'user modification')
        foreign = self.root / 'my-notes.txt'
        foreign.write_text('keep')
        result = self.clear()
        self.assertEqual(len(result['preserved']), 2)
        self.assertTrue(owned.exists())
        self.assertTrue(foreign.exists())

    def test_stale_cleanup_plan_refused(self):
        self.put()
        old = session.plan(self.root)['approval_digest']
        (self.root / 'new-user-file').write_text('keep')
        with self.assertRaisesRegex(ValueError, 'plan changed'):
            session.cleanup(self.root, old, True)

    def test_traversal_receipt_refused(self):
        root, data = session.load(self.root)
        data['files']['../original.png'] = {'sha256': '0' * 64}
        session.save(root, data)
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            session.plan(root)
        self.assertTrue(self.original.exists())

    def test_other_root_refused(self):
        root, data = session.load(self.root)
        data['root'] = str(self.original.parent)
        session.save(root, data)
        with self.assertRaisesRegex(ValueError, 'receipt'):
            session.plan(root)

    def test_source_scope_and_exact_asset(self):
        for bad in ['https://approved.example.evil/gallery/item',
                    'https://approved.example/gallery-two/item',
                    'https://approved.example/private/item']:
            with self.assertRaises(ValueError):
                session.grant(self.root, bad, self.asset, True)
        with self.assertRaises(ValueError):
            session.put(self.root, self.original, self.page, self.asset + '?different')
        with self.assertRaises(ValueError):
            session.grant(self.root, self.page, self.asset, False)

    def test_unsafe_urls_refused(self):
        for bad in ['http://approved.example/', 'https://user:pass@approved.example/',
                    'https://approved.example/%2e%2e/private',
                    'https://approved.example/gallery/../private',
                    'https://approved.example:1234/', 'https://approved.example/\n']:
            with self.assertRaises(ValueError):
                session.url(bad)

    def test_nonimage_and_oversize_refused(self):
        self.original.write_bytes(b'<html>access denied</html>')
        with self.assertRaisesRegex(ValueError, 'raster'):
            self.put()
        with patch.object(session, 'MAX_BYTES', 2):
            with self.assertRaisesRegex(ValueError, 'storage bound'):
                self.put()

    def test_hardlink_preserved(self):
        owned = self.put()
        alias = Path(self.tmp.name) / 'alias.png'
        os.link(owned, alias)
        result = self.clear()
        self.assertEqual(len(result['preserved']), 1)
        self.assertTrue(owned.exists())
        self.assertTrue(alias.exists())

    def test_reparse_attribute_refused(self):
        class Fake:
            st_mode = 0o100600
            st_file_attributes = 0x400
            st_nlink = 1
        with patch.object(Path, 'lstat', return_value=Fake()):
            with self.assertRaisesRegex(ValueError, 'reparse'):
                session.ordinary(self.original)


if __name__ == '__main__':
    unittest.main()
