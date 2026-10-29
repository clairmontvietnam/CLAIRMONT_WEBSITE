#!/usr/bin/env python3
"""Clairmont Group — static site builder.

    python3 tools/build.py

Inputs : src/layout.html, src/pages/*.html, content/services/*.md, content/posts/*.md
Outputs: index.html, gioi-thieu/, linh-vuc/, goc-nhin/ (+ one folder per post), lien-he/,
         dich-vu/ (+ one folder per service), 404.html, sitemap.xml, robots.txt, feed.xml, llms.txt

New daily article = add one file to content/posts/ (frontmatter + Markdown) and run this script.
"""
import datetime as dt, html, json, os, re, shutil, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://www.clairmontgroup.vn'
TODAY = dt.date.today().isoformat()
OG_IMAGE = SITE + '/assets/og-clairmont.jpg'
FORM_ENDPOINT = ''  # Google Apps Script / Formspree URL for the contact form (empty = manual copy mode)

ORG = {
    'name': 'Clairmont Group',
    'legal': 'Công ty TNHH Clairmont Group',
    'alt': ['Clairmont Việt Nam', 'Clairmont Vietnam', 'Clairmont'],
    'tax': '0111450942',
    'founded': '2021-04-17',
    'email': 'clairmontvietnam@gmail.com',
    'phone': '+84947120258',
    'street': 'Căn SH03, Tầng 1–2, Tòa nhà Trinity Tower, 145 Hồ Mễ Trì',
    'locality': 'Phường Đại Mỗ',
    'region': 'Hà Nội',
    'slogan': 'Bản sắc dẫn lối chiến lược · Identity Inspires Strategy',
    'same_as': [],  # add official Facebook / LinkedIn / TikTok / YouTube URLs here
    'founder': 'Tô Thị Thu Thảo',
    'founder_img': '/assets/media/img-1660bf6ddb.webp',
}

# ---- core pages ------------------------------------------------------------------------
CORE = [
    # key, fragment, url, nav, title, description
    ('home', 'home', '/', '/',
     'Clairmont Group – Tư vấn chiến lược & phát triển thương hiệu',
     'Clairmont Group (Clairmont Việt Nam): tư vấn chiến lược doanh nghiệp, tái cấu trúc, tư vấn bất động sản, định vị và phát triển thương hiệu tại Hà Nội.'),
    ('gioi-thieu', 'gioi-thieu', '/gioi-thieu/', '/gioi-thieu/',
     'Giới thiệu Clairmont Group – Nhà sáng lập Tô Thị Thu Thảo',
     'Clairmont Group – tư vấn chiến lược tại Hà Nội, do Tô Thị Thu Thảo sáng lập năm 2021. Sứ mệnh, cách làm việc, năng lực và định hướng 2027–2030.'),
    ('linh-vuc', 'linh-vuc', '/linh-vuc/', '/linh-vuc/',
     'Lĩnh vực: tư vấn chiến lược & thương hiệu | Clairmont Group',
     'Ba lĩnh vực của Clairmont Group: tư vấn chiến lược doanh nghiệp và bất động sản, phát triển thương hiệu FLEUR · KỂ · MỜI, chuỗi giá trị.'),
    ('goc-nhin', 'goc-nhin', '/goc-nhin/', '/goc-nhin/',
     'Góc nhìn – Chiến lược, bất động sản, thương hiệu | Clairmont',
     'Bài viết của Clairmont Group về chiến lược doanh nghiệp, tái cấu trúc, thị trường bất động sản, định vị và phát triển thương hiệu. Cập nhật thường xuyên.'),
    ('lien-he', 'lien-he', '/lien-he/', '/lien-he/',
     'Liên hệ Clairmont Group – Tư vấn chiến lược tại Hà Nội',
     'Liên hệ Clairmont Group: hotline 0947 120 258, clairmontvietnam@gmail.com, Trinity Tower, 145 Hồ Mễ Trì, Hà Nội. Đặt lịch trao đổi về chiến lược.'),
]
NEXT = {'home': 'gioi-thieu', 'gioi-thieu': 'linh-vuc', 'linh-vuc': 'goc-nhin', 'goc-nhin': 'lien-he', 'lien-he': 'home'}
SERVICE_ORDER = ['tu-van-chien-luoc-doanh-nghiep', 'tai-cau-truc-doanh-nghiep', 'tu-van-bat-dong-san',
                 'dinh-vi-thuong-hieu', 'phat-trien-thuong-hieu', 'phat-trien-chuoi-gia-tri']
