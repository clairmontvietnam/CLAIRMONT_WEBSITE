"""Visual content blocks for Góc nhìn articles.

Syntax inside a Markdown body (block starts with ':::type args', ends with ':::' on its own line):

:::hook
Câu mở bài lật lại một niềm tin quen thuộc.
:::

:::takeaways
- ý 1
- ý 2
:::

:::story co-hoa | Tiêu đề câu chuyện
Đoạn kể (Markdown được).
:::

:::model pyramid | Tháp nhu cầu Maslow | Abraham Maslow (1943)
- Tầng trên cùng | giải thích        (pyramid & funnel: liệt kê từ TRÊN xuống)
:::
  types: pyramid · funnel · matrix (x:/y: axis, 4 items TL,TR,BL,BR; highlight: n) · cycle · radial (center:) ·
         steps · circles (trong → ngoài) · venn (2–3 items, center:) · curve (shape: bell|s|smile|rise) ·
         spectrum (x: trái | phải) · canvas (9 ô Business Model Canvas, đúng thứ tự)

:::steps Tiêu đề phần áp dụng
- Bước | mô tả
:::

:::compare Thường làm | Nên làm
- vế trái || vế phải
:::

:::example Tiêu đề
Đoạn ví dụ giả định.
:::

:::principle
Một câu nguyên tắc.
:::

:::exercise
Một việc làm ngay.
:::

:::quote
原文
Phiên âm Hán Việt
Nghĩa
Nguồn
:::
"""
import html
import math
import re

import markdown as _md

esc = lambda s: html.escape(s or '', quote=True)


def inline(s):
    out = _md.markdown(s or '').strip()
    if out.startswith('<p>') and out.endswith('</p>') and out.count('<p>') == 1:
        out = out[3:-4]
    return out


def para(s):
    return _md.markdown(s or '')


# ---- character portraits (line icons) ----------------------------------------------------
GOLD, IVORY, RED, GREEN = '#E3CFA6', '#F6F0E6', '#C8343B', '#5E8C4A'
CHARS = {
    'co-hoa': ('Cô Hoa', 'quán cà phê đầu phố',
               f'<path d="M18 30h24v8a12 12 0 0 1-24 0z" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M42 32h3a4 4 0 0 1 0 8h-4" fill="none" stroke="{GOLD}" stroke-width="2.4"/>'
               f'<path d="M14 50h32" stroke="{IVORY}" stroke-width="2.4" stroke-linecap="round"/><path d="M25 16c-2 3 2 5 0 9M31 14c-2 3 2 5 0 9M37 16c-2 3 2 5 0 9" fill="none" stroke="{IVORY}" stroke-width="1.8" stroke-linecap="round" opacity=".8"/>'),
    'ong-thuong': ('Ông Thương', 'Tiệm Bánh Thương',
                   f'<path d="M12 40c0-10 9-16 20-16s20 6 20 16v6H12z" fill="#7A3414" stroke="{GOLD}" stroke-width="2.2"/><path d="M21 31l3 6M30 28l2 7M39 30l-1 7" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>'
                   f'<path d="M32 22c-3-4-9-2-8 2 1 3 8 7 8 7s7-4 8-7c1-4-5-6-8-2z" fill="{RED}"/>'),
    'ong-tu': ('Ông Tư', 'sạp dưa hấu',
               f'<path d="M10 28h44a22 22 0 0 1-44 0z" fill="{RED}" stroke="{GREEN}" stroke-width="4"/><circle cx="24" cy="34" r="1.8" fill="#1a0703"/><circle cx="32" cy="38" r="1.8" fill="#1a0703"/><circle cx="40" cy="34" r="1.8" fill="#1a0703"/>'),
    'di-linh': ('Dì Linh', 'quán cơm gà kiểu Đà Lạt',
                f'<path d="M12 32h40a20 20 0 0 1-40 0z" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M16 32c4-8 28-8 32 0" fill="{IVORY}" opacity=".9"/><path d="M40 12l-10 18M46 14l-12 17" stroke="{IVORY}" stroke-width="2" stroke-linecap="round"/>'),
    'ong-9-co': ('Ông 9 Cò', 'siêu thị đầu ngõ',
                 f'<path d="M12 18h6l6 22h22l5-16H21" fill="none" stroke="{GOLD}" stroke-width="2.4" stroke-linejoin="round"/><circle cx="27" cy="46" r="3" fill="{IVORY}"/><circle cx="43" cy="46" r="3" fill="{IVORY}"/>'),
    'cau-hieu': ('Cậu Hiếu', 'Khách sạn Hiếu Thảo',
                 f'<path d="M14 42a18 18 0 0 1 36 0z" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M10 46h44" stroke="{IVORY}" stroke-width="2.6" stroke-linecap="round"/><circle cx="32" cy="21" r="3" fill="{GOLD}"/>'),
    'cau-trong': ('Cậu Trống', 'xưởng đồ thủ công KỂ',
                  f'<ellipse cx="32" cy="22" rx="16" ry="6" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M16 22v18c0 3.3 7.2 6 16 6s16-2.7 16-6V22" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M20 26l8 18M44 26l-8 18" stroke="{RED}" stroke-width="2"/>'),
    'chi-thao': ('Chị Thảo', 'văn phòng tư vấn Clairmont',
                 f'<circle cx="32" cy="32" r="18" fill="none" stroke="{GOLD}" stroke-width="2.4"/><path d="M32 18l5 14-5 14-5-14z" fill="{GOLD}"/><path d="M18 32h28" stroke="{IVORY}" stroke-width="1.6" opacity=".7"/>'),
    'chu-dau-tu': ('Chủ đầu tư', 'một dự án ven đô',
                   f'<path d="M14 50V26l12-6v30M26 50V14l16 8v28M42 50V30l8 4v16" fill="none" stroke="{GOLD}" stroke-width="2.4" stroke-linejoin="round"/><path d="M10 50h44" stroke="{IVORY}" stroke-width="2.4" stroke-linecap="round"/><path d="M31 26h6M31 32h6M31 38h6" stroke="{IVORY}" stroke-width="1.8"/>'),
}


