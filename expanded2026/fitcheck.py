#!/usr/bin/env python3
"""Pre-gate text-fit check: reproduce the quality checker's text extent estimate.

width_px = (wide_chars / cjk_rate + other_chars / latin_rate) * 100

"wide" is every non-ASCII character, which is why an em dash, a middle dot or a
curly quote costs about twice a Latin letter. Rates come from
`text_measure.py calibrate`, scaled by 0.92 because the checker's own estimator
carries more wrapping headroom than the calibration table reports.

Vertical extent per text element: first line top = y - 0.85*size,
last line bottom = y + 0.35*size.

Attributes inherit svg -> g -> text -> tspan, which matters after
`compact_svg_styles.py` promotes shared font-size onto the group.
"""
import sys, glob, os
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/2000/svg}'
HEADROOM = 0.92
# size -> (cjk_rate, latin_rate) chars per 100px, from text_measure.py calibrate
RATES = {
    72: (1.2, 2.5), 56: (1.7, 3.5), 48: (1.9, 3.7), 36: (2.5, 4.9),
    34: (2.8, 5.7), 28: (3.4, 6.9), 22: (4.3, 8.8), 16: (5.9, 12.1),
}
THRESHOLD = 3.0  # percent of the zone; the checker errors above 5


def width(text, size):
    key = min(RATES, key=lambda k: abs(k - size))
    cjk_rate, latin_rate = (r * HEADROOM for r in RATES[key])
    wide = sum(1 for ch in text if ord(ch) > 127)
    return (wide / cjk_rate + (len(text) - wide) / latin_rate) * 100


def rendered_lines(txt, inh):
    """[(text, size, x, anchor, y)] — one entry per rendered line."""
    size = float(txt.get('font-size', inh['font-size']))
    x = float(txt.get('x', inh['x']))
    anchor = txt.get('text-anchor', inh['text-anchor'])
    y = float(txt.get('y', 0))
    out = [[txt.text or '', size, x, anchor, y]]
    for ch in txt:
        if ch.tag != NS + 'tspan':
            continue
        csize = float(ch.get('font-size', size))
        if 'dy' in ch.attrib:
            y = y + float(ch.get('dy'))
            out.append([ch.text or '', csize, float(ch.get('x', x)),
                        ch.get('text-anchor', anchor), y])
        elif 'y' in ch.attrib:
            y = float(ch.get('y'))
            out.append([ch.text or '', csize, float(ch.get('x', x)),
                        ch.get('text-anchor', anchor), y])
        else:
            out[-1][0] += (ch.text or '')
        if ch.tail:
            out[-1][0] += ch.tail
    return [l for l in out if l[0].strip()]


def check(path):
    root = ET.parse(path).getroot()
    inh0 = {'font-size': float(root.get('font-size', 28)),
            'x': 0.0, 'text-anchor': root.get('text-anchor', 'start')}
    bad = []
    for g in root.findall(NS + 'g'):
        b = g.get('data-pptx-bounds')
        if not b:
            continue
        bx, by, bw, bh = (float(v) for v in b.split())
        inh = dict(inh0, x=bx)
        if g.get('font-size'):
            inh['font-size'] = float(g.get('font-size'))
        if g.get('text-anchor'):
            inh['text-anchor'] = g.get('text-anchor')
        for txt in g.iter(NS + 'text'):
            lines = rendered_lines(txt, inh)
            if not lines:
                continue
            top = lines[0][4] - 0.85 * lines[0][1]
            bot = lines[-1][4] + 0.35 * lines[-1][1]
            v = max(0.0, bot - (by + bh)) + max(0.0, by - top)
            if v / bh * 100 > THRESHOLD:
                bad.append((os.path.basename(path), g.get('id'), int(lines[0][1]),
                            round(bot), round(v / bh * 100, 1),
                            'VERTICAL ' + lines[0][0][:46]))
            for text, size, x, anchor, _y in lines:
                w = width(text, size)
                left = x - w if anchor == 'end' else x - w / 2 if anchor == 'middle' else x
                over = max(0.0, (left + w) - (bx + bw)) + max(0.0, bx - left)
                if over / bw * 100 > THRESHOLD:
                    bad.append((os.path.basename(path), g.get('id'), int(size),
                                round(w), round(over / bw * 100, 1), text[:56]))
    return bad


if __name__ == '__main__':
    targets = sys.argv[1:] or ['svg_output']
    rows = []
    for t in targets:
        files = sorted(glob.glob(os.path.join(t, '*.svg'))) if os.path.isdir(t) else [t]
        for f in files:
            rows += check(f)
    for r in rows:
        print('OVERFLOW %-26s %-26s %2dpx  w=%4d  +%4.1f%%  %s' % r)
    if not rows:
        print('fit OK — every line inside its module zone')
    sys.exit(1 if rows else 0)