GENERATED = ['gioi-thieu', 'linh-vuc', 'goc-nhin', 'lien-he', 'dich-vu']


def esc(s):
    return html.escape(s or '', quote=True)


def read(p):
    return Path(p).read_text(encoding='utf-8')


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')


# ---- content -----------------------------------------------------------------------------
def parse_md(path):
    raw = read(path)
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m:
        sys.exit(f'missing frontmatter: {path}')
    meta = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip().strip('"')
    body = m.group(2).strip()
    meta.setdefault('slug', Path(path).stem)
    meta['keywords_list'] = [k.strip() for k in meta.get('keywords', '').split(',') if k.strip()]
    # FAQ = last "## Câu hỏi thường gặp" section, "### question" + answer
    faq = []
    fm = re.search(r'^##\s+Câu hỏi thường gặp.*$', body, re.M)
    if fm:
        faq_txt = body[fm.end():]
        body = body[:fm.start()].rstrip()
        for q in re.finditer(r'^###\s+(.+?)\n(.*?)(?=^###\s|\Z)', faq_txt, re.S | re.M):
            faq.append((q.group(1).strip(), ' '.join(q.group(2).split())))
    md = markdown.Markdown(extensions=['toc', 'tables', 'sane_lists'], extension_configs={'toc': {'toc_depth': '2'}})
    meta['html'] = md.convert(body)
    meta['toc'] = [(t['id'], t['name']) for t in md.toc_tokens]
    meta['faq'] = faq
    meta['words'] = len(re.sub(r'<[^>]+>', ' ', meta['html']).split())
    meta['minutes'] = max(3, round(meta['words'] / 220))
    return meta


def load(dirname):
    d = ROOT / 'content' / dirname
    return [parse_md(p) for p in sorted(d.glob('*.md'))] if d.exists() else []


# ---- head / schema -------------------------------------------------------------------------
def org_graph():
    o = ORG
    org = {
        '@type': ['Organization', 'ProfessionalService'], '@id': SITE + '/#org',
        'name': o['name'], 'legalName': o['legal'], 'alternateName': o['alt'],
        'url': SITE + '/', 'logo': SITE + '/icon-512.png', 'image': OG_IMAGE,
        'email': o['email'], 'telephone': o['phone'], 'taxID': o['tax'], 'foundingDate': o['founded'],
        'slogan': o['slogan'], 'priceRange': 'Theo phạm vi dự án',
        'address': {'@type': 'PostalAddress', 'streetAddress': o['street'], 'addressLocality': o['locality'],
                    'addressRegion': o['region'], 'addressCountry': 'VN'},
        'areaServed': {'@type': 'Country', 'name': 'Việt Nam'},
        'founder': {'@id': SITE + '/#founder'},
        'knowsAbout': ['Tư vấn chiến lược doanh nghiệp', 'Tái cấu trúc doanh nghiệp', 'Tư vấn bất động sản',
                       'Định vị thương hiệu', 'Phát triển thương hiệu', 'Phát triển chuỗi giá trị'],
    }
    if o['same_as']:
        org['sameAs'] = o['same_as']
    person = {'@type': 'Person', '@id': SITE + '/#founder', 'name': o['founder'],
              'jobTitle': 'Nhà sáng lập & Giám đốc', 'worksFor': {'@id': SITE + '/#org'},
              'image': SITE + o['founder_img'], 'url': SITE + '/gioi-thieu/#nha-sang-lap'}
    site = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Clairmont Group',
            'alternateName': ['Clairmont Việt Nam', 'Clairmont'], 'inLanguage': 'vi-VN', 'publisher': {'@id': SITE + '/#org'}}
    return [org, person, site]