def avatar(cid):
    name, place, g = CHARS.get(cid, CHARS['chi-thao'])
    return name, place, f'<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="31" fill="#3D1201"/>{g}</svg>'


# ---- mini glyph per model type (for cards) -----------------------------------------------
def glyph(t):
    G = 'stroke="#C9AD7B" stroke-width="2" fill="none"'
    F = 'fill="#C9AD7B"'
    shapes = {
        'pyramid': f'<path d="M32 8 56 52H8z" {G}/><path d="M20 30h24M14 41h36" {G}/>',
        'funnel': f'<path d="M8 10h48L38 34v18l-12-6V34z" {G}/>',
        'matrix': f'<rect x="10" y="10" width="44" height="44" {G}/><path d="M32 10v44M10 32h44" {G}/><rect x="34" y="12" width="18" height="18" {F} opacity=".5"/>',
        'cycle': f'<circle cx="32" cy="32" r="20" {G}/><circle cx="32" cy="12" r="4" {F}/><circle cx="50" cy="40" r="4" {F}/><circle cx="14" cy="40" r="4" {F}/>',
        'radial': f'<circle cx="32" cy="32" r="8" {F}/><path d="M32 24V8M32 40v16M24 32H8M40 32h16" {G}/><circle cx="32" cy="8" r="3" {F}/><circle cx="32" cy="56" r="3" {F}/><circle cx="8" cy="32" r="3" {F}/><circle cx="56" cy="32" r="3" {F}/>',
        'steps': f'<path d="M6 44h14V34h14V24h14V14h10" {G}/>',
        'circles': f'<circle cx="32" cy="32" r="24" {G}/><circle cx="32" cy="32" r="15" {G}/><circle cx="32" cy="32" r="6" {F}/>',
        'venn': f'<circle cx="24" cy="28" r="14" {G}/><circle cx="40" cy="28" r="14" {G}/><circle cx="32" cy="42" r="14" {G}/>',
        'curve': f'<path d="M6 52C20 50 22 14 32 14s14 36 26 38" {G}/><path d="M6 54h52" {G}/>',
        'spectrum': f'<path d="M6 32h52" {G}/><circle cx="12" cy="32" r="4" {F}/><circle cx="32" cy="32" r="4" {F}/><circle cx="52" cy="32" r="4" {F}/>',
        'canvas': f'<rect x="6" y="12" width="52" height="40" {G}/><path d="M16 12v28M27 12v28M37 12v28M48 12v28M6 40h52M32 40v12M37 26h11" {G}/>',
    }
    return f'<svg viewBox="0 0 64 64" aria-hidden="true">{shapes.get(t, shapes["matrix"])}</svg>'


