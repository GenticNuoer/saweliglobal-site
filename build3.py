# -*- coding: utf-8 -*-
import json, os, shutil, html, sys
sys.path.insert(0, '/home/claude/site2')
from imgs import I
M = json.load(open('/home/claude/site2_map.json'))
SRC = '/home/claude/site3/src'; D = '/home/claude/site3/out'
PHONE = '+252 614 264 999'; TEL = '+252614264999'; EMAIL = 'hello@saweli.com'; WA = 'https://wa.me/252614264999'
SITE = 'https://saweli.com'
E = lambda s: html.escape(str(s), quote=True)
USED = {}
def src(k, w): USED[k] = I[k]; return f'/img/{k}-{w}.jpg'
def img(k, alt='', w=1600, sizes='100vw', cls='', lazy=True, extra=''):
    s = f'{src(k,800)} 800w, {src(k,1600)} 1600w'
    return (f'<img src="{src(k, 1600 if w > 800 else 800)}" srcset="{s}" sizes="{sizes}" alt="{E(alt)}"'
            f'{" class=%s" % chr(34)+cls+chr(34) if cls else ""}{" loading=lazy" if lazy else " fetchpriority=high"} decoding="async"{extra}>')
AR = '<svg class="ar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARU = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M7 17L17 7M8 7h9v9"/></svg>'
CARET = '<svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M6 9l6 6 6-6"/></svg>'
IC = {
 'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'wa': '<path d="M3 21l1.7-5A9 9 0 1 1 8 19.3z"/><path d="M9 9.5c.5 2 2.5 4 4.5 4.5l1-1.2 2 .8c0 1.2-1 2-2.2 1.9C11 15 9 13 8.5 9.7 8.4 8.5 9.3 7.5 10.5 7.5l.8 2z"/>',
 'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 'box': '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
 'ship': '<path d="M3 17l2 4h14l2-4H3z"/><path d="M5 17V10h14v7M9 10V6h6v4M12 3v3"/>',
 'bank': '<path d="M3 10l9-6 9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
 'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
 'pin': '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
}
def ic(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{IC[n]}</svg>'
LOGO_W = '/brand/saweli-white.svg'; LOGO_C = '/brand/saweli-colour.svg'

NAV = [('How it works', '/how-it-works/'),
       ('Services', None, [('Sourcing', '/sourcing/', 'cn_wholesale', 'Find and check suppliers in China'),
                           ('Inspection', '/how-it-works/#inspection', 'cn_inspector', 'Goods checked before they ship'),
                           ('Logistics', '/logistics/', 'ship_aerial2', 'Sea, air and road to your door'),
                           ('For banks', '/banks/', 'handshake', 'Verified trade behind each payment')]),
       ('Corridors', '/corridors/'), ('About', '/about/'), ('Contact', '/contact/')]

def header(cur, light=False):
    items = ''
    for n in NAV:
        if n[1] is None:
            mega = ''.join(f'<a href="{h}">{img(k, "", 800, "92px")}<span><b>{E(t)}</b><small>{E(s)}</small></span></a>' for t, h, k, s in n[2])
            on = ' aria-current="page"' if any(cur == h for _, h, _, _ in n[2]) else ''
            items += f'<div class="dd"><button type="button"{on} aria-haspopup="true">{E(n[0])}{CARET}</button><div class="mega">{mega}</div></div>'
        else:
            items += f'<a href="{n[1]}"{" aria-current=page" if cur == n[1] else ""}>{E(n[0])}</a>'
    dl = [('Home', '/'), ('How it works', '/how-it-works/'), ('Sourcing', '/sourcing/'), ('Logistics', '/logistics/'), ('Corridors', '/corridors/'), ('For banks', '/banks/'), ('About', '/about/'), ('Contact', '/contact/')]
    drawer = ''.join(f'<a href="{h}">{E(t)}</a>' for t, h in dl)
    return f'''<div class="prog" aria-hidden="true"></div><div class="cur" aria-hidden="true"><span></span></div>
<header class="top{" light" if light else ""}"><div class="wrap"><a class="brand" href="/" aria-label="Saweli home"><img class="w" src="{LOGO_W}" alt="Saweli" width="150" height="43"><img class="c" src="{LOGO_C}" alt="Saweli" width="150" height="43"></a>
<nav class="nav" aria-label="Main">{items}</nav>
<div class="tools"><div class="lang"><button type="button" aria-haspopup="true">EN</button><ul><li><a href="/" lang="en">English</a></li><li><a href="/zh/" lang="zh">中文</a></li><li><a href="/so/" lang="so">Soomaali</a></li><li><a href="/sw/" lang="sw">Kiswahili</a></li></ul></div>
<a class="btn sm" href="/contact/">Start an order</a><button class="burger" type="button" aria-label="Menu" aria-expanded="false"><i></i><i></i></button></div></div></header>
<div class="drawer"><nav aria-label="Mobile">{drawer}</nav><div class="dfoot"><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="/zh/">中文</a><a href="/so/">Soomaali</a><a href="/sw/">Kiswahili</a></div></div>'''

LOADER = '<div class="loader" aria-hidden="true"><img src="/brand/saweli-mark.svg" alt="" width="240" height="124"><span class="lzh">萨维利</span><i class="bar"></i></div>'

def cta_end(h='Ready to <em>trade?</em>', p='Tell us what you want to buy or sell. We reply within one working day with the next steps and what it will cost.'):
    return f'''<section class="cta-end"><div class="wrap"><span class="kicker lt r">Start an order</span><h2 data-split>{h}</h2>
<div class="row"><p class="lede r" style="color:rgba(255,255,255,.75);max-width:44ch;margin:0">{E(p)}</p><div class="ctas r d1"><a class="btn" href="/contact/">Start an order {AR}</a><a class="btn ghost" href="{WA}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
<div class="row r d2" style="margin-top:56px"><a class="big-tel" href="tel:{TEL}">{PHONE}</a><a class="big-tel" href="mailto:{EMAIL}">{EMAIL}</a></div></div></section>'''

def footer():
    cols = [('Services', [('How it works', '/how-it-works/'), ('Sourcing', '/sourcing/'), ('Inspection', '/how-it-works/#inspection'), ('Logistics', '/logistics/'), ('For banks', '/banks/')]),
            ('Company', [('About', '/about/'), ('Corridors', '/corridors/'), ('Contact', '/contact/'), ('Privacy', '/privacy/')]),
            ('Languages', [('English', '/'), ('中文', '/zh/'), ('Soomaali', '/so/'), ('Kiswahili', '/sw/')])]
    cc = ''.join(f'<div><h4>{E(h)}</h4><ul>' + ''.join(f'<li><a href="{u}">{E(t)}</a></li>' for t, u in l) + '</ul></div>' for h, l in cols)
    return f'''<footer class="foot"><div class="wrap"><div class="grid"><div class="brandf"><img src="{LOGO_W}" alt="Saweli" width="160" height="46"><p>Trade between East Africa and China. Verified suppliers, inspected goods, freight to your port and payment through partner banks.</p></div>{cc}
<div><h4>Trade notes, once a month</h4><p style="font-size:14.5px">Freight, prices and market news from the corridor. No spam.</p><form class="sub" data-ok="Thank you. You are on the list." data-err="That did not go through. Please try again."><input type="email" name="email" required placeholder="Your email" aria-label="Your email"><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button>Subscribe</button></form><p class="submsg" role="status"></p></div></div>
<div class="huge" aria-hidden="true">saweli</div>
<div class="legal"><span>© 2026 Saweli. Payments are processed by partner banks. Saweli does not take deposits.</span><span><a href="/privacy/">Privacy</a></span></div></div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Message Saweli on WhatsApp" data-l="Chat on WhatsApp">{ic('wa')}</a>'''

ZHP = {'How it works': '运作方式', 'Sourcing': '采购与出口', 'Logistics': '物流运输', 'Corridors': '贸易走廊', 'For banks': '银行合作', 'About': '关于萨维利'}
ZHK = {'Why Saweli': '为什么选择萨维利', 'What we do': '我们的服务', 'The journey': '流程', 'Watch': '影片', 'The corridor': '贸易走廊', 'What moves': '货物', 'Markets': '市场',
       'For banks': '银行合作', 'Questions': '常见问题', 'Start an order': '开始下单', 'The film': '影片', 'Step by step': '逐步说明', 'What you get': '您将获得', 'Buying from China': '从中国采购',
       'From China': '来自中国', 'Selling to China': '销往中国', 'From East Africa': '来自东非', 'Supplier checks': '供应商核查', 'How we move it': '运输方式', 'Routes': '航线', 'Ports': '港口',
       'Paperwork': '单证', 'The map': '地图', 'Cities': '城市', 'Coming next': '下一步', 'The problem': '问题所在', 'How it fits': '合作方式', 'Our view': '我们的看法', 'How we work': '工作原则',
       'Where we are going': '发展方向', 'Before you write': '联系之前'}
import re
def zhk(h):
    return re.sub(r'(<span class="kicker[^"]*">)([^<]+)(</span>)', lambda m: m.group(1) + m.group(2) + (f'<span class="zh" lang="zh">{ZHK[m.group(2)]}</span>' if m.group(2) in ZHK else '') + m.group(3), h)
def page(path, title, desc, body, cur='', light=False, og='/og.jpg', extra_js=''):
    url = SITE + path
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "Saweli", "url": SITE, "logo": SITE + LOGO_C,
          "telephone": PHONE, "email": EMAIL, "areaServed": ["Somalia", "Kenya", "Tanzania", "Ethiopia", "Uganda", "Djibouti", "China"]}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}{og}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B1410"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" hreflang="en" href="{SITE}/"><link rel="alternate" hreflang="zh" href="{SITE}/zh/"><link rel="alternate" hreflang="so" href="{SITE}/so/"><link rel="alternate" hreflang="sw" href="{SITE}/sw/">