def crumbs_ld(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}


def head(title, desc, url, og_type='website', extra=None, image=OG_IMAGE):
    graph = org_graph() + [{'@type': 'WebPage', '@id': SITE + url + '#page', 'url': SITE + url, 'name': title,
                            'description': desc, 'isPartOf': {'@id': SITE + '/#website'}, 'inLanguage': 'vi-VN'}]
    graph += extra or []
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
    return '\n'.join([
        f'<title>{esc(title)}</title>',
        f'<meta name="description" content="{esc(desc)}">',
        f'<link rel="canonical" href="{SITE}{url}">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<meta property="og:type" content="{og_type}">',
        '<meta property="og:site_name" content="Clairmont Group">',
        '<meta property="og:locale" content="vi_VN">',
        f'<meta property="og:url" content="{SITE}{url}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:image" content="{image}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<link rel="icon" href="/favicon.ico" sizes="48x48">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
        '<link rel="alternate" type="application/rss+xml" title="Clairmont Group – Góc nhìn" href="/feed.xml">',
        '<meta name="theme-color" content="#120503">',
        f'<script type="application/ld+json">{ld}</script>',
        '<script>window.CLM_FORM=' + json.dumps({'endpoint': FORM_ENDPOINT}) + ';</script>',
    ])


LAYOUT = None


def render(url, head_html, main_html, nav_url):
    out = LAYOUT.replace('{{HEAD}}', head_html).replace('{{MAIN}}', main_html)
    # current nav item
    out = re.sub(r'(<a href="' + re.escape(nav_url) + r'"(?: class="nav-ct")?)', r'\1 aria-current="page"', out, count=1) if nav_url else out
    if nav_url == '/lien-he/':
        out = out.replace('<a class="cta" href="/lien-he/"', '<a class="cta" href="/lien-he/" aria-current="page"', 1)
    rel = 'index.html' if url == '/' else url.strip('/') + '/index.html'
    write(rel, out)


def nextp(key, titles):
    n = NEXT[key]
    nurl = '/' if n == 'home' else f'/{n}/'
    t, te = titles[n]
    return (f'<nav class="nextp wrap" aria-label="Trang tiếp"><a href="{nurl}"><span data-en="Next →">Tiếp theo →</span>'
            f'<strong data-en="{esc(te)}">{esc(t)}</strong></a></nav>')


def crumb_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        if i:
            parts.append('<span aria-hidden="true">/</span>')
        parts.append(f'<a href="{u}">{esc(n)}</a>' if i < len(items) - 1 else f'<span>{esc(n)}</span>')
    return '<nav class="crumb" aria-label="Breadcrumb">' + ''.join(parts) + '</nav>'


def cta_box():
    return ('<div class="cta-box"><div><h3 data-en="Talk to Clairmont">Trao đổi cùng Clairmont</h3>'
            '<p data-en="Share your situation and Clairmont will get back to you.">Chia sẻ bài toán của doanh nghiệp, Clairmont sẽ liên hệ lại để trao đổi.</p></div>'
            '<a class="btn solid" href="/lien-he/"><span data-en="Request a meeting">Đặt lịch trao đổi</span><b aria-hidden="true">→</b></a></div>')


def faq_html(faq):
    if not faq:
        return ''
    items = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)
    return f'<section class="faq" id="cau-hoi"><h2>Câu hỏi thường gặp</h2>{items}</section>'


def faq_ld(faq):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q,
            'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}


def toc_box(toc):
    if len(toc) < 3:
        return ''
    li = ''.join(f'<li><a href="#{i}">{esc(n)}</a></li>' for i, n in toc)
    return f'<div class="glass"><h4>Nội dung</h4><ol>{li}</ol></div>'


def card(url, k, title, summary, go='Đọc tiếp →'):
    return (f'<a class="card" href="{url}"><span class="k">{esc(k)}</span><h3>{esc(title)}</h3>'
            f'<p>{esc(summary)}</p><span class="go">{go}</span></a>')