# ---- parsing ------------------------------------------------------------------------------
def items_of(body):
    out, opts, rest = [], {}, []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith('- '):
            parts = [p.strip() for p in s[2:].split('|', 1)]
            out.append((parts[0], parts[1] if len(parts) > 1 else ''))
        elif re.match(r'^(x|y|center|highlight|shape):', s):
            k, v = s.split(':', 1)
            opts[k.strip()] = v.strip()
        else:
            rest.append(s)
    return out, opts, ' '.join(rest)


# ---- model renderers ----------------------------------------------------------------------
def v_pyramid(items, o, funnel=False):
    n = len(items)
    rows = []
    for i, (lab, _) in enumerate(items):
        if funnel:
            w = 100 - (100 - 34) * i / max(1, n - 1)
            wn = 100 - (100 - 34) * (i + 1) / max(1, n - 1) if i < n - 1 else w * .78
            inset = max(0, (w - wn) / 2 / w * 100)
            clip = f'polygon(0 0,100% 0,{100 - inset:.1f}% 100%,{inset:.1f}% 100%)'
        else:
            w = 30 + (100 - 30) * i / max(1, n - 1)
            wp = 30 + (100 - 30) * (i - 1) / max(1, n - 1) if i else 0
            inset = (w - wp) / 2 / w * 100
            clip = 'polygon(50% 0,100% 100%,0 100%)' if i == 0 else f'polygon({inset:.1f}% 0,{100 - inset:.1f}% 0,100% 100%,0 100%)'
        shade = i / max(1, n - 1)
        rows.append(f'<div class="lv" style="width:{w:.1f}%;clip-path:{clip};--s:{shade:.2f}"><span><b>{i + 1}</b>{inline(lab)}</span></div>')
    return f'<div class="v-pyr{" funnel" if funnel else ""}">{"".join(rows)}</div>'


