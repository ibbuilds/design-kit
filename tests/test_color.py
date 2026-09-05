import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'skills/design-director/scripts'
sys.path.insert(0, str(SCRIPTS))
import color


class ColorTests(unittest.TestCase):
    def test_known_oklab_reference_vectors(self):
        # Independent published primary-color vectors (D65 Oklab), not a round trip.
        for hex_value, expected in [('#FF0000', (0.62795536, 0.25768331, 29.233885)),
                                    ('#00FF00', (0.86643961, 0.29482724, 142.495339)),
                                    ('#0000FF', (0.45201372, 0.31321437, 264.052021))]:
            actual = color.to_oklch(color.parse_hex(hex_value))
            for a, e in zip(actual, expected):
                self.assertAlmostEqual(a, e, places=5)

    def test_round_trip_and_neutrals(self):
        for value in ['#000000', '#FFFFFF', '#808080', '#3856A6', '#D36E38', '#FF00FF']:
            mapped = color.swatch(color.gamut_map(*color.to_oklch(color.parse_hex(value))))
            self.assertEqual(mapped['hex'], value)
        self.assertEqual(color.to_oklch(color.parse_hex('#808080'))[1:], (0.0, 0.0))

    def test_out_of_gamut_reduces_chroma_without_changing_lightness_hue(self):
        rgb = color.gamut_map(0.6, 0.6, 40)
        self.assertTrue(all(0 <= c <= 1 for c in rgb))
        l, c, h = color.to_oklch(rgb)
        self.assertAlmostEqual(l, 0.6, places=6)
        self.assertAlmostEqual(h, 40, places=4)
        self.assertLess(c, 0.6)
        self.assertGreater(c, 0.1)
        self.assertEqual(color.swatch(color.gamut_map(0, 0.6, 40))['hex'], '#000000')
        self.assertEqual(color.swatch(color.gamut_map(1, 0.6, 40))['hex'], '#FFFFFF')

    def test_twenty_stop_ramps_preserve_anchor_and_order(self):
        for anchor in ['#3856A6', '#C8553D', '#808080', '#00FF00']:
            result = color.ramp(anchor)
            self.assertEqual(result['actual_stops'], 20)
            self.assertEqual(len({s['hex'] for s in result['stops']}), 20)
            self.assertIn(anchor, [s['hex'] for s in result['stops']])
            lights = [s['oklch'][0] for s in result['stops']]
            self.assertTrue(all(a < b for a, b in zip(lights, lights[1:])))
            self.assertEqual(result, color.ramp(anchor))

    def test_neutral_ramp_and_token_serialization(self):
        for swatch in color.ramp('#808080', name='neutral')['stops']:
            self.assertTrue(swatch['name'].startswith('color/neutral/'))
            self.assertEqual(tuple(swatch['rgb'].values()), color.parse_hex(swatch['hex']))
            self.assertEqual(swatch['oklch'][1], 0)

    def test_custom_counts_chroma_and_endpoints(self):
        self.assertEqual(color.ramp('#3856A6', stops=7)['actual_stops'], 7)
        for anchor in ['#000000', '#FFFFFF']:
            self.assertIn(anchor, [s['hex'] for s in color.ramp(anchor, dark=0, light=1)['stops']])
        result = color.ramp('#3856A6', chroma=0.06)
        self.assertIn('#3856A6', [s['hex'] for s in result['stops']])
        self.assertNotEqual(result, color.ramp('#3856A6'))

    def test_redundant_quantized_stops_are_not_fabricated(self):
        al = color.to_oklch(color.parse_hex('#808080'))[0]
        result = color.ramp('#808080', dark=al-0.0001, light=al+0.0001)
        self.assertLess(result['actual_stops'], 20)
        self.assertTrue(result['notes'])

    def test_wcag_known_ratios_and_boundary_not_rounded_up(self):
        self.assertEqual(color.contrast('#000000', '#FFFFFF'), 21)
        self.assertEqual(color.contrast('#AABBCC', '#AABBCC'), 1)
        self.assertAlmostEqual(color.contrast('#777777', '#FFFFFF'), 4.47808945, places=7)
        self.assertLess(color.contrast('#777777', '#FFFFFF'), 4.5)
        self.assertGreater(color.contrast('#767676', '#FFFFFF'), 4.5)
        self.assertEqual(color.contrast('#3856A6', '#FFFFFF'), color.contrast('#FFFFFF', '#3856A6'))

    def test_invalid_input_and_alpha_are_rejected(self):
        for value in ['#FFF', '#FFFFFF00', 'red', '#GGGGGG', '#FFFFFF\n']:
            with self.assertRaises(ValueError): color.parse_hex(value)
        for kw in [dict(stops=2), dict(stops=True), dict(stops=257), dict(dark=0.9, light=0.1),
                   dict(dark=float('nan')), dict(chroma=float('inf')), dict(name='../brand')]:
            with self.assertRaises(ValueError): color.ramp('#3856A6', **kw)
        with self.assertRaises(ValueError): color.ramp('#FFFFFF')
        for lch in [(float('nan'), 0.1, 20), (0.5, -0.1, 20), (0.5, 0.1, float('inf'))]:
            with self.assertRaises(ValueError): color.gamut_map(*lch)

    def test_cli_json_and_invalid_input(self):
        def run(*args):
            return subprocess.run([sys.executable, '-B', str(SCRIPTS/'color.py'), *args],
                                  capture_output=True, text=True)
        valid = run('ramp', '--anchor', '#3856A6')
        self.assertEqual(valid.returncode, 0)
        self.assertEqual(json.loads(valid.stdout)['actual_stops'], 20)
        self.assertFalse(json.loads(run('contrast', '#777777', '#FFFFFF').stdout)['passes'])
        self.assertEqual(json.loads(run('convert', '--oklch', '0', '0', '0').stdout)['hex'], '#000000')
        bad = run('ramp', '--anchor', '#FFFFFF00')
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, '')
        self.assertNotIn('Traceback', bad.stderr)


if __name__ == '__main__':
    unittest.main()
