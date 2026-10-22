# Gera as publicações a partir de content/posts/*.md (arquivos criados pelo painel /admin)
import os, re, glob, datetime, unicodedata, html
import yaml, markdown

E = html.escape
MESES = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
MESES_CURTOS = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
DEFAULT_IMG = '/img/publicacoes/padrao.svg'
DEFAULT_ALT = 'Ilustração do escritório Quartieri & Maldonado.'
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect fill="none" height="17.5" rx="5.25" stroke="currentColor" stroke-width="1.9" width="17.5" x="3.25" y="3.25"/><circle cx="12" cy="12" fill="none" r="4.1" stroke="currentColor" stroke-width="1.9"/><circle cx="17.35" cy="6.65" fill="currentColor" r="1"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def slugify(t):
    t = unicodedata.normalize('NFD', str(t)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-') or 'publicacao'


def to_date(v):
    if isinstance(v, datetime.datetime): return v.date()
    if isinstance(v, datetime.date): return v
    s = str(v or '').strip()
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m: return datetime.date(int(m[1]), int(m[2]), int(m[3]))
    m = re.match(r'(\d{2})/(\d{2})/(\d{4})', s)
    if m: return datetime.date(int(m[3]), int(m[2]), int(m[1]))
    return datetime.date.today()


def load_posts(folder):
    posts = []
    for path in glob.glob(os.path.join(folder, '*.md')):
        raw = open(path, encoding='utf-8').read()
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', raw, re.S)
        if not m:
            print('Aviso: publicação sem cabeçalho ignorada:', path); continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            print('Aviso: cabeçalho inválido em', path, e); continue
        if meta.get('draft'): continue
        title = str(meta.get('title') or '').strip()
        if not title: continue
        cat = str(meta.get('category') or 'Artigos').strip()
        d = to_date(meta.get('date'))
        slug = os.path.splitext(os.path.basename(path))[0]
        body_html = markdown.markdown(m.group(2), extensions=['extra', 'sane_lists'], output_format='html')
        # links externos abrem em nova aba
        body_html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body_html)
        img = str(meta.get('image') or '').strip() or DEFAULT_IMG
        if not img.startswith(('/', 'http')): img = '/' + img
        pdf = str(meta.get('pdf') or '').strip()
        if pdf and not pdf.startswith(('/', 'http')): pdf = '/' + pdf
        if not body_html.strip() and not pdf:
            print('Aviso: publicação sem texto e sem PDF ignorada:', path); continue
        posts.append({
            'pdf': pdf,
            'title': title, 'category': cat, 'cat_slug': slugify(cat), 'slug': slugify(slug),
            'date': d, 'summary': str(meta.get('summary') or '').strip(),
            'image': img, 'image_alt': str(meta.get('image_alt') or '').strip() or (DEFAULT_ALT if img == DEFAULT_IMG else title),
            'body': body_html,
        })
    posts.sort(key=lambda p: (p['date'], p['title']), reverse=True)
    for p in posts:
        p['url'] = f"posts/{p['cat_slug']}/{p['slug']}.html"
        p['date_long'] = f"{p['date'].day} de {MESES[p['date'].month-1]} de {p['date'].year}"
        p['date_short'] = f"{p['date'].day:02d} {MESES_CURTOS[p['date'].month-1]} {p['date'].year}"
    return posts


PDF_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5"/><path d="M5 19h14"/></svg>'


def pdf_block(p):
    if not p.get('pdf'): return ''
    intro = '' if p['body'].strip() else '<p>O conteúdo completo desta publicação está disponível em PDF.</p>'
    return f'''{intro}<p style="margin-top:36px"><a class="btn btn-solid" style="color:#fff;text-decoration:none" href="{E(p['pdf'])}" target="_blank" rel="noopener" download>{PDF_ICON}Baixar PDF</a></p>'''


def img_attrs(p):
    return f'src="{E(p["image"])}" alt="{E(p["image_alt"])}"'


def feature_card(p, prefix=''):
    return f'''<a class="feature" href="{prefix}{p['url']}">
        <div class="feature__img"><img {img_attrs(p)} width="1200" height="900" loading="lazy"></div>
        <div class="feature__body">
          <div class="feature__meta"><span class="post__tag">{E(p['category'])}</span><time datetime="{p['date'].isoformat()}">{p['date_long']}</time></div>
          <h3>{E(p['title'])}</h3>
          <p>{E(p['summary'])}</p>
          <span class="feature__cta">Ler publicação<span class="feature__arrow" aria-hidden="true">{ARROW}</span></span>
        </div>
      </a>'''