<link rel="preload" href="/assets/fonts/bigshoulders.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v=6"><script type="application/ld+json">{json.dumps(ld)}</script></head>
<body><a class="skip" href="#main">Skip to content</a>{LOADER}{header(cur, light)}<main id="main">{zhk(body)}</main>{footer()}
<script src="/assets/app.js?v=6" defer></script>{extra_js}</body></html>'''

def phero(k, crumb, h, lede, meta=None, extra=''):
    zh = ZHP.get(crumb, '')
    m = ''
    if meta: m = '<div class="meta r d3">' + ''.join(f'<div><b>{E(a)}</b>{E(b)}</div>' for a, b in meta) + '</div>'
    return f'''<section class="phero"><div class="bg" data-par=".12">{img(k, "", 1600, lazy=False)}</div><div class="wrap"><div class="crumbs r"><a href="/">Home</a><span>/</span><span>{E(crumb)}</span></div>
<h1 data-split=".2">{h}</h1>{f'<span class="zh-big r d2" lang="zh">{zh}</span>' if zh else ''}<p class="lede r d2">{E(lede)}</p>{extra}{m}</div></section>'''

def mapsvg(mode='full'):
    W, H = M['W'], M['H']
    LBL = {'Mogadishu': (12, 5, 'start'), 'Bosaso': (12, 5, 'start'), 'Djibouti': (-12, -6, 'end'), 'Mombasa': (12, 6, 'start'), 'Dar es Salaam': (12, 8, 'start'), 'Nairobi': (-12, 4, 'end'),
           'Addis Ababa': (-12, 4, 'end'), 'Kampala': (-12, 4, 'end'), 'Yiwu': (-12, 4, 'end'), 'Ningbo': (12, 4, 'start'), 'Shanghai': (-10, -10, 'end'), 'Guangzhou': (-12, -6, 'end'), 'Shenzhen': (10, 14, 'start')}
    grid = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W + 1, 80)) + ''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0, H + 1, 80))
    cities = ''
    for n, (x, y) in M['cities'].items():
        dx, dy, an = LBL.get(n, (12, 4, 'start'))
        big = n in ('Mogadishu', 'Yiwu', 'Djibouti', 'Mombasa', 'Dar es Salaam', 'Guangzhou', 'Ningbo')
        cities += f'<g class="city">{f"<circle class=pulse cx={x} cy={y} r=6 />" if big else ""}<circle class="dot" cx="{x}" cy="{y}" r="{5 if big else 3.5}"/><text x="{x+dx}" y="{y+dy}" text-anchor="{an}">{E(n)}</text></g>'
    roads = ''.join(f'<path class="route road draw" d="{r}"/>' for r in M['roads'])
    ships = f'''<circle r="7" fill="#fff"><animateMotion dur="22s" repeatCount="indefinite" path="{M['sea']}"/></circle><circle r="7" fill="#fff"><animateMotion dur="22s" begin="-11s" repeatCount="indefinite" path="{M['sea']}"/></circle>
<circle r="6" fill="#fff"><animateMotion dur="12s" repeatCount="indefinite" path="{M['seaS']}"/></circle><circle r="5" fill="#FFE07A"><animateMotion dur="9s" repeatCount="indefinite" path="{M['air']}"/></circle>'''
    return f'''<div class="mapbox"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Trade routes between China and East Africa"><g stroke="rgba(255,255,255,.05)">{grid}</g><path d="{M['land']}" fill="#3b2f27" stroke="#55453a"/>