def v_matrix(items, o):
    x = [p.strip() for p in o.get('x', '|').split('|')]
    y = [p.strip() for p in o.get('y', '|').split('|')]
    hl = o.get('highlight', '')
    cells = ''.join(f'<div class="cell{" hl" if hl == str(i + 1) else ""}"><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, (l, _) in enumerate(items[:4]))
    return (f'<div class="v-mx"><div class="ya"><span>{esc(y[0] if y else "")}</span><span>{esc(y[1] if len(y) > 1 else "")}</span></div>'
            f'<div class="grid">{cells}</div><div class="xa"><span>{esc(x[0] if x else "")}</span><span>{esc(x[1] if len(x) > 1 else "")}</span></div></div>')


def _around(items, r=38, start=-90):
    n = len(items)
    pos = []
    for i in range(n):
        a = math.radians(start + 360 * i / n)
        pos.append((50 + r * math.cos(a), 50 + r * math.sin(a)))
    return pos


def v_cycle(items, o, radial=False):
    pos = _around(items, 38 if not radial else 39)
    n = len(items)
    svg = ['<svg viewBox="0 0 100 100" aria-hidden="true">']
    if radial:
        for (x, y) in pos:
            svg.append(f'<line x1="50" y1="50" x2="{x:.1f}" y2="{y:.1f}" stroke="rgba(201,173,123,.45)" stroke-width=".5"/>')
    else:
        svg.append('<defs><marker id="ah" viewBox="0 0 6 6" refX="3" refY="3" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0L6 3 0 6z" fill="#C9AD7B"/></marker></defs>')
        for i in range(n):
            a1 = math.radians(-90 + 360 * (i + .28) / n)
            a2 = math.radians(-90 + 360 * (i + .72) / n)
            x1, y1, x2, y2 = 50 + 38 * math.cos(a1), 50 + 38 * math.sin(a1), 50 + 38 * math.cos(a2), 50 + 38 * math.sin(a2)
            svg.append(f'<path d="M{x1:.1f} {y1:.1f}A38 38 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="#C9AD7B" stroke-width=".7" marker-end="url(#ah)"/>')
    svg.append('</svg>')
    nodes = ''.join(f'<div class="nd" style="left:{x:.1f}%;top:{y:.1f}%"><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, ((l, _), (x, y)) in enumerate(zip(items, pos)))
    center = o.get('center', '')
    c = f'<div class="ctr">{inline(center)}</div>' if center else ''
    return f'<div class="v-ring{" radial" if radial else ""}">{"".join(svg)}{c}{nodes}</div>'


def v_steps(items, o):
    cells = ''.join(f'<div class="st"><b>{i + 1:02d}</b><span>{inline(l)}</span></div>' for i, (l, _) in enumerate(items))
    return f'<div class="v-steps" style="--n:{len(items)}">{cells}</div>'


def v_circles(items, o):
    n = len(items)
    rings = []
    for i, (l, _) in enumerate(items):
        size = 34 + (96 - 34) * i / max(1, n - 1)
        rings.append(f'<div class="rg" style="width:{size:.0f}%;height:{size:.0f}%;--s:{i / max(1, n - 1):.2f};z-index:{n - i}"><span class="{"in" if i == 0 else "top"}">{inline(l)}</span></div>')
    return f'<div class="v-circ">{"".join(rings)}</div>'


def v_venn(items, o):
    n = min(3, len(items))
    P = {2: [(36, 50), (64, 50)], 3: [(38, 40), (62, 40), (50, 62)]}[max(2, n)]
    L = {2: [(22, 50), (78, 50)], 3: [(27, 26), (73, 26), (50, 82)]}[max(2, n)]
    circ = ''.join(f'<div class="vc" style="left:{x}%;top:{y}%"></div>' for x, y in P[:n])
    labs = ''.join(f'<div class="vl" style="left:{x}%;top:{y}%"><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, ((l, _), (x, y)) in enumerate(zip(items, L)))
    center = o.get('center', '')
    c = f'<div class="vctr" style="top:{48 if n == 3 else 50}%">{inline(center)}</div>' if center else ''
    return f'<div class="v-venn n{n}">{circ}{labs}{c}</div>'


def v_curve(items, o):
    shape = o.get('shape', 'bell')
    f = {'bell': lambda x: math.exp(-((x - .55) / .24) ** 2),
         's': lambda x: 1 / (1 + math.exp(-10 * (x - .5))),
         'rise': lambda x: x ** 1.6,
         'smile': lambda x: (2 * (x - .5)) ** 2}.get(shape)
    W, H, pad = 100, 56, 6
    Y = lambda x: H - pad - f(x) * (H - 2 * pad - 6)
    pts = ' '.join(f'{4 + x * 92:.1f},{Y(x):.1f}' for x in [i / 60 for i in range(61)])
    n = len(items)
    xs = [.1 + .8 * i / max(1, n - 1) for i in range(n)]
    dots = ''.join(f'<circle cx="{4 + x * 92:.1f}" cy="{Y(x):.1f}" r="1.6" fill="#E3CFA6"/>' for x in xs)
    labs = ''.join(f'<div class="cl" style="left:{(4 + x * 92):.1f}%;top:{Y(x) / H * 100:.1f}%"><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, ((l, _), x) in enumerate(zip(items, xs)))
    ax = [p.strip() for p in o.get('x', '|').split('|')]
    axis = f'<div class="cax"><span>{esc(ax[0])}</span><span>{esc(ax[1] if len(ax) > 1 else "")}</span></div>' if o.get('x') else ''
    svg = (f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="none" aria-hidden="true"><path d="M4 {H - pad} H96" stroke="rgba(201,173,123,.4)" stroke-width=".4"/>'
           f'<polyline points="{pts}" fill="none" stroke="#C9AD7B" stroke-width=".9" vector-effect="non-scaling-stroke"/>{dots}</svg>')
    return f'<div class="v-curve">{svg}{labs}</div>{axis}'


def v_spectrum(items, o):
    ax = [p.strip() for p in o.get('x', '|').split('|')]
    nodes = ''.join(f'<div class="sp"><i></i><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, (l, _) in enumerate(items))
    return f'<div class="v-spec"><div class="line"></div><div class="row">{nodes}</div><div class="cax"><span>{esc(ax[0])}</span><span>{esc(ax[1] if len(ax) > 1 else "")}</span></div></div>'


def v_canvas(items, o):
    areas = ['kp', 'ka', 'kr', 'vp', 'cr', 'ch', 'cs', 'co', 're']
    cells = ''.join(f'<div class="cv" style="grid-area:{a}"><b>{i + 1}</b><span>{inline(l)}</span></div>' for i, ((l, _), a) in enumerate(zip(items, areas)))
    return f'<div class="v-canvas">{cells}</div>'


R = {'pyramid': v_pyramid, 'funnel': lambda i, o: v_pyramid(i, o, True), 'matrix': v_matrix, 'cycle': v_cycle,
     'radial': lambda i, o: v_cycle(i, o, True), 'steps': v_steps, 'circles': v_circles, 'venn': v_venn,
     'curve': v_curve, 'spectrum': v_spectrum, 'canvas': v_canvas}


def model_html(args, body):
    parts = [p.strip() for p in args.split('|')]
    t = parts[0] if parts else 'matrix'
    title = parts[1] if len(parts) > 1 else ''
    src = parts[2] if len(parts) > 2 else ''
    items, o, _ = items_of(body)
    viz = R.get(t, v_matrix)(items, o)
    legend = ''.join(f'<li><b>{inline(l)}</b>{(" — " + inline(d)) if d else ""}</li>' for l, d in items)
    return (f'<figure class="b-model m-{t}"><figcaption><span class="k">Mô hình</span><h3>{inline(title)}</h3>'
            f'{f"<small>{esc(src)}</small>" if src else ""}</figcaption><div class="viz">{viz}</div><ol class="legend">{legend}</ol></figure>'), {'type': t, 'title': title}


# ---- other blocks -------------------------------------------------------------------------
def render_block(kind, args, body, meta):
    if kind == 'hook':
        return f'<div class="b-hook">{para(body)}</div>'
    if kind == 'takeaways':
        items, _, _ = items_of(body)
        return '<aside class="b-take"><h4>Đọc nhanh</h4><ul>' + ''.join(f'<li>{inline(l + (" | " + d if d else ""))}</li>' for l, d in items) + '</ul></aside>'
    if kind == 'story':
        p = [x.strip() for x in args.split('|', 1)]
        name, place, av = avatar(p[0])
        title = p[1] if len(p) > 1 else ''
        return (f'<figure class="b-story"><div class="av">{av}</div><div class="tx"><div class="who">Chuyện khu phố · {esc(name)} · {esc(place)}</div>'
                f'{f"<h3>{inline(title)}</h3>" if title else ""}{para(body)}</div></figure>')
    if kind == 'model':
        h, m = model_html(args, body)
        meta.setdefault('models', []).append(m)
        return h
    if kind == 'steps':
        items, _, _ = items_of(body)
        cards = ''.join(f'<li><b>{i + 1:02d}</b><h4>{inline(l)}</h4><p>{inline(d)}</p></li>' for i, (l, d) in enumerate(items))
        return f'<section class="b-steps">{f"<h3>{inline(args)}</h3>" if args else ""}<ol>{cards}</ol></section>'
    if kind == 'compare':
        lt, rt = ([p.strip() for p in args.split('|', 1)] + ['', ''])[:2]
        rows = []
        for line in body.splitlines():
            s = line.strip()
            if s.startswith('- ') and '||' in s:
                a, b = s[2:].split('||', 1)
                rows.append(f'<div class="a">{inline(a.strip())}</div><div class="b">{inline(b.strip())}</div>')
        return f'<div class="b-compare"><div class="h a">✕ {esc(lt)}</div><div class="h b">✓ {esc(rt)}</div>{"".join(rows)}</div>'
    if kind == 'example':
        return f'<div class="b-example"><div class="k">Ví dụ giả định{(" · " + esc(args)) if args else ""}</div>{para(body)}</div>'
    if kind == 'principle':
        return f'<div class="b-principle"><span class="k">📌 Nguyên tắc</span><p>{inline(body.strip())}</p></div>'
    if kind == 'exercise':
        return f'<div class="b-exercise"><span class="k">✍️ Thử ngay</span><p>{inline(body.strip())}</p></div>'
    if kind == 'quote':
        L = [l.strip() for l in body.strip().splitlines() if l.strip()] + ['', '', '', '']
        return (f'<blockquote class="b-quote"><div class="han" lang="zh-Hant">{esc(L[0])}</div><div class="hv">{esc(L[1])}</div>'
                f'<p>{esc(L[2])}</p>{f"<cite>{esc(L[3])}</cite>" if L[3] else ""}</blockquote>')
    return para(body)


BLOCK_RE = re.compile(r'^:::(\w+)[ \t]*(.*?)\n(.*?)^:::[ \t]*$', re.S | re.M)


def extract(body, meta):
    """Replace ::: blocks with placeholders; return (markdown, {token: html})."""
    store = {}

    def sub(m):
        tok = f'CLMBLOCK{len(store)}X'
        store[tok] = render_block(m.group(1), m.group(2).strip(), m.group(3), meta)
        return f'\n\n{tok}\n\n'
    return BLOCK_RE.sub(sub, body), store


def restore(html_text, store):
    for tok, h in store.items():
        html_text = html_text.replace(f'<p>{tok}</p>', h).replace(tok, h)
    return html_text