def small_card(p, prefix=''):
    return f'''<a class="pcard" href="{prefix}{p['url']}">
        <div class="pcard__img"><img {img_attrs(p)} width="1200" height="900" loading="lazy"></div>
        <div class="pcard__body">
          <div class="feature__meta"><span class="post__tag">{E(p['category'])}</span><time datetime="{p['date'].isoformat()}">{p['date_long']}</time></div>
          <h3>{E(p['title'])}</h3>
          <p>{E(p['summary'])}</p>
        </div>
      </a>'''


INSTA = f'''<aside class="insta">
        <span class="insta__icon">{IG}</span>
        <h3>Acompanhe no Instagram</h3>
        <p>Conteúdos jurídicos e novidades do escritório também são publicados no perfil oficial.</p>
        <span class="insta__handle">@quartieriemaldonadoadv</span>
        <a class="btn btn-light" href="https://www.instagram.com/quartieriemaldonadoadv/" target="_blank" rel="noopener">Seguir no Instagram</a>
      </aside>'''


def home_block(posts):
    if not posts:
        return f'<div class="posts__grid posts__grid--empty">{INSTA}</div>'
    out = f'''<div class="posts__grid">
      {feature_card(posts[0])}
      {INSTA}
    </div>'''
    rest = posts[1:4]
    if rest:
        out += '\n    <div class="posts__more-grid">' + ''.join(small_card(p) for p in rest) + '</div>'
    if len(posts) > 1:
        out += '\n    <div class="posts__all"><a class="btn btn-line" href="publicacoes/">Ver todas as publicações</a></div>'
    return out


def build(g, OUT, content_dir):
    head, header, footer, WA_DEFAULT = g['head'], g['header'], g['footer'], g['WA_DEFAULT']
    T = ' | Quartieri & Maldonado Advogados Associados'
    posts = load_posts(content_dir)

    # Página de cada publicação
    for p in posts:
        r = '../../'
        main = f'''<main>
<section class="phero">
  <div class="wrap">
    <div>
      <nav class="crumb" aria-label="Você está em"><a href="{r}index.html">Início</a><span aria-hidden="true">/</span><a href="{r}publicacoes/">Publicações</a><span aria-hidden="true">/</span><span aria-current="page">{E(p['category'])}</span></nav>
      <h1 class="display">{E(p['title'])}</h1>
      <p class="phero__lede">{E(p['summary'])}</p>
      <div class="meta"><span class="post__tag">{E(p['category'])}</span><time datetime="{p['date'].isoformat()}">{p['date_long']}</time></div>
    </div>
    <div class="phero__art"><div class="arch"><img {img_attrs(p)} width="1200" height="900"></div></div>
  </div>
</section>
<article class="article">
  <div class="wrap">
    {p['body']}
    {pdf_block(p)}
    <a class="article__back" href="{r}publicacoes/">Voltar para publicações</a>
  </div>
</article>
'''
        canon = f"/posts/{p['cat_slug']}/{p['slug']}"
        doc = head(r, p['title'] + T, p['summary'] or p['title'], canon) + header(r, WA_DEFAULT) + main + '</main>\n' + footer(r, WA_DEFAULT)
        dest = os.path.join(OUT, p['url'])
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, 'w', encoding='utf-8').write(doc)

    # Página com todas as publicações
    r = '../'
    cards = ''.join(small_card(p, r) for p in posts) or '<p class="posts__empty">Em breve, novas publicações.</p>'
    main = f'''<main>
<section class="legal-hero">
  <div class="wrap" style="max-width:var(--max)">
    <nav class="crumb" aria-label="Você está em"><a href="{r}index.html">Início</a><span aria-hidden="true">/</span><span aria-current="page">Publicações</span></nav>
    <h1 class="display">Publicações</h1>
    <p>Publicações do escritório sobre temas jurídicos, atualizações relevantes e posicionamento profissional.</p>
  </div>
</section>
<section class="sec posts posts--index">
  <div class="wrap">
    <div class="posts__more-grid">{cards}</div>
  </div>
</section>
</main>
'''
    os.makedirs(os.path.join(OUT, 'publicacoes'), exist_ok=True)
    open(os.path.join(OUT, 'publicacoes', 'index.html'), 'w', encoding='utf-8').write(
        head(r, 'Publicações' + T, 'Publicações do escritório Quartieri & Maldonado sobre temas jurídicos e institucionais.', '/publicacoes/') + header(r, WA_DEFAULT) + main + footer(r, WA_DEFAULT))

    # Página inicial: troca o bloco de publicações
    idx = os.path.join(OUT, 'index.html')
    s = open(idx, encoding='utf-8').read()
    s = re.sub(r'<!-- PUBLICACOES -->.*?<!-- /PUBLICACOES -->', lambda _: '<!-- PUBLICACOES -->\n    ' + home_block(posts) + '\n    <!-- /PUBLICACOES -->', s, flags=re.S)
    open(idx, 'w', encoding='utf-8').write(s)
    return posts