<path class="route sea draw" d="{M['sea']}"/><path class="route sea draw" d="{M['seaS']}"/><path class="route sea draw" d="{M['feeder']}"/><path class="route sea draw" d="{M['feederS']}"/><path class="route air" d="{M['air']}"/>{roads}{ships}{cities}</svg></div>
<div class="legend"><span><i class="sea"></i>Sea freight</span><span><i class="air"></i>Air freight</span><span><i class="road"></i>Road delivery</span></div>'''

CN = [('phone_acc', 'Phones and electronics', 'Handsets, accessories and small electronics from Shenzhen and Guangzhou.', 'Shenzhen'),
      ('solar', 'Solar and power', 'Panels, inverters and batteries for homes, shops and farms.', 'Ningbo'),
      ('fabric_rolls', 'Textiles and garments', 'Fabric by the roll and finished clothing.', 'Guangzhou'),
      ('furniture', 'Furniture', 'Home and office furniture from Foshan.', 'Foshan'),
      ('engine', 'Auto parts', 'Engine parts, tyres and spares for the vehicles on East African roads.', 'Guangzhou'),
      ('steel', 'Building materials', 'Steel, tiles, fittings and fixtures for construction.', 'Tianjin'),
      ('ceramics_colour', 'Household goods', 'Kitchenware, ceramics and the small commodities Yiwu is known for.', 'Yiwu'),
      ('cn_line', 'Machinery', 'Equipment for workshops, small factories and processing.', 'Zhejiang')]
EA = [('coffee_harvest', 'Coffee', 'Ethiopian and Kenyan coffee for roasters and buyers in China.', 'Ethiopia'),
      ('sesame', 'Sesame', 'Sesame seed from Ethiopia, Somalia and Tanzania.', 'Somalia'),
      ('resin', 'Frankincense', 'Resin from the Somali highlands, graded and packed for export.', 'Somalia'),
      ('goats', 'Livestock and meat', 'Live animals and chilled meat through Berbera and Bosaso.', 'Somalia'),
      ('fruit_stall', 'Fresh produce', 'Fruit and vegetables for regional and Gulf markets.', 'Kenya'),
      ('green_coffee', 'Green beans', 'Unroasted coffee, inspected and documented before loading.', 'Tanzania')]

def bento(items, id, hidden=False):
    n = len(items); out = ''
    for i, (k, t, d, tag) in enumerate(items):
        c = (n - 5) % 4 if n > 5 else 0
        wide = (f' style="--sp:{4 - c + 1}"' if c else '') if i == n - 1 else ''
        out += f'<article class="clip"{wide}>{img(k, t, 1600 if i == 0 else 800, "(max-width:900px) 100vw, 50vw" if i == 0 else "(max-width:900px) 50vw, 25vw")}<span class="tag">{E(tag)}</span><div><h3>{E(t)}</h3><p>{E(d)}</p></div></article>'
    return f'<div class="bento" id="{id}" role="tabpanel"{" hidden" if hidden else ""}>{out}</div>'

STEPS = [('trader_phone', 'Tell us what you need', 'Send the product, quantity and port, or the details of a supplier you already use. A person who speaks your language picks it up.'),
         ('cn_wholesale', 'We source and quote', 'We find suppliers in Yiwu, Guangzhou and the factory towns around them, compare offers and send one quote with every cost shown.'),
         ('cn_factorywoman', 'We check the supplier', 'Business licence, factory and export history are checked before any money moves. Suppliers that fail are dropped.'),
         ('cn_inspector', 'Goods are inspected', 'Our inspector checks quantity, quality, packing and labels against your order and sends you the report with photos.'),
         ('ship_loading', 'We ship to your port', 'Sea, air or road. We book the freight, prepare the documents and track the shipment to Mogadishu, Mombasa, Dar es Salaam or Djibouti.'),
         ('handshake', 'Payment is settled', 'Payment goes through a partner bank with the invoice and inspection report attached, so every party sees the same record.')]

FAQ = [('Is Saweli a bank?', 'No. Saweli arranges trade and verification. Payments are processed by our partner banks, and Saweli does not take deposits.'),
       ('Can I use a supplier I already work with?', 'Yes. Send us the supplier details and we will verify the company and inspect your order in the same way.'),
       ('How do I know the goods are right before they ship?', 'We inspect the goods against your order before they leave and send you the report with photos. You decide whether the shipment goes.'),
       ('What does it cost?', 'It depends on the order value, the inspection and the freight. You see every fee in the quote before you confirm.'),
       ('What is the smallest order you take?', 'We handle full containers, shared containers and air parcels. Tell us what you need and we will suggest the cheapest way to move it.'),
       ('Which languages do you work in?', 'English, Somali, Swahili and Chinese.')]
def faq(items=FAQ):
    return '<div class="faq">' + ''.join(f'<details class="r"><summary>{E(q)}<i></i></summary><div class="ans"><p>{E(a)}</p></div></details>' for q, a in items) + '</div>'

MARKETS = [('mog_aerial', 'Mogadishu', 'Somalia', 'Port of Mogadishu, our first market'), ('nbo_skyline', 'Nairobi', 'Kenya', 'By road from Mombasa, or by air'), ('dar_skyline', 'Dar es Salaam', 'Tanzania', 'Port for Tanzania and the inland states'),
           ('add_street', 'Addis Ababa', 'Ethiopia', 'Through the port of Djibouti'), ('kla_skyline', 'Kampala', 'Uganda', 'By road from Mombasa'), ('dji_aerial', 'Djibouti', 'Djibouti', 'Gateway to Ethiopia'),
           ('cn_market', 'Yiwu', 'China', 'Small commodities and household goods'), ('nansha_view', 'Guangzhou', 'China', 'Textiles, auto parts and furniture'), ('shenzhen_sunset', 'Shenzhen', 'China', 'Electronics and phones'), ('shanghai_night', 'Shanghai and Ningbo', 'China', 'The main container ports')]
def rail(id='mk', link=True):
    out = ''.join(f'<{"a href=/corridors/#" + k if link else "figure"} class="r">{img(k, n, 800, "380px")}<small>{E(c)}</small><h3>{E(n)}</h3><small>{E(s)}</small></{"a" if link else "figure"}>' for k, n, c, s in MARKETS)
    return f'<div class="rail" id="{id}">{out}</div>'
def railnav(id):
    return f'<div class="railnav" data-rail="{id}"><button type="button" data-dir="-1" aria-label="Previous"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></button><button type="button" data-dir="1" aria-label="Next"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></div>'

def film_block(mode='play'):
    for k in ['containers_aerial', 'cn_market', 'cn_factorywoman', 'cn_inspector', 'ship_aerial', 'mog_port', 'hero_port']: src(k, 1600)
    data = {'label': 'How Saweli works, in five steps', 'land': M['land'], 'sea': M['sea'], 'seaS': M['seaS'], 'cities': M['cities'],
            'pins': [['Ningbo', 26, 'start'], ['Shanghai', -26, 'end'], ['Guangzhou', -26, 'end'], ['Djibouti', -26, 'end'], ['Mogadishu', 26, 'start'], ['Mombasa', 26, 'start']],
            'fields': [['Product', 'Solar panels, 450 W'], ['Quantity', '1,200 panels'], ['Deliver to', 'Port of Mogadishu']],
            'cost': ['Goods', 'Inspection', 'Freight', 'Saweli fee'], 'sup': [['Supplier A', 'Yiwu, Zhejiang'], ['Supplier B', 'Ningbo, Zhejiang'], ['Supplier C', 'Foshan, Guangdong']],
            'checks': ['Business licence', 'Factory visit', 'Export history'], 'ref': 'Order SW-0412', 'insp': ['Quantity', 'Quality', 'Packing', 'Labels and marks'],
            'docs': ['Bill of lading', 'Commercial invoice', 'Packing list', 'Inspection report'], 'payline': 'The invoice and inspection report travel with the payment.',
            'nodes': [['You', 'The buyer'], ['Partner bank', 'Checks the documents'], ['Supplier', 'Paid on the record']],
            'chap': ['Order', 'Verify', 'Inspect', 'Ship', 'Pay'], 'phone': PHONE,
            'zhStep': ['下单', '核实', '验货', '运输', '付款'], 'imgBase': '/img/', 'imgExt': '-1600.jpg', 'audio': '/media/film-audio.m4a',
            'bg': ['containers_aerial', 'cn_market', 'cn_factorywoman', 'cn_inspector', 'ship_aerial', 'mog_port', 'hero_port'], 'zhTitle': ['告诉我们您的需求', '我们核实供应商', '货物发运前先验货', '运抵您的港口', '通过合作银行付款']}
    if mode == 'scroll':
        return (f'<section class="scrollfilm" aria-label="How Saweli works, film"><div class="sticky"><div class="film" data-mode="scroll"><div class="ui"><div class="chap"></div><button class="snd" type="button" aria-pressed="false" aria-label="Sound"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 9h4l5-4v14l-5-4H4z"/><path class="w1" d="M16.5 8.5a5 5 0 0 1 0 7"/><path class="x" d="M17 9l5 6M22 9l-5 6"/></svg><span>Sound on</span></button></div>'
                f'<div class="hint"><span>Scroll to play</span><i></i></div></div></div></section><script type="application/json" id="film-data">{json.dumps(data)}</script>')
    return (f'<div class="film r"><div class="ui"><button class="pp" type="button" aria-label="Play"></button><div class="chap"></div><button class="snd" type="button" aria-pressed="false" aria-label="Sound"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 9h4l5-4v14l-5-4H4z"/><path class="w1" d="M16.5 8.5a5 5 0 0 1 0 7"/><path class="x" d="M17 9l5 6M22 9l-5 6"/></svg><span>Sound</span></button></div></div>'
            f'<script type="application/json" id="film-data">{json.dumps(data)}</script>')
FILMJS = '<script src="/assets/film.js?v=6" defer></script>'

# ------------------------------------------------------------------ pages
def home():
    slides = [('cn_market', 'Wholesale market, Yiwu'), ('hero_port', 'Container terminal, China'), ('ship_aerial', 'Indian Ocean crossing'), ('mog_sea', 'Mogadishu'), ('trader_phone', 'Market trader, Dar es Salaam')]
    sl = ''.join(f'<div class="slide{" on" if i == 0 else ""}" data-cap="{E(c)}">{img(k, c, 1600, lazy=i > 0)}</div>' for i, (k, c) in enumerate(slides))
    dots = ''.join(f'<button type="button" class="{"on" if i == 0 else ""}" aria-label="Photo {i+1}"><i></i></button>' for i in range(len(slides)))
    lanes = [('Yiwu', 'Mogadishu', 'Household goods'), ('Shenzhen', 'Nairobi', 'Phones, by air'), ('Ningbo', 'Mombasa', 'Solar panels'), ('Guangzhou', 'Dar es Salaam', 'Textiles'),
             ('Addis Ababa', 'Shanghai', 'Coffee'), ('Bosaso', 'Guangzhou', 'Frankincense'), ('Foshan', 'Djibouti', 'Furniture'), ('Mogadishu', 'Ningbo', 'Sesame')]
    tk = ''.join(f'<span><i></i><b>{a}</b> to <b>{b}</b> · {c}</span>' for a, b, c in lanes) * 2
    svc = [('cn_wholesale', 'Sourcing', 'We find and compare suppliers across China, then send one quote with every cost shown.', '/sourcing/'),
           ('cn_inspector', 'Inspection', 'Goods are checked against your order before they leave. You get the report and photos.', '/how-it-works/#inspection'),
           ('ship_aerial2', 'Logistics', 'Sea, air and road freight to the ports and cities of East Africa, with the paperwork done.', '/logistics/'),
           ('handshake', 'Payments', 'Payment is settled through partner banks with the documents attached to it.', '/banks/')]
    sv = ''.join(f'<a class="r d{i}" href="{h}">{img(k, t, 800, "(max-width:1000px) 50vw, 25vw")}<span class="n">0{i+1}</span><div><h3>{E(t)}</h3><p>{E(d)}</p><span class="go">{ARU}</span></div></a>' for i, (k, t, d, h) in enumerate(svc))
    jc = ''.join(f'<article class="jcard"><div class="ph">{img(k, t, 800, "520px")}</div><div class="tx"><div class="num">0{i+1}</div><h3>{E(t)}</h3><p>{E(d)}</p></div></article>' for i, (k, t, d) in enumerate(STEPS))
    mq1 = ''.join(f'<figure>{img(k, n, 800, "300px")}<figcaption>{E(n)}</figcaption></figure>' for k, n, _, _ in CN) * 2
    mq2 = ''.join(f'<figure>{img(k, n, 800, "300px")}<figcaption>{E(n)}</figcaption></figure>' for k, n, _, _ in EA + [('market_greens', 'Market produce', '', ''), ('coffee_sack', 'Coffee sacks', '', '')]) * 2
    body = f'''<section class="hero" aria-label="Saweli"><div class="slides">{sl}</div><div class="hin"><div class="wrap"><p class="zh-line r d1" lang="zh">两个市场的交汇处</p><h1 data-split=".1">Where two markets <em>meet</em></h1>