def fmt_date(d):
    y, m, dd = d.split('-')
    return f'{dd}/{m}/{y}'


# ---- build -------------------------------------------------------------------------------
def main():
    global LAYOUT
    import hashlib
    ver = hashlib.sha1((read(ROOT / 'assets/site.css') + read(ROOT / 'assets/site.js') + read(ROOT / 'assets/sprite.svg')).encode()).hexdigest()[:8]
    LAYOUT = read(ROOT / 'src/layout.html').replace('{{V}}', ver)
    services = {s['slug']: s for s in load('services')}
    services = [services[k] for k in SERVICE_ORDER if k in services] + [s for k, s in services.items() if k not in SERVICE_ORDER]
    posts = sorted(load('posts'), key=lambda p: (p.get('date', ''), p['slug']), reverse=True)
    posts = [p for p in posts if p.get('date', '') <= TODAY and p.get('draft', '').lower() != 'true']

    for d in GENERATED:  # clean previous output
        shutil.rmtree(ROOT / d, ignore_errors=True)

    titles = {'home': ('Trang chủ', 'Home'), 'gioi-thieu': ('Giới thiệu', 'About'), 'linh-vuc': ('Lĩnh vực', 'Services'),
              'goc-nhin': ('Góc nhìn', 'Insights'), 'lien-he': ('Liên hệ', 'Contact')}
    urls = []

    # core pages
    for key, frag, url, nav, title, desc in CORE:
        body = read(ROOT / f'src/pages/{frag}.html')
        if '{{POSTS}}' in body:
            latest = ''.join(card(f'/goc-nhin/{p["slug"]}/', f'{p.get("category", "Góc nhìn")} · {fmt_date(p["date"])}', p['h1'] if p.get('h1') else p['title'], p.get('summary', p['description']))
                             for p in posts)
            block = (f'<div class="posts-head"><h2 class="subh" style="margin:0" data-en="Latest articles">Bài viết mới</h2></div>'
                     f'<div class="cards">{latest}</div>') if posts else ''
            body = body.replace('{{POSTS}}', block)
        main_html = f'<div class="page" id="p-{key}">\n{body}{nextp(key, titles)}\n</div>'
        extra = [] if key == 'home' else [crumbs_ld([('Trang chủ', '/'), (titles[key][0], url)])]
        render(url, head(title, desc, url, extra=extra), main_html, nav)
        urls.append((url, TODAY, '1.0' if key == 'home' else '0.8'))

    # services hub + pages
    svc_cards = ''.join(card(f'/dich-vu/{s["slug"]}/', 'Dịch vụ', s['h1'], s.get('summary', s['description']), 'Xem chi tiết →') for s in services)
    hub = (f'<div class="page" id="p-dich-vu"><section class="sec"><div class="wrap">'
           f'{crumb_html([("Trang chủ", "/"), ("Dịch vụ", "/dich-vu/")])}'
           f'<div class="art-head"><div class="lbl">Dịch vụ</div><h1>Dịch vụ tư vấn của Clairmont Group</h1>'
           f'<p class="dek">Tư vấn chiến lược doanh nghiệp, tái cấu trúc, tư vấn bất động sản, định vị và phát triển thương hiệu, phát triển chuỗi giá trị — bắt đầu từ bản sắc, đồng hành đến khi triển khai.</p></div>'
           f'<div class="cards" style="margin-top:40px">{svc_cards}</div>{cta_box()}</div></section></div>')
    render('/dich-vu/', head('Dịch vụ tư vấn chiến lược & thương hiệu | Clairmont Group',
                             'Dịch vụ của Clairmont Group: tư vấn chiến lược doanh nghiệp, tái cấu trúc, tư vấn bất động sản, định vị và phát triển thương hiệu, chuỗi giá trị.',
                             '/dich-vu/', extra=[crumbs_ld([('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/')])]), hub, '/linh-vuc/')
    urls.append(('/dich-vu/', TODAY, '0.9'))

    for s in services:
        url = f'/dich-vu/{s["slug"]}/'
        cr = [('Trang chủ', '/'), ('Dịch vụ', '/dich-vu/'), (s['h1'], url)]
        others = ''.join(f'<li><a href="/dich-vu/{o["slug"]}/">{esc(o["h1"])}</a></li>' for o in services if o is not s)
        rel_posts = [p for p in posts if url in p['html']][:4]
        rel = ''.join(f'<li><a href="/goc-nhin/{p["slug"]}/">{esc(p.get("h1") or p["title"])}</a></li>' for p in rel_posts)
        side = toc_box(s['toc']) + f'<div class="glass"><h4>Dịch vụ khác</h4><ul>{others}</ul></div>' + (f'<div class="glass"><h4>Bài viết liên quan</h4><ul>{rel}</ul></div>' if rel else '')
        page = (f'<div class="page" id="p-svc"><section class="sec"><div class="wrap">{crumb_html(cr)}'
                f'<header class="art-head"><div class="lbl">Dịch vụ · Clairmont Group</div><h1>{esc(s["h1"])}</h1><p class="dek">{esc(s["description"])}</p></header>'
                f'<div class="art-grid"><div><article class="prose">{s["html"]}{faq_html(s["faq"])}</article>{cta_box()}</div>'
                f'<aside class="art-side">{side}</aside></div></div></section></div>')
        ld = [crumbs_ld(cr), {'@type': 'Service', 'name': s['h1'], 'serviceType': s['keywords_list'][0] if s['keywords_list'] else s['h1'],
                              'description': s['description'], 'url': SITE + url, 'provider': {'@id': SITE + '/#org'},
                              'areaServed': {'@type': 'Country', 'name': 'Việt Nam'}}]
        if s['faq']:
            ld.append(faq_ld(s['faq']))
        render(url, head(s['title'], s['description'], url, extra=ld), page, '/linh-vuc/')
        urls.append((url, TODAY, '0.9'))

    # posts
    for i, p in enumerate(posts):
        url = f'/goc-nhin/{p["slug"]}/'
        h1 = p.get('h1') or p['title']
        cr = [('Trang chủ', '/'), ('Góc nhìn', '/goc-nhin/'), (h1, url)]
        more = [q for q in posts if q is not p][:4]
        more_html = ''.join(f'<li><a href="/goc-nhin/{q["slug"]}/">{esc(q.get("h1") or q["title"])}</a></li>' for q in more)
        svc_html = ''.join(f'<li><a href="/dich-vu/{s["slug"]}/">{esc(s["h1"])}</a></li>' for s in services if f'/dich-vu/{s["slug"]}/' in p['html']) or \
            ''.join(f'<li><a href="/dich-vu/{s["slug"]}/">{esc(s["h1"])}</a></li>' for s in services[:3])
        side = toc_box(p['toc']) + f'<div class="glass"><h4>Dịch vụ liên quan</h4><ul>{svc_html}</ul></div>' + (f'<div class="glass"><h4>Bài viết khác</h4><ul>{more_html}</ul></div>' if more_html else '')
        author = p.get('author', 'Clairmont Group')
        page = (f'<div class="page" id="p-post"><section class="sec"><div class="wrap">{crumb_html(cr)}'
                f'<header class="art-head"><div class="lbl">{esc(p.get("category", "Góc nhìn"))}</div><h1>{esc(h1)}</h1><p class="dek">{esc(p["description"])}</p>'
                f'<div class="art-meta"><span>{esc(author)}</span><time datetime="{p["date"]}">{fmt_date(p["date"])}</time><span>{p["minutes"]} phút đọc</span></div></header>'
                f'<div class="art-grid"><div><article class="prose">{p["html"]}{faq_html(p["faq"])}</article>{cta_box()}</div>'
                f'<aside class="art-side">{side}</aside></div></div></section></div>')
        auth_ld = {'@id': SITE + '/#founder'} if author == ORG['founder'] else {'@id': SITE + '/#org'}
        ld = [crumbs_ld(cr), {'@type': 'BlogPosting', 'headline': h1[:110], 'description': p['description'], 'url': SITE + url,
                              'mainEntityOfPage': SITE + url, 'datePublished': p['date'], 'dateModified': p.get('updated', p['date']),
                              'inLanguage': 'vi-VN', 'author': auth_ld, 'publisher': {'@id': SITE + '/#org'}, 'image': OG_IMAGE,
                              'keywords': ', '.join(p['keywords_list']), 'articleSection': p.get('category', 'Góc nhìn'), 'wordCount': p['words']}]
        if p['faq']:
            ld.append(faq_ld(p['faq']))
        render(url, head(p['title'], p['description'], url, og_type='article', extra=ld), page, '/goc-nhin/')
        urls.append((url, p.get('updated', p['date']), '0.7'))

    # 404
    nf = ('<div class="page" id="p-404"><section class="sec"><div class="wrap"><div class="art-head"><div class="lbl">404</div>'
          '<h1>Không tìm thấy trang</h1><p class="dek">Trang này đã được chuyển hoặc không còn tồn tại.</p>'
          '<div class="ctas" style="margin-top:28px"><a class="btn solid" href="/"><span>Về trang chủ</span><b aria-hidden="true">→</b></a>'
          '<a class="pill" href="/dich-vu/"><i></i><span>Xem dịch vụ</span></a></div></div></div></section></div>')
    out = LAYOUT.replace('{{HEAD}}', head('Không tìm thấy trang | Clairmont Group', 'Trang không tồn tại.', '/404/').replace(
        '<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')).replace('{{MAIN}}', nf)
    write('404.html', out)

    # sitemap / robots / feed / llms
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f'<url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>' for u, d, pr in urls]
    sm.append('</urlset>')
    write('sitemap.xml', '\n'.join(sm) + '\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /src/\nDisallow: /tools/\nDisallow: /content/\n\nSitemap: {SITE}/sitemap.xml\n')
    items = ''.join(
        f'<item><title>{esc(p.get("h1") or p["title"])}</title><link>{SITE}/goc-nhin/{p["slug"]}/</link><guid>{SITE}/goc-nhin/{p["slug"]}/</guid>'
        f'<pubDate>{dt.datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 07:00:00 +0700")}</pubDate><description>{esc(p["description"])}</description></item>'
        for p in posts[:30])
    write('feed.xml', f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Clairmont Group – Góc nhìn</title>'
                      f'<link>{SITE}/goc-nhin/</link><description>Chiến lược doanh nghiệp, bất động sản, thương hiệu</description><language>vi</language>{items}</channel></rss>\n')
    llms = ['# Clairmont Group (Clairmont Việt Nam)', '',
            '> Công ty TNHH Clairmont Group — doanh nghiệp tư vấn chiến lược, phát triển thương hiệu và phát triển chuỗi giá trị tại Hà Nội, thành lập 17/04/2021. Nhà sáng lập & Giám đốc: Tô Thị Thu Thảo. Slogan: "Bản sắc dẫn lối chiến lược" (Identity Inspires Strategy).',
            '', 'Liên hệ: 0947 120 258 · clairmontvietnam@gmail.com · Trinity Tower, 145 Hồ Mễ Trì, Hà Nội · MST 0111450942', '', '## Trang chính']
    llms += [f'- [{t}]({SITE}{u}): {d}' for k, f, u, n, t, d in CORE]
    llms += ['', '## Dịch vụ'] + [f'- [{s["h1"]}]({SITE}/dich-vu/{s["slug"]}/): {s["description"]}' for s in services]
    llms += ['', '## Bài viết'] + [f'- [{p.get("h1") or p["title"]}]({SITE}/goc-nhin/{p["slug"]}/): {p["description"]}' for p in posts]
    write('llms.txt', '\n'.join(llms) + '\n')
    print(f'built {len(urls)} pages · {len(services)} services · {len(posts)} posts')


if __name__ == '__main__':
    main()
