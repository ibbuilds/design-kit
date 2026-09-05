"""Optional opaque-sRGB/OKLCH calculator; the primary model authors the palette.

D65 Oklab matrices: https://bottosson.github.io/posts/oklab/
Color spaces: https://www.w3.org/TR/css-color-4/
Contrast: https://www.w3.org/TR/WCAG22/#dfn-relative-luminance
Verified 2026-09-05. Fixed-L/h chroma reduction is a simple local gamut map,
not the CSS gamut-mapping algorithm. No dependencies, I/O or creative selection.
"""
import argparse
import json
import math
import re


def finite(value, low, high, label):
    if isinstance(value, bool) or not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f'{label} must be finite in {low}..{high}')
    return value


def parse_hex(value):
    if not isinstance(value, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise ValueError('Use opaque six-digit #RRGGBB; composite alpha separately')
    return tuple(int(value[i:i + 2], 16) / 255 for i in (1, 3, 5))


def linear(channel):
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def encoded(channel):
    return 12.92 * channel if channel <= 0.0031308 else 1.055 * channel ** (1 / 2.4) - 0.055


def to_oklch(rgb):
    r, g, b = (linear(finite(c, 0, 1, 'sRGB channel')) for c in rgb)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    light = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    b = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    chroma = math.hypot(a, b)
    # Neutral numerical residue is not a meaningful hue.
    return (light, chroma, math.degrees(math.atan2(b, a)) % 360) if chroma > 1e-7 else (light, 0.0, 0.0)


def _linear_rgb(light, chroma, hue):
    a, b = chroma * math.cos(math.radians(hue)), chroma * math.sin(math.radians(hue))
    l = (light + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (light - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (light - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def gamut_map(light, chroma, hue):
    finite(light, 0, 1, 'OKLCH lightness')
    finite(chroma, 0, 1, 'OKLCH chroma')
    if not math.isfinite(hue):
        raise ValueError('OKLCH hue must be finite')
    hue %= 360
    def inside(rgb):
        return all(-1e-7 <= c <= 1 + 1e-7 for c in rgb)
    raw = _linear_rgb(light, chroma, hue)
    if not inside(raw):
        low, high = 0.0, chroma
        for _ in range(32):
            mid = (low + high) / 2
            if inside(_linear_rgb(light, mid, hue)):
                low = mid
            else:
                high = mid
        raw = _linear_rgb(light, low, hue)
    return tuple(encoded(max(0.0, min(1.0, c))) for c in raw)


def swatch(rgb):
    # Emit one canonical 8-bit color: Figma RGB, OKLCH and contrast agree with HEX.
    channels = [round(finite(c, 0, 1, 'sRGB channel') * 255) for c in rgb]
    value = '#' + ''.join(f'{c:02X}' for c in channels)
    actual = tuple(c / 255 for c in channels)
    return {'hex': value, 'rgb': dict(zip(('r', 'g', 'b'), actual)),
            'oklch': list(to_oklch(actual))}


def contrast(foreground, background):
    def luminance(value):
        return sum(w * linear(c) for w, c in zip((0.2126, 0.7152, 0.0722), parse_hex(value)))
    a, b = sorted((luminance(foreground), luminance(background)))
    return (b + 0.05) / (a + 0.05)


def ramp(anchor, name='brand', stops=20, dark=0.08, light=0.98, chroma=None):
    if type(stops) is not int or not 3 <= stops <= 256:
        raise ValueError('Request 3..256 stops')
    if not re.fullmatch(r'[a-z][a-z0-9-]*', name):
        raise ValueError('Name must be a lowercase token segment')
    finite(dark, 0, 1, 'dark endpoint'); finite(light, 0, 1, 'light endpoint')
    if dark >= light:
        raise ValueError('Endpoints must ascend from dark to light')
    anchor_rgb = parse_hex(anchor)
    al, ac, ah = to_oklch(anchor_rgb)
    if not dark - 1e-7 <= al <= light + 1e-7:
        raise ValueError('Anchor lightness must lie within endpoints; adjust --dark/--light')
    al = max(dark, min(light, al))
    peak = ac if chroma is None else finite(chroma, 0, 1, 'chroma')
    levels = [dark + (light - dark) * i / (stops - 1) for i in range(stops)]
    # Keep the authored anchor, without adding an unrequested stop or moving endpoints.
    if dark < al < light:
        nearest = min(range(1, stops - 1), key=lambda i: abs(levels[i] - al))
        levels[nearest] = al
    result, seen = [], set()
    for level in levels:
        is_anchor = abs(level - al) < 1e-12
        # Chroma tapers towards black/white, preserving the authored hue.
        taper = level / al if level < al else (1 - level) / (1 - al) if al < 1 else 1
        item = swatch(anchor_rgb if is_anchor else gamut_map(level, peak * max(0, taper), ah))
        if item['hex'] in seen or (result and item['oklch'][0] <= result[-1]['oklch'][0]):
            continue
        seen.add(item['hex'])
        item['name'] = f'color/{name}/{len(result) + 1:02d}'
        result.append(item)
    return {'anchor': swatch(anchor_rgb), 'requested_stops': stops, 'actual_stops': len(result),
            'direction': 'dark-to-light', 'stops': result,
            'notes': ['Redundant/nonascending 8-bit stops removed; inspect perceptual spacing.']
            if len(result) < stops else []}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('ramp')
    p.add_argument('--anchor', required=True); p.add_argument('--name', default='brand')
    p.add_argument('--stops', type=int, default=20)
    p.add_argument('--dark', type=float, default=0.08); p.add_argument('--light', type=float, default=0.98)
    p.add_argument('--chroma', type=float)
    p = commands.add_parser('contrast')
    p.add_argument('foreground'); p.add_argument('background')
    p.add_argument('--minimum', type=float, default=4.5)
    p = commands.add_parser('convert')
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument('--hex'); source.add_argument('--oklch', nargs=3, type=float)
    args = vars(parser.parse_args()); command = args.pop('command')
    try:
        if command == 'ramp':
            result = ramp(**args)
        elif command == 'contrast':
            minimum = finite(args['minimum'], 1, 21, 'minimum contrast')
            ratio = contrast(args['foreground'], args['background'])
            result = {'ratio': ratio, 'minimum': minimum, 'passes': ratio >= minimum,
                      'scope': 'Opaque sRGB pair only; no whole-interface conformance claim'}
        else:
            result = swatch(parse_hex(args['hex']) if args['hex'] else gamut_map(*args['oklch']))
        print(json.dumps(result, indent=2, allow_nan=False))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