<div class="row"><div><p class="lede r d3">Buy from China and sell to China with every step checked: verified suppliers, goods inspected before they ship, freight to East African ports and payment through partner banks.</p>
<div class="ctas r d4"><a class="btn" href="/contact/">Start an order {AR}</a><a class="btn ghost" href="/how-it-works/">Watch how it works</a></div></div>
<div class="cap r d4"><span class="t">{E(slides[0][1])}</span><div class="dots">{dots}</div></div></div></div></div><div class="scroll-cue" aria-hidden="true"></div>
<div class="ticker" aria-hidden="true"><div class="tr">{tk}</div></div></section>
<section class="sec"><div class="wrap"><span class="kicker r">Why Saweli</span><p class="statement">East Africa buys phones, solar and building materials from China. China buys coffee, sesame and frankincense from East Africa. Most of that trade still runs on trust and a phone number. <em>We put a checked record behind every order.</em></p>
<div class="stats"><div class="r"><b data-count="5">0</b><span>Ports we ship to in East Africa</span></div><div class="r d1"><b data-count="4">0</b><span>Languages we work in</span></div><div class="r d2"><b data-count="6">0</b><span>Checks before your goods move</span></div><div class="r d3"><b data-count="1">0</b><span>Reference number for the whole order</span></div></div></div></section>
<section class="sec tight" style="padding-top:0"><div class="wrap"><div class="head"><div><span class="kicker r">What we do</span><h2 data-split>Four services, one order</h2></div><p class="lede mut r">Use one of them or all four. Each order carries one reference, and you can follow it from the first message to the bank receipt.</p></div><div class="svc">{sv}</div></div></section>
<section class="journey" style="--n:{len(STEPS)}"><div class="pin"><div class="wrap"><div class="jhead"><div><span class="kicker lt">The journey</span><h2>From a factory in China<br>to your shop</h2></div><div class="jprog"><i></i></div></div></div><div class="track">{jc}</div></div></section>
<section class="sec tight" style="padding-bottom:40px"><div class="wrap"><div class="head" style="margin-bottom:0"><div><span class="kicker r">Watch</span><h2 data-split>How Saweli works, in one scroll</h2></div><p class="lede mut r">Keep scrolling and the film plays. Turn the sound on to hear it explained.</p></div></div></section>{film_block('scroll')}
<section class="sec dark"><div class="wrap"><div class="head"><div><span class="kicker r">The corridor</span><h2 data-split>Routes we run</h2></div><p class="lede mut r">From the factories and wholesale markets of China to the ports and cities of East Africa. Sea freight for volume, air for speed and road delivery inland.</p></div>{mapsvg()}<p style="margin-top:34px"><a class="btn ghost" href="/corridors/">Explore the corridors {AR}</a></p></div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">What moves</span><h2 data-split>Goods in both directions</h2></div><p class="lede mut r">What East Africa buys from China, and what China buys from East Africa.</p></div>
<div class="tabs r" role="tablist"><button role="tab" aria-selected="true" aria-controls="p-cn">From China</button><button role="tab" aria-selected="false" aria-controls="p-ea">From East Africa</button></div>{bento(CN, 'p-cn')}{bento(EA, 'p-ea', True)}
<p style="margin-top:34px"><a class="link" href="/sourcing/">See everything we source {AR}</a></p></div></section>
<section class="sec tight sand" style="padding:40px 0"><div class="mq"><div class="tr">{mq1}</div></div><div class="mq rev"><div class="tr">{mq2}</div></div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">Markets</span><h2 data-split>Where we work</h2></div><div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><p class="lede mut r" style="margin:0">Somalia first, with Kenya, Tanzania, Ethiopia, Uganda and Djibouti on the same routes.</p>{railnav('mk')}</div></div></div>{rail('mk')}</section>
<section class="banks"><div class="bg" data-par=".1">{img('handshake', '', 1600)}</div><div class="wrap"><div class="box"><span class="kicker lt r">For banks</span><h2 data-split>Know what you are paying for</h2><p class="lede r" style="color:rgba(255,255,255,.85)">Banks in East Africa use Saweli to check the customer, the supplier and the documents behind a trade payment before it is released.</p><a class="btn lite r" href="/banks/">How it works for banks {AR}</a></div></div></section>
<section class="sec"><div class="wrap faqwrap"><div><span class="kicker r">Questions</span><h2 data-split>Good to know</h2><p class="lede mut r" style="margin-top:20px">Something else? Call us on <a class="link" href="tel:{TEL}">{PHONE}</a></p></div>{faq()}</div></section>
{cta_end()}'''
    return page('/', 'Saweli: trade between East Africa and China', 'Buy from China and sell to China with every step checked: verified suppliers, goods inspected before they ship, freight to East African ports and payment through partner banks.', body, '/', extra_js=FILMJS)

def how():
    det = [['Product, quantity and target price', 'The port or city you want it delivered to', 'An existing supplier, if you have one'],
           ['Offers from several suppliers compared', 'One quote: goods, inspection, freight and fees', 'Nothing is paid until you confirm'],
           ['Business licence and registration', 'Factory visit or video inspection', 'Export history and references'],
           ['Quantity and quality against your order', 'Packing, labels and marks', 'Report with photos, sent before loading'],
           ['Full container, shared container or air', 'Bill of lading, invoice and packing list', 'Tracking until arrival at port'],
           ['Payment through a partner bank', 'Documents attached to the payment', 'Delivery confirmed on the same reference']]
    li = ''.join(f'<li id="{["order","sourcing","verification","inspection","shipping","payment"][i]}"><div class="num">Step 0{i+1}</div><h3>{E(t)}</h3><p class="lede mut">{E(d)}</p><ul>' + ''.join(f'<li>{E(x)}</li>' for x in det[i]) + '</ul></li>' for i, (k, t, d) in enumerate(STEPS))
    ims = ''.join(img(k, t, 1600, "50vw", cls="on" if i == 0 else "") for i, (k, t, _) in enumerate(STEPS))
    body = f'''{phero('cn_inspector', 'How it works', 'One order, checked at <em>every step</em>', 'Every order carries one reference number. You, the supplier and the bank see the same record from the first message to the payment.', [('6', 'steps, one reference'), ('4', 'languages'), ('1', 'quote with every cost')])}
<section class="sec tight" style="padding-bottom:40px"><div class="wrap"><div class="head" style="margin-bottom:0"><div><span class="kicker r">The film</span><h2 data-split>Scroll through the whole process</h2></div><p class="lede mut r">Five chapters: order, verify, inspect, ship and pay. Turn the sound on to hear it explained. <a class="link" href="/media/saweli-how-it-works.mp4" download>Download the film {AR}</a></p></div></div></section>{film_block('scroll')}
<section class="sec white"><div class="wrap"><div class="head"><div><span class="kicker r">Step by step</span><h2 data-split>What happens to your order</h2></div><p class="lede mut r">Scroll through the six steps. The checks are the same whether you buy from China or sell to it.</p></div>
<div class="stepsx"><ol>{li}</ol><div><div class="stick"><span class="lbl">1 / 6</span>{ims}</div></div></div></div></section>
<section class="sec dark"><div class="wrap"><div class="head"><div><span class="kicker r">What you get</span><h2 data-split>Proof at every stage</h2></div><p class="lede mut r">Each step leaves a document behind. All of them sit under your order reference.</p></div>
<div class="cards">{"".join(f'<div class="card r d{i%3}"><div class="ico">{ic(c)}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i,(c,t,d) in enumerate([('doc','Quote','Goods, inspection, freight and fees, line by line.'),('shield','Supplier check','Licence, factory and export history, with the result.'),('eye','Inspection report','Quantity, quality and packing, with photos.'),('ship','Shipping documents','Bill of lading, commercial invoice and packing list.'),('bank','Bank record','The payment, with the documents it was released against.'),('clock','Order timeline','Every step, dated, under one reference.')]))}</div></div></section>
<section class="sec"><div class="wrap faqwrap"><div><span class="kicker r">Questions</span><h2 data-split>About the process</h2></div>{faq()}</div></section>
{cta_end()}'''
    return page('/how-it-works/', 'How Saweli works: order, verify, inspect, ship, pay', 'Six steps under one order reference: sourcing, supplier checks, inspection before shipping, freight to East African ports and payment through partner banks.', body, '/how-it-works/', extra_js=FILMJS)

def sourcing():
    body = f'''{phero('cn_wholesale', 'Sourcing', 'The right supplier, <em>checked</em> before you pay', 'We search the wholesale markets and factory towns of China, compare offers and check the supplier before any money moves. For exporters, we find buyers in China and prepare the goods for them.', [('Yiwu', 'small commodities'), ('Guangzhou', 'textiles and parts'), ('Shenzhen', 'electronics')])}
<section class="sec"><div class="wrap feat"><div class="media clip">{img('cn_market', 'Yiwu market', 1600, "(max-width:900px) 100vw, 50vw")}<div class="badge"><b>Yiwu International Trade City</b><span>Where many East African traders already buy</span></div></div>
<div><span class="kicker r">Buying from China</span><h2 data-split>We do the searching</h2><p class="lede mut r">Tell us what you need and the price you want to pay. We go to the markets and factories, ask for samples and come back with offers you can compare.</p>
<ul class="checks r"><li>Several offers for each product, side by side</li><li>Samples sent by air before a large order</li><li>Your existing supplier checked the same way</li><li>One quote with goods, inspection, freight and fees</li></ul><a class="btn r" href="/contact/?need=Sourcing%20from%20China">Ask for a quote {AR}</a></div></div></section>
<section class="sec sand"><div class="wrap"><div class="head"><div><span class="kicker r">From China</span><h2 data-split>What we source</h2></div><p class="lede mut r">The goods our buyers order most often. If it is made in China, ask us.</p></div>{bento(CN, 'c1')}</div></section>
<section class="sec"><div class="wrap feat rev"><div class="media clip">{img('coffee_harvest', 'Coffee harvest', 1600, "(max-width:900px) 100vw, 50vw")}<div class="badge"><b>Selling to China</b><span>Coffee, sesame, frankincense and more</span></div></div>
<div><span class="kicker r">Selling to China</span><h2 data-split>Your goods, in front of buyers in China</h2><p class="lede mut r">We match East African exporters with importers in China, check the buyer, inspect the goods before loading and see the documents through to the bank.</p>
<ul class="checks r"><li>Buyers checked before you ship</li><li>Grading and inspection at origin</li><li>Export documents prepared with you</li><li>Payment through a partner bank</li></ul><a class="btn r" href="/contact/?need=Selling%20to%20China">Talk to us about exports {AR}</a></div></div></section>
<section class="sec sand"><div class="wrap"><div class="head"><div><span class="kicker r">From East Africa</span><h2 data-split>What China buys</h2></div><p class="lede mut r">Goods from Somalia, Ethiopia, Kenya and Tanzania with steady demand in China.</p></div>{bento(EA, 'e1')}</div></section>
<section class="sec dark"><div class="wrap"><div class="head"><div><span class="kicker r">Supplier checks</span><h2 data-split>What we check before you pay</h2></div><p class="lede mut r">A supplier that fails any of these checks does not get your order.</p></div>
<div class="cards">{"".join(f'<div class="card r d{i%3}"><div class="ico">{ic(c)}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i,(c,t,d) in enumerate([('doc','Registration','Business licence, registered name and the person who signs.'),('pin','Factory','A visit or a live video walk through the production line.'),('globe','Export history','Past shipments abroad and the markets they went to.'),('users','References','Other buyers who have ordered from the same supplier.'),('box','Samples','Product samples checked against your specification.'),('shield','Bank details','The receiving account matches the registered company.')]))}</div></div></section>
{cta_end('Tell us what to <em>find</em>', 'Send a product name, a photo or a link. We come back with suppliers, samples and a quote.')}'''
    return page('/sourcing/', 'Sourcing from China and selling to China | Saweli', 'Verified suppliers in Yiwu, Guangzhou and Shenzhen, samples before you order, and buyers in China for East African coffee, sesame and frankincense.', body, '/sourcing/')

def logistics():
    modes = [('ship_aerial2', 'Sea freight', 'Full containers and shared loads from Ningbo, Shanghai, Shenzhen and Guangzhou to Mogadishu, Mombasa, Dar es Salaam and Djibouti.'),
             ('cargo_plane', 'Air freight', 'Samples, phones and urgent parts flown to Nairobi, Addis Ababa and Mogadishu.'),
             ('truck_road', 'Road delivery', 'Onward trucking from the port to Nairobi, Kampala and Addis Ababa.'),
             ('warehouse', 'Consolidation', 'Orders from several suppliers collected in China, checked and packed into one shipment.')]
    md = ''.join(f'<div class="mode{" on" if i == 0 else ""}" tabindex="0" aria-expanded="{"true" if i == 0 else "false"}">{img(k, n, 1600, "(max-width:820px) 100vw, 60vw")}<span class="lab">0{i+1}</span><div class="mtx"><h3>{E(n)}</h3><p>{E(d)}</p></div></div>' for i, (k, n, d) in enumerate(modes))
    ports = [('mog_port', 'Mogadishu', 'Somalia', 'Our first market. Sea freight from the main Chinese ports, cleared and delivered in the city.'),
             ('tz_containers', 'Mombasa', 'Kenya', 'The port for Kenya, Uganda and beyond, with road delivery to Nairobi and Kampala.'),
             ('dar_port', 'Dar es Salaam', 'Tanzania', 'Gateway for Tanzania and the inland states around it.'),
             ('djibouti_port', 'Djibouti', 'Djibouti', 'The sea route into Ethiopia, with road and rail to Addis Ababa.'),
             ('dji_boats', 'Bosaso', 'Somalia', 'Northern Somalia, and an export port for livestock and frankincense.'),
             ('hero_port', 'Ningbo and Shanghai', 'China', 'Where most of our sea freight from Zhejiang and Yiwu is loaded.')]
    pt = ''.join(f'<article class="port r d{i%3}"><div class="ph">{img(k, n, 800, "(max-width:620px) 100vw, 33vw")}</div><div class="tx"><div class="cty">{E(c)}</div><h3>{E(n)}</h3><p>{E(d)}</p></div></article>' for i, (k, n, c, d) in enumerate(ports))
    body = f'''{phero('ship_aerial', 'Logistics', 'From the factory gate to <em>your door</em>', 'We book the freight, prepare the documents and follow the goods until they reach you. Sea for volume, air for speed and road for the last miles.', [('Sea', 'FCL and shared loads'), ('Air', 'samples and urgent goods'), ('Road', 'inland delivery')])}
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">How we move it</span><h2 data-split>Freight that fits the order</h2></div><p class="lede mut r">Hover or tap to open each mode. We suggest the cheapest way that still meets your date.</p></div><div class="modes r">{md}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="head"><div><span class="kicker r">Routes</span><h2 data-split>The lanes we run</h2></div><p class="lede mut r">Sea routes across the Indian Ocean, air links to the capitals and roads inland from the ports.</p></div>{mapsvg()}</div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">Ports</span><h2 data-split>Where your goods arrive</h2></div><p class="lede mut r">We ship into five East African ports and deliver onward by road.</p></div><div class="ports">{pt}</div></div></section>
<section class="sec white"><div class="wrap feat"><div class="media clip">{img('warehouse_yellow', 'Warehouse', 1600, "(max-width:900px) 100vw, 50vw")}<div class="badge"><b>Consolidation in China</b><span>Several suppliers, one container</span></div></div>
<div><span class="kicker r">Paperwork</span><h2 data-split>Documents that travel with the goods</h2><p class="lede mut r">Customs delays usually start with missing papers. We prepare them with the supplier and check them before the ship leaves.</p>
<ul class="checks r"><li>Bill of lading or air waybill</li><li>Commercial invoice and packing list</li><li>Certificate of origin where it is needed</li><li>Inspection report attached to the order</li></ul><a class="btn r" href="/contact/?need=Freight%20quote">Get a freight quote {AR}</a></div></div></section>
{cta_end('Move your next <em>shipment</em>', 'Tell us what you are shipping, from where and to which port. We send a freight quote with the documents you will need.')}'''
    return page('/logistics/', 'Sea, air and road freight from China to East Africa | Saweli', 'Full and shared containers to Mogadishu, Mombasa, Dar es Salaam, Djibouti and Bosaso, air freight to the capitals and road delivery inland.', body, '/logistics/')

def corridors():
    cards = ''.join(f'<article class="port r d{i%3}" id="{k}"><div class="ph">{img(k, n, 800, "(max-width:620px) 100vw, 33vw")}</div><div class="tx"><div class="cty">{E(c)}</div><h3>{E(n)}</h3><p>{E(s)}</p></div></article>' for i, (k, n, c, s) in enumerate(MARKETS))
    body = f'''{phero('containers_aerial', 'Corridors', 'One ocean, <em>two markets</em>', 'The trade between China and East Africa runs across the Indian Ocean. These are the routes and cities we work in.', [('10', 'cities'), ('7', 'countries'), ('3', 'ways to move goods')])}
<section class="sec dark"><div class="wrap"><div class="head"><div><span class="kicker r">The map</span><h2 data-split>Routes between China and East Africa</h2></div><p class="lede mut r">Sea routes from the Chinese ports, an air link to the East African capitals and road delivery inland.</p></div>{mapsvg()}</div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">Cities</span><h2 data-split>Markets on the corridor</h2></div><p class="lede mut r">Six markets in East Africa and the four trading regions in China we buy from most.</p></div><div class="ports">{cards}</div></div></section>
<section class="sec sand"><div class="wrap center"><span class="kicker r">Coming next</span><h2 data-split>Somalia first, then Kenya</h2><p class="lede mut r" style="margin-top:20px">Saweli starts with trade into Somalia. Kenya and a presence in China come next. Tell us if you want us in your market sooner.</p><p class="r"><a class="btn" href="/contact/">Talk to us {AR}</a></p></div></section>
{cta_end()}'''
    return page('/corridors/', 'Trade corridors between China and East Africa | Saweli', 'Routes and markets: Mogadishu, Nairobi, Dar es Salaam, Addis Ababa, Kampala and Djibouti, linked to Yiwu, Guangzhou, Shenzhen, Shanghai and Ningbo.', body, '/corridors/')

def banks():
    body = f'''{phero('handshake', 'For banks', 'Know what you are <em>paying for</em>', 'Banks in East Africa use Saweli to check the customer, the supplier and the documents behind a trade payment before it is released.')}
<section class="sec"><div class="wrap"><div class="head"><div><span class="kicker r">The problem</span><h2 data-split>Trade payments with little behind them</h2></div><p class="lede mut r">A customer asks to pay a supplier in China. The invoice may be real, the supplier may exist, the goods may ship. Checking all of that from East Africa is slow and expensive.</p></div>
<div class="cards">{"".join(f'<div class="card r d{i%3}"><div class="ico">{ic(c)}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i,(c,t,d) in enumerate([('users','Customer checks','Know your customer and know your business checks on the importer or exporter.'),('shield','Supplier checks','The company in China is registered, real and matches the receiving account.'),('eye','Goods checks','An inspection report confirms the goods match the invoice before release.'),('doc','Document checks','Invoice, packing list and bill of lading checked against each other.'),('layers','One record','Every check sits under one reference you can audit later.'),('chat','Your workflow','Reports arrive in the format your trade finance team already uses.')]))}</div></div></section>
<section class="sec dark"><div class="wrap feat"><div class="media clip">{img('containers_aerial2', 'Containers', 1600, "(max-width:900px) 100vw, 50vw")}</div><div><span class="kicker r">How it fits</span><h2 data-split>We check, you decide</h2><p class="lede mut r">Saweli does not hold funds or take deposits. We give the bank the evidence it needs, and the bank decides whether to release the payment.</p>
<ul class="checks r"><li>The bank keeps the customer and the account</li><li>Saweli supplies the checks and the reports</li><li>Payment moves through the bank's own channels</li><li>Each payment is linked to an inspected shipment</li></ul><a class="btn r" href="/contact/?need=Bank%20partnership">Talk to us as a bank {AR}</a></div></div></section>
<section class="sec"><div class="wrap faqwrap"><div><span class="kicker r">For banks</span><h2 data-split>Common questions</h2></div>{faq([('Does Saweli hold customer money?', 'No. Payments go through the partner bank. Saweli does not take deposits or hold funds.'),('Which checks do you run?', 'Customer verification, supplier registration and factory checks, inspection of the goods and a cross-check of the trade documents.'),('Can we see a sample report?', 'Yes. Ask us and we will send a sample with the customer details removed.'),('Which countries do you cover?', 'Somalia first, then Kenya. Suppliers anywhere in mainland China.')])}</div></section>
{cta_end('Partner with <em>Saweli</em>', 'We are speaking with banks in Somalia and Kenya. Tell us about your trade finance desk and we will arrange a call.')}'''
    return page('/banks/', 'For banks: verified trade behind each payment | Saweli', 'Customer, supplier, goods and document checks for trade payments between East Africa and China. Saweli does not hold funds.', body, '/banks/')

def about():
    body = f'''{phero('mog_coast', 'About', 'Built for the people who <em>trade</em> on this route', 'Saweli started with a simple question from traders in Mogadishu: how do I know the supplier is real, the goods are right and my money is safe? Everything we do answers one part of that.')}
<section class="sec"><div class="wrap"><span class="kicker r">Our view</span><p class="statement">Trade between East Africa and China is growing every year, yet most orders still run on WhatsApp messages and trust. <em>We want every order on this route to be checked, documented and paid through a bank.</em></p></div></section>
<section class="sec white"><div class="wrap"><div class="head"><div><span class="kicker r">How we work</span><h2 data-split>What we hold ourselves to</h2></div></div>
<div class="cards">{"".join(f'<div class="card r d{i%3}"><div class="ico">{ic(c)}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i,(c,t,d) in enumerate([('eye','Show the cost','Every fee is in the quote before you confirm. No surprises at the port.'),('shield','Check first','No money moves to a supplier we have not checked.'),('chat','Speak your language','Somali, Swahili, English and Chinese, from the first message.'),('doc','Write it down','Every step leaves a document under your order reference.'),('bank','Banks hold the money','Payments go through partner banks. We do not take deposits.'),('users','Both sides matter','Exporters in East Africa get the same care as importers.')]))}</div></div></section>
<section class="sec"><div class="wrap feat"><div class="media clip">{img('cn_wholesale', 'Wholesale market', 1600, "(max-width:900px) 100vw, 50vw")}</div><div><span class="kicker r">Where we are going</span><h2 data-split>Somalia first, then Kenya and China</h2><p class="lede mut r">We start with trade into Somalia, where the need is greatest. Kenya and a presence in China come next, so that both ends of the route are covered by our own people.</p><a class="btn r" href="/contact/">Work with us {AR}</a></div></div></section>
{cta_end()}'''
    return page('/about/', 'About Saweli', 'Saweli puts a checked, documented record behind trade between East Africa and China, starting in Somalia.', body, '/about/')

def contact():
    roles = ['Buy from China', 'Sell to China', 'Check a supplier', 'Freight only', 'Bank partnership', 'Something else']
    chips = ''.join(f'<label><input type="radio" name="role" value="{E(r)}"{" checked" if i == 0 else ""}><span>{E(r)}</span></label>' for i, r in enumerate(roles))
    countries = ['Somalia', 'Kenya', 'Tanzania', 'Ethiopia', 'Uganda', 'Djibouti', 'China', 'Other']
    body = f'''<section class="sec dark" style="padding-top:170px"><div class="wrap formwrap"><div><div class="crumbs r"><a href="/">Home</a><span>/</span><span>Contact</span></div><h1 data-split style="font-size:clamp(46px,6.4vw,104px)">Start an <em style="color:var(--t)">order</em></h1>
<p class="lede mut r" style="margin-top:24px">Tell us what you want to buy or sell. A person who speaks your language replies within one working day.</p>
<ul class="contact-list r"><li><a href="tel:{TEL}"><span class="ic">{ic('phone')}</span><span><small>Call</small><b>{PHONE}</b></span></a></li><li><a href="{WA}" target="_blank" rel="noopener"><span class="ic">{ic('wa')}</span><span><small>WhatsApp</small><b>Message us</b></span></a></li><li><a href="mailto:{EMAIL}"><span class="ic">{ic('mail')}</span><span><small>Email</small><b>{EMAIL}</b></span></a></li></ul></div>
<form class="enq r d1" data-ok="Thank you. We will reply within one working day." data-err="That did not go through. Please call us or try again." novalidate>
<div class="full"><p style="margin:0 0 12px;font-weight:600">I want to</p><div class="chips">{chips}</div></div>
<div class="fld"><input id="f-n" name="name" required placeholder=" " autocomplete="name"><label for="f-n">Your name</label></div>
<div class="fld"><input id="f-c" name="company" placeholder=" " autocomplete="organization"><label for="f-c">Company</label></div>
<div class="fld"><input id="f-e" name="email" type="email" required placeholder=" " autocomplete="email"><label for="f-e">Email</label></div>
<div class="fld"><input id="f-p" name="phone" type="tel" placeholder=" " autocomplete="tel"><label for="f-p">Phone or WhatsApp</label></div>
<div class="fld full"><select id="f-co" name="country">{"".join(f'<option>{c}</option>' for c in countries)}</select><label for="f-co">Country</label></div>
<div class="fld full"><textarea id="f-m" name="message" required placeholder=" "></textarea><label for="f-m">What do you need? Product, quantity and port</label></div>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="lang" value="en">
<div class="full" style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap"><span class="note">We use your details only to answer you. <a class="link" href="/privacy/">Privacy</a></span><button class="btn" type="submit">Send enquiry {AR}</button></div>
<p class="form-msg" role="status"></p></form></div></section>
<section class="sec"><div class="wrap faqwrap"><div><span class="kicker r">Before you write</span><h2 data-split>Quick answers</h2></div>{faq()}</div></section>'''
    return page('/contact/', 'Contact Saweli: start an order', 'Call +252 614 264 999, message us on WhatsApp or send an enquiry. We reply within one working day.', body, '/contact/')

def privacy():
    body = f'''<section class="sec" style="padding-top:170px"><div class="wrap prose"><div class="crumbs r" style="color:var(--g)"><a href="/">Home</a><span>/</span><span>Privacy</span></div><h1 data-split style="font-size:clamp(44px,6vw,90px)">Privacy</h1>
<p class="lede mut r" style="margin-top:20px">This page explains what Saweli collects through this website and what we do with it.</p>
<h2>What we collect</h2><p>When you send an enquiry we receive the details you enter: your name, company, email, phone number, country and message. When you subscribe to trade notes we receive your email address.</p>
<h2>How we use it</h2><p>We use your details to answer your enquiry, prepare quotes and send the trade notes you asked for. We do not sell your details.</p>
<h2>Who sees it</h2><p>Our team, and partners such as inspectors, freight forwarders and partner banks when they need the details to handle your order.</p>
<h2>How long we keep it</h2><p>Enquiries are kept for as long as we need them to deal with your order and meet our legal duties. You can unsubscribe from trade notes at any time.</p>
<h2>Your choices</h2><p>To see, correct or delete your details, email <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>'''
    return page('/privacy/', 'Privacy | Saweli', 'How Saweli handles the details you send through this website.', body, '/privacy/', light=True)

def notfound():
    body = f'''<section class="err404"><div><h1 data-split>404</h1><p class="lede" style="color:rgba(255,255,255,.75);margin:18px auto 30px">This page has sailed. Try the home page or start an order.</p><div class="ctas" style="justify-content:center"><a class="btn" href="/">Home {AR}</a><a class="btn ghost" href="/contact/">Start an order</a></div></div></section>'''
    return page('/404', 'Page not found | Saweli', 'This page does not exist.', body)

def build():
    if os.path.exists(D): shutil.rmtree(D)
    os.makedirs(D + '/assets/fonts')
    pages = {'index.html': home(), 'how-it-works/index.html': how(), 'sourcing/index.html': sourcing(), 'logistics/index.html': logistics(),
             'corridors/index.html': corridors(), 'banks/index.html': banks(), 'about/index.html': about(), 'contact/index.html': contact(),
             'privacy/index.html': privacy(), '404.html': notfound()}
    for p, h in pages.items():
        os.makedirs(os.path.dirname(f'{D}/{p}') or D, exist_ok=True); open(f'{D}/{p}', 'w').write(h)
    for f in ('site.css', 'app.js', 'film.js'): shutil.copy(f'{SRC}/{f}', f'{D}/assets/{f}')
    os.makedirs(f'{D}/media', exist_ok=True); shutil.copy(f'{SRC}/film-audio.m4a', f'{D}/media/film-audio.m4a'); shutil.copy('/tmp/film/saweli-how-it-works.mp4', f'{D}/media/saweli-how-it-works.mp4')
    NM = '/home/claude/fontsrc/node_modules/'
    for a, b in [('@fontsource-variable/big-shoulders-display/files/big-shoulders-display-latin-wght-normal', 'bigshoulders'), ('@fontsource-variable/inter/files/inter-latin-wght-normal', 'inter')]:
        shutil.copy(f'{NM}{a}.woff2', f'{D}/assets/fonts/{b}.woff2')
    chars = set()
    for h in pages.values(): chars |= {c for c in h if ord(c) > 0x2e80}
    chars |= set('萨维利两个市场的交汇处下单核实验货运输付款告诉我们您需求供应商物发前先抵港口通过合作银行')
    css = ''
    for fam, pkg, wt in [('Noto Serif SC', 'noto-serif-sc', 300), ('Noto Sans SC', 'noto-sans-sc', 500)]:
        txt = open(f'{NM}@fontsource/{pkg}/{wt}.css').read()
        for blk in re.findall(r'@font-face \{.*?\}', txt, re.S):
            ur = re.search(r'unicode-range: ([^;]+);', blk).group(1); rng = []
            for part in ur.split(','):
                part = part.strip()[2:]; lo, _, hi = part.partition('-'); rng.append((int(lo, 16), int(hi or lo, 16)))
            if any(lo <= ord(c) <= hi for c in chars for lo, hi in rng):
                fn = re.search(r'files/([^)]+\.woff2)', blk).group(1)
                shutil.copy(f'{NM}@fontsource/{pkg}/files/{fn}', f'{D}/assets/fonts/{fn}')
                css += f"@font-face{{font-family:'{fam}';font-weight:{wt};font-display:swap;src:url(/assets/fonts/{fn}) format('woff2');unicode-range:{ur}}}\n"
    open(f'{D}/assets/fonts/zh.css', 'w').write(css)
    LP = '/home/claude/w/pack/Saweli-logo-pack/01-logo/'
    os.makedirs(f'{D}/brand', exist_ok=True)
    for a, b in [('horizontal/full/saweli-horizontal-full', 'saweli-colour'), ('horizontal/rev/saweli-horizontal-rev', 'saweli-white'), ('mark/full/saweli-mark-full', 'saweli-mark'), ('stacked/white/saweli-stacked-white', 'saweli-stacked-white'), ('stacked/rev/saweli-stacked-rev', 'saweli-stacked-rev')]:
        shutil.copy(f'{LP}{a}.svg', f'{D}/brand/{b}.svg')
    shutil.copy('/home/claude/site2/dist/favicon.svg', f'{D}/favicon.svg')
    urls = ['/', '/how-it-works/', '/sourcing/', '/logistics/', '/corridors/', '/banks/', '/about/', '/contact/', '/privacy/', '/zh/', '/so/', '/sw/']
    open(f'{D}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{SITE}{u}</loc></url>' for u in urls) + '</urlset>')
    open(f'{D}/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /admin/\nSitemap: {SITE}/sitemap.xml\n')
    open(f'{D}/_headers', 'w').write('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/img/*\n  Cache-Control: public, max-age=31536000, immutable\n')
    open(f'{D}/_redirects', 'w').write('/how /how-it-works/ 301\n/services/ /sourcing/ 301\n/markets/ /corridors/ 301\n/logistic/ /logistics/ 301\n')
    json.dump(USED, open(f'{D}/img.json', 'w'), indent=0)
    open(f'{D}/_worker.js', 'w').write(open(f'{SRC}/_worker.js').read().replace('__IMG__', json.dumps(USED)))
    print('pages', len(pages), 'images', len(USED))
if __name__ == '__main__': build()
