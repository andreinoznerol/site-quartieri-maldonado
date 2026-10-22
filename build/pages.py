# Gera as páginas internas do site Quartieri & Maldonado a partir do conteúdo do site atual.
import html, urllib.parse, os
import sys
OUT = os.environ.get('SITE_OUT','dist')
HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape

WA = 'https://wa.me/5555997350808?text='
def wa(msg): return WA + urllib.parse.quote(msg)
WA_DEFAULT = wa('Olá! Vim pelo site e gostaria de agendar um atendimento.')

ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12.5 2.7 2.7L16.5 9.5"/></svg>'
ICON_WARN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4.5 6v6c0 4.6 3.2 8 7.5 9 4.3-1 7.5-4.4 7.5-9V6L12 3Z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35M12.05 21.79h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.9-9.88a9.83 9.83 0 0 1 6.99 2.9 9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.89 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.9c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.9 0-3.18-1.24-6.17-3.48-8.41"/></svg>'
SOC = {
 'Instagram':('https://www.instagram.com/quartieriemaldonadoadv/','<svg viewBox="0 0 24 24" aria-hidden="true"><rect fill="none" height="17.5" rx="5.25" stroke="currentColor" stroke-width="1.9" width="17.5" x="3.25" y="3.25"/><circle cx="12" cy="12" fill="none" r="4.1" stroke="currentColor" stroke-width="1.9"/><circle cx="17.35" cy="6.65" fill="currentColor" r="1"/></svg>'),
 'Facebook':('https://www.facebook.com/profile.php?id=61575399580595','<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.55 20.5v-7h2.36l.35-2.76h-2.71V9c0-.8.23-1.35 1.38-1.35h1.48V5.2c-.26-.04-1.13-.11-2.14-.11-2.12 0-3.57 1.29-3.57 3.66v2.01H8.5v2.76h2.2v7h2.85Z" fill="currentColor"/></svg>'),
 'LinkedIn':('https://www.linkedin.com/company/quartierimaldonado','<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.76 8.33a1.63 1.63 0 1 1 0-3.26 1.63 1.63 0 0 1 0 3.26ZM5.3 9.82h2.93v8.88H5.3V9.82Zm4.78 0h2.81v1.21h.04c.39-.74 1.35-1.52 2.77-1.52 2.96 0 3.5 1.95 3.5 4.48v4.71h-2.93v-4.18c0-1-.02-2.28-1.39-2.28-1.39 0-1.6 1.08-1.6 2.21v4.25h-2.9V9.82Z" fill="currentColor"/></svg>'),
}
Q_DECOR = '<svg class="q" viewBox="0 0 600 600" aria-hidden="true"><path d="M98.5 501.5 A285 285 0 1 1 442.5 546.8 L497 604" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>'

PEOPLE = {
 'matheus':('Matheus Quartieri Simões Pires','Núcleo Penal, Penal Militar e Administrativo Sancionador','img/matheus-quartieri.jpg'),
 'jackson':('Jackson Maldonado','Núcleo Cível, Direito Público e Direito do Trabalho','img/jackson-maldonado.jpg'),
}

def head(r, title, desc, canon):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#ffffff">
<link rel="canonical" href="https://quartierimaldonado.com{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="https://quartierimaldonado.com/img/og.jpg">
<link rel="icon" href="{r}img/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/site.css">
</head>
<body>
'''

def header(r, wa_link):
    h = r + 'index.html'
    links = [('Início',h+'#inicio'),('Áreas de atuação',h+'#areas'),('Publicações',h+'#publicacoes'),('Sobre nós',h+'#escritorio'),('Contato',h+'#contato')]
    nav = '\n      '.join(f'<a href="{u}">{t}</a>' for t,u in links)
    drawer = '\n  '.join(f'<a class="link" href="{u}">{t}</a>' for t,u in links)
    return f'''<header class="header">
  <div class="wrap">
    <a class="brand" href="{h}" aria-label="Quartieri &amp; Maldonado Advogados Associados, voltar ao início">
      <img src="{r}img/logo-mark.svg" alt="" width="59" height="38">
      <span><b>Quartieri &amp; Maldonado</b><small>Advogados Associados</small></span>
    </a>
    <nav class="nav" aria-label="Menu principal">
      {nav}
    </nav>
    <a class="btn btn-solid" href="{wa_link}" target="_blank" rel="noopener">Entre em contato</a>
    <button class="menu-btn" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>

<nav class="drawer" id="menu" aria-label="Menu">
  {drawer}
  <a class="btn btn-solid" href="{wa_link}" target="_blank" rel="noopener">Entre em contato</a>
</nav>
'''

def footer(r, wa_link):
    h = r + 'index.html'
    soc = ''.join(f'<a class="social" href="{u}" target="_blank" rel="noopener" aria-label="{n}">{svg}</a>' for n,(u,svg) in SOC.items())
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand" href="{h}"><img src="{r}img/logo-mark-light.svg" alt="" width="59" height="38"><span><b>Quartieri &amp; Maldonado</b><small>Advogados Associados</small></span></a>
        <p class="footer__about"><b>Integridade, excelência e compromisso.</b> Construímos soluções jurídicas com excelência e responsabilidade.</p>
      </div>
      <div>
        <h4>Navegação</h4>
        <ul>
          <li><a href="{h}#inicio">Início</a></li>
          <li><a href="{h}#areas">Áreas de atuação</a></li>
          <li><a href="{h}#publicacoes">Publicações</a></li>
          <li><a href="{h}#escritorio">Sobre o escritório</a></li>
          <li><a href="{h}#contato">Contato</a></li>
        </ul>
      </div>
      <div>
        <h4>Redes sociais</h4>
        <div class="socials">{soc}</div>
        <p class="footer__contact">(55) 99735-0808</p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span id="ano">2026</span> Quartieri &amp; Maldonado Advogados Associados. Todos os direitos reservados.</span>
      <span class="footer__legal"><a href="{r}politica-de-privacidade.html">Privacidade</a><a href="{r}termos-de-uso.html">Termos de uso</a><span>Desenvolvido por André Lorenzoni</span></span>
    </div>
  </div>
</footer>

<a class="wa" href="{wa_link}" target="_blank" rel="noopener" aria-label="Entre em contato pelo WhatsApp">{ICON_WA}</a>

<script>
(function(){{
  var header=document.querySelector('.header'), wa=document.querySelector('.wa');
  function onScroll(){{header.classList.toggle('scrolled',scrollY>10);wa.classList.toggle('show',scrollY>innerHeight*.7)}}
  onScroll();addEventListener('scroll',onScroll,{{passive:true}});
  var btn=document.querySelector('.menu-btn');
  function menu(open){{document.body.classList.toggle('menu-open',open);btn.setAttribute('aria-expanded',open);btn.setAttribute('aria-label',open?'Fechar menu':'Abrir menu');document.body.style.overflow=open?'hidden':''}}
  btn.addEventListener('click',function(){{menu(!document.body.classList.contains('menu-open'))}});
  document.querySelectorAll('.drawer a').forEach(function(a){{a.addEventListener('click',function(){{menu(false)}})}});
  addEventListener('keydown',function(e){{if(e.key==='Escape')menu(false)}});
  document.getElementById('ano').textContent=new Date().getFullYear();
}})();
</script>
</body>
</html>
'''

# ---------- blocos ----------
def b_statement(title, text, variant='', link=None):
    more = f'<a class="statement__more" href="{link[0]}">{E(link[1])}</a>' if link else ''
    return f'''<section class="statement {variant}">
  <div class="wrap">
    <h2 class="display">{E(title)}</h2>
    <div><p>{E(text)}</p>{more}</div>
  </div>
</section>
'''

def _head(title, desc):
    d = f'<p>{E(desc)}</p>' if desc else ''
    return f'<div class="block__head"><h2 class="display">{E(title)}</h2>{d}</div>'

def b_checks(title, desc, items, tint=False, warn=False):
    ic = ICON_WARN if warn else ICON_CHECK
    lis = ''.join(f'<li>{ic}<span>{E(i)}</span></li>' for i in items)
    return f'''<section class="block{' tint' if tint else ''}">
  <div class="wrap">
    {_head(title, desc)}
    <ul class="checks{' warn' if warn else ''}">{lis}</ul>
  </div>
</section>
'''

def b_details(title, desc, items, tint=False):
    cols = ' two' if len(items) in (2, 4) else ''
    out = []
    for it in items:
        more = f'<a class="more" href="{it["href"]}">{E(it.get("more","Saiba mais"))}</a>' if it.get('href') else ''
        p = f'<p>{E(it["p"])}</p>' if it.get('p') else ''
        out.append(f'<article class="detail"><h3>{E(it["t"])}</h3>{p}{more}</article>')
    return f'''<section class="block{' tint' if tint else ''}">
  <div class="wrap">
    {_head(title, desc)}
    <div class="details{cols}">{''.join(out)}</div>
  </div>
</section>
'''

def b_band(title, desc, items):
    def tile(i):
        if not isinstance(i, dict): i = {'t': i}
        p = f'<p>{E(i["p"])}</p>' if i.get('p') else ''
        more = f'<a class="tile__more" href="{i["href"]}">{E(i.get("more","Saiba mais"))}</a>' if i.get('href') else ''
        return f'<div class="tile">{ICON_SHIELD}<h3>{E(i["t"])}</h3>{p}{more}</div>'
    tiles = ''.join(tile(i) for i in items)
    return f'''<section class="band">
  <div class="wrap">
    {_head(title, desc)}
    <div class="tiles">{tiles}</div>
  </div>
</section>
'''

def b_faq(title, desc, qas):
    d = f'<p class="faq__intro">{E(desc)}</p>' if desc else ''
    items = ''.join(f'<details><summary>{E(q)}<i aria-hidden="true"></i></summary><p>{E(a)}</p></details>' for q,a in qas)
    return f'''<section class="faq" id="duvidas">
  <div class="wrap">
    <div><h2 class="display">{E(title)}</h2>{d}</div>
    <div class="qa">{items}</div>
  </div>
</section>
'''

def b_cta(title, text, btn, link):
    return f'''<section class="cta">
  {Q_DECOR}
  <div class="wrap">
    <h2 class="display">{E(title)}</h2>
    <p>{E(text)}</p>
    <a class="btn btn-light" href="{link}" target="_blank" rel="noopener">{ICON_WA}{E(btn)}</a>
  </div>
</section>
'''

AREAS = [
 ('penal','Defesa Criminal','Direito Criminal'),
 ('militar','Direito Militar','Direito Penal Militar'),
 ('mensalista-funcional','Assistência funcional','Policiais e bombeiros militares'),
 ('direito-publico','Direito Público','Servidores, candidatos e militares'),
 ('trabalhista','Direito Trabalhista','Trabalhadores e empresas'),
]
def b_related(r, current):
    links = ''.join(f'<a href="{r}areas/{slug}/index.html">{E(name)}<span>{E(sub)}</span></a>' for slug,name,sub in AREAS if slug != current)
    return f'''<section class="related">
  <div class="wrap">
    <h2 class="display" style="font-size:clamp(1.6rem,2.6vw,2.1rem)">Outras áreas de atuação</h2>
    <div class="related__list">{links}</div>
  </div>
</section>
'''

def page_area(slug, meta_title, meta_desc, crumb, h1, lede, cta_btn, art, art_alt, owner, blocks, wa_msg, parent=None):
    r = '../../'
    link = wa(wa_msg)
    own = ''
    if owner:
        n, role, img = PEOPLE[owner]
        own = f'<div class="owner"><img src="{r}{img}" alt="" width="44" height="44"><p><b>{E(n)}</b>{E(role)}</p></div>'
    faq_btn = '<a class="btn btn-line" href="#duvidas">Ver dúvidas frequentes</a>' if any(('id="duvidas"' in (b if isinstance(b,str) else '')) for b in blocks) else ''
    parent_crumb = f'<a href="index.html">{E(parent[1])}</a><span aria-hidden="true">/</span>' if parent else ''
    hero = f'''<main>
<section class="phero">
  <div class="wrap">
    <div>
      <nav class="crumb" aria-label="Você está em"><a href="{r}index.html">Início</a><span aria-hidden="true">/</span><a href="{r}index.html#areas">Áreas de atuação</a><span aria-hidden="true">/</span>{parent_crumb}<span aria-current="page">{E(crumb)}</span></nav>
      <h1 class="display">{E(h1)}</h1>
      <p class="phero__lede">{E(lede)}</p>
      <div class="hero__ctas">
        <a class="btn btn-solid" href="{link}" target="_blank" rel="noopener">{E(cta_btn)}</a>
        {faq_btn}
      </div>
      {own}
    </div>
    <div class="phero__art"><div class="arch"><img src="{r}img/areas/{art}.svg" alt="{E(art_alt)}" width="400" height="500"></div></div>
  </div>
</section>
'''
    parts = [b(link) if callable(b) else b for b in blocks]
    # alterna fundo branco / gelo entre seções claras vizinhas
    import re as _re
    prev = 'white'
    for i, part in enumerate(parts):
        m = _re.match(r'<section class="(statement|block|faq|band|cta)([^"]*)"', part)
        kind = m.group(1)
        if kind in ('band', 'cta'):
            prev = 'dark'; continue
        classes = [c for c in m.group(2).split() if c != 'tint']
        want_tint = prev == 'white'
        if want_tint: classes.append('tint')
        prev = 'tint' if want_tint else 'white'
        parts[i] = part.replace(m.group(0), '<section class="' + ' '.join([kind] + classes) + '"', 1)
    body = ''.join(parts)
    if parent:
        canon, path, cur = f'/areas/{parent[0]}/{slug}', f'{OUT}/areas/{parent[0]}/{slug}.html', parent[0]
    else:
        canon, path, cur = f'/areas/{slug}/', f'{OUT}/areas/{slug}/index.html', slug
    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc = head(r, meta_title, meta_desc, canon) + header(r, link) + hero + body + b_related(r, cur) + '</main>\n' + footer(r, link)
    open(path, 'w', encoding='utf-8').write(doc)

# ======================= DEFESA CRIMINAL =======================
page_area('penal',
 'Defesa Criminal | Quartieri & Maldonado Advogados Associados',
 'Foi intimado para depor na polícia ou citado em processo criminal? Avalie a situação juridicamente antes de qualquer manifestação.',
 'Defesa Criminal',
 'Foi intimado para depor na polícia ou citado em processo criminal?',
 'A forma como você se posiciona no início pode influenciar todo o caso. Antes de qualquer manifestação, é necessário avaliar a investigação, a acusação e os riscos processuais.',
 'Solicitar orientação jurídica', 'penal', 'Ilustração de uma balança da justiça.', 'matheus', [
 b_statement('Receber uma intimação ou citação criminal gera dúvidas e insegurança', 'Nessas situações, a pessoa pode não saber se deve falar ou permanecer em silêncio, desconhecer o conteúdo da investigação, acreditar que não tem nada a esconder e comparecer sem orientação, ou subestimar o impacto de suas declarações. No âmbito criminal, cada palavra pode ter consequência jurídica relevante.', 'tint'),
 b_band('Interrogatório na polícia: seus direitos fundamentais', 'Ao ser intimado para depor, você possui direitos que devem ser respeitados.', ['Direito ao silêncio','Direito de não produzir prova contra si','Direito de ser assistido por advogado']),
 b_checks('Declarações prestadas sem orientação podem:', '', ['Ser interpretadas de forma desfavorável','Gerar contradições','Comprometer a estratégia de defesa futura'], warn=True),
 b_statement('Citação em processo criminal: atenção ao prazo', 'Ao receber uma citação criminal, inicia-se formalmente o prazo para apresentação de defesa. Já existe uma acusação estruturada, há prazo legal para resposta e a ausência de manifestação pode gerar prejuízos processuais relevantes. A resposta à acusação é uma peça técnica fundamental, onde podem ser analisados nulidades do processo, ausência de provas, inconsistências na acusação e possibilidades de absolvição.', 'tint'),
 b_checks('Por que a atuação jurídica desde o início é importante', 'No processo penal, o início é determinante. Uma condução técnica adequada desde os primeiros atos permite:', ['Evitar autoincriminação','Definir estratégia de defesa','Identificar falhas na investigação','Preservar direitos fundamentais','Reduzir riscos ao longo do processo']),
 b_checks('Erros comuns que dificultam a defesa', 'Muitos prejuízos decorrem de decisões tomadas sem orientação.', ['Comparecer à delegacia sem advogado','Prestar declarações sem conhecer o conteúdo da investigação','Ignorar prazos processuais','Acreditar que a situação se resolve sozinha'], tint=True, warn=True),
 b_checks('O que pode ser feito em cada situação', 'A atuação jurídica pode envolver, conforme o caso:', ['Análise prévia da intimação ou citação','Acompanhamento em interrogatório policial','Acesso aos autos da investigação','Elaboração de resposta à acusação','Definição de estratégia defensiva']),
 b_details('Exemplos de serviços prestados', 'Situações concretas em que o escritório pode atuar na área criminal.', [
   {'t':'Defesa no processo penal','p':'Atuação técnica em ações penais desde a fase de investigação até o trânsito em julgado.'},
   {'t':'Defesa perante o Tribunal do Júri','p':'Representação e estratégia de defesa nos processos de competência do Júri Popular.'},
   {'t':'Acompanhamento na execução da pena','p':'Atuação nas fases de execução penal, incluindo progressão de regime e benefícios legais.'},
   {'t':'Retirada de antecedentes criminais','p':'Análise e medidas para retirada ou restrição de registros como inquéritos arquivados e absolvições.','href':'retirada-antecedentes.html','more':'Ver a página sobre antecedentes'}], tint=True),
 b_faq('Dúvidas frequentes', '', [
   ('Sou obrigado a responder tudo na delegacia?','Não. Você possui o direito ao silêncio e à assistência por advogado.'),
   ('Posso ir sozinho para prestar depoimento?','Pode, mas não é recomendável diante dos riscos envolvidos.'),
   ('Recebi uma citação. O que devo fazer?','É necessário apresentar defesa dentro do prazo legal.'),
   ('Se eu não fizer nada, o que acontece?','A ausência de defesa pode gerar prejuízos processuais relevantes.')]),
 b_statement('A atuação preventiva é tão relevante quanto a defesa em juízo', 'Se você foi intimado para depor ou citado em processo criminal, é recomendável compreender previamente seus direitos e as implicações jurídicas do caso antes de tomar qualquer decisão.', 'quiet'),
 lambda link: b_cta('Converse com o escritório antes de tomar qualquer decisão sensível', 'Um primeiro contato permite organizar o cenário, identificar urgências e definir a resposta técnica cabível.', 'Solicitar orientação jurídica', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre Defesa Criminal.')

# ======================= DIREITO MILITAR =======================
page_area('militar',
 'Direito Militar | Quartieri & Maldonado Advogados Associados',
 'Defesa técnica em IPM, sindicância, processo administrativo disciplinar militar e ação penal militar antes de qualquer manifestação formal.',
 'Direito Militar',
 'Foi intimado em Inquérito Policial Militar, sindicância ou citado na Justiça Militar?',
 'A forma como você se defende desde o início pode impactar diretamente sua carreira e sua liberdade. Procedimentos administrativos e criminais militares exigem orientação técnica antes de qualquer manifestação.',
 'Solicitar orientação jurídica', 'militar', 'Ilustração de um escudo com estrela militar.', 'matheus', [
 b_statement('A atividade militar exige decisões rápidas, a investigação também', 'Quando surge uma investigação, seja um IPM, sindicância ou processo administrativo, o militar pode não ter acesso imediato a todas as informações, ser chamado a prestar depoimento sem conhecer o conteúdo integral dos autos, subestimar o impacto jurídico da sua manifestação ou acreditar que o procedimento é apenas administrativo. Esses procedimentos podem evoluir para consequências relevantes na esfera disciplinar e penal.', 'tint'),
 b_checks('Situações que exigem atenção imediata', 'A atuação jurídica é especialmente relevante quando o militar é:', ['Intimado para depor em Inquérito Policial Militar (IPM)','Notificado em sindicância investigatória','Acusado em Processo Administrativo Disciplinar Militar (PADM)','Citado para responder a ação penal militar']),
 b_band('Direitos fundamentais no depoimento', 'O depoimento é um dos momentos mais sensíveis da investigação. A versão dos fatos passa a integrar formalmente o processo e eventuais contradições podem ser utilizadas posteriormente. O militar possui direitos que devem ser respeitados:', ['Direito ao silêncio','Direito de não produzir prova contra si','Direito de ser assistido por advogado']),
 b_statement('Processo Administrativo Disciplinar Militar (PADM)', 'O PADM tem como objetivo apurar eventual transgressão disciplinar e pode resultar em advertência, detenção disciplinar, licenciamento ou exclusão, além de repercussões na carreira e na antiguidade. A defesa técnica permite análise da legalidade do procedimento, verificação de nulidades, produção adequada de provas e atuação na dosimetria da sanção.'),
 b_statement('Ação penal militar: risco real e prazo determinante', 'Quando há instauração de ação penal militar, o militar passa a responder a acusação formal perante a Justiça Militar. Já existe imputação definida, há prazos processuais rígidos e a estratégia de defesa é determinante. A atuação técnica envolve análise aprofundada da prova, da dinâmica dos fatos e das particularidades da atividade militar.', 'tint'),
 b_checks('Erros comuns que aumentam o risco', '', ['Prestar depoimento sem conhecer os autos','Tentar explicar tudo sem estratégia definida','Não exercer o direito ao silêncio quando necessário','Apresentar defesa administrativa genérica','Subestimar o procedimento por ser interno'], warn=True),
 b_checks('Impactos na carreira militar', 'No âmbito militar, qualquer apontamento, mesmo em fase inicial de investigação, pode gerar reflexos concretos na vida funcional.', ['Restrições ou suspensão de promoções','Reclassificação de comportamento disciplinar','Impedimento de frequentar cursos de formação ou aperfeiçoamento','Prejuízo na antiguidade e no conceito funcional','Limitação de oportunidades dentro da carreira','Risco de sanções disciplinares mais gravosas'], tint=True, warn=True),
 b_checks('O que a atuação técnica desde o início permite', '', ['Compreender a acusação de forma precisa','Alinhar a narrativa dos fatos','Evitar autoincriminação','Identificar inconsistências e ilegalidades','Proteger a carreira e a liberdade do militar']),
 b_statement('Possibilidade de revisão e controle judicial', 'Diante de decisões administrativas ou penais desfavoráveis, é possível interpor recursos nas instâncias competentes, questionar irregularidades do procedimento e buscar revisão judicial, quando cabível. O controle judicial tem como finalidade assegurar o respeito às garantias legais e constitucionais.', 'tint'),
 b_faq('Dúvidas frequentes', '', [
   ('Sou obrigado a responder tudo no IPM?','Não. Você possui direito ao silêncio e à assistência por advogado.'),
   ('Sindicância pode virar PAD ou processo penal?','Sim. Dependendo da apuração, o procedimento pode evoluir.'),
   ('Preciso de advogado no PADM?','Não é obrigatório, mas é recomendável diante dos riscos envolvidos.'),
   ('Fui citado na Justiça Militar. O que devo fazer?','É necessário apresentar defesa técnica dentro do prazo legal.')]),
 b_statement('O procedimento pode afetar carreira, reputação e futuro funcional', 'A defesa técnica busca fazer com que a conduta seja analisada dentro do contexto real da atividade e evitar que registros indevidos gerem consequências desproporcionais.', 'quiet'),
 lambda link: b_cta('Foi intimado ou citado em procedimento militar?', 'Um primeiro contato permite organizar o cenário, identificar urgências e definir a resposta técnica cabível.', 'Solicitar orientação jurídica', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre Direito Militar.')

# ======================= ASSISTÊNCIA FUNCIONAL =======================
page_area('mensalista-funcional',
 'Assistência Jurídica funcional para Policiais e Bombeiros Militares | Quartieri & Maldonado Advogados Associados',
 'Assistência jurídica contínua para policiais e bombeiros militares do Rio Grande do Sul, com foco em defesa técnica.',
 'Assistência funcional',
 'Proteção jurídica contínua para quem atua na segurança pública',
 'Atendimento preventivo e resposta técnica para Brigada Militar, Bombeiros Militares e SUSEPE no Rio Grande do Sul.',
 'Falar com o escritório', 'funcional', 'Ilustração de um distintivo de segurança pública com uma chama.', None, [
 b_statement('Atuação ajustada à rotina funcional', 'O acompanhamento considera o vínculo funcional, o tipo de procedimento e a urgência do caso.', 'tint'),
 b_details('Públicos atendidos', 'Grupos centrais que recebem nossa assistência funcional.', [
   {'t':'Brigada Militar','p':'Orientação em sindicâncias, PADs, IPMs e questões correlatas.','href':'brigadianos.html','more':'Ver a assistência para brigadianos'},
   {'t':'Bombeiros Militares','p':'Suporte técnico em procedimentos disciplinares e funcionais.','href':'bombeiros-militares.html','more':'Ver a assistência para bombeiros'},
   {'t':'SUSEPE','p':'Acompanhamento em sindicâncias, PADs e demandas da rotina institucional.','href':'policiais-penais.html','more':'Ver a assistência para policiais penais'}]),
 b_band('O que o plano oferece', 'Três frentes centrais do acompanhamento.', [
   {'t':'Orientação preventiva','p':'Leitura inicial de riscos e decisões funcionais sensíveis.'},
   {'t':'Análise técnica','p':'Avaliação de sindicâncias, PADs e outras demandas correlatas.'},
   {'t':'Acompanhamento contínuo','p':'Mais segurança para agir cedo e evitar improviso.'}]),
 b_statement('Atendimento com foco em rotina institucional', 'A leitura do caso incorpora urgência típica de sindicância, PAD e procedimentos internos antes que cristalize risco maior.', 'quiet'),
 b_faq('Dúvidas iniciais', 'Pontos iniciais para avaliar quando buscar orientação jurídica.', [
   ('Para quem esse atendimento foi pensado?','Para profissionais da Brigada Militar, Bombeiros Militares e SUSEPE em questões funcionais, disciplinares e correlatas.'),
   ('O contato serve só quando já existe procedimento?','Não. A orientação preventiva ajuda a avaliar riscos e definir condutas antes que a situação avance.'),
   ('Quando vale a pena procurar o escritório?','Ao primeiro sinal de sindicância, PAD, apuração interna ou dúvida funcional que exija leitura jurídica mais segura.'),
   ('Como funciona o primeiro contato?','O contato inicial serve para entender a situação, indicar o próximo passo e esclarecer a lógica do atendimento.')]),
 lambda link: b_cta('Converse com o escritório antes que a situação avance', 'Um primeiro contato pode esclarecer o cenário e indicar o próximo passo com mais segurança.', 'Entrar em contato', link),
 ], 'Olá! Vim pelo site e gostaria de saber mais sobre a assistência jurídica funcional.')

# ======================= DIREITO PÚBLICO =======================
page_area('direito-publico',
 'Direito Público | Quartieri & Maldonado Advogados Associados',
 'Atuação técnica em Direito Público: processos administrativos disciplinares, investigação social em concursos, direito militar e defesa de servidores e candidatos.',
 'Direito Público',
 'Atuação técnica em Direito Público',
 'Defesa de servidores, candidatos e militares em procedimentos administrativos, disciplinares e situações que envolvem relações com o Estado.',
 'Falar com o escritório', 'publico', 'Ilustração de um edifício público com colunas.', None, [
 b_statement('Relações com o Estado exigem leitura técnica específica', 'Procedimentos administrativos, investigações disciplinares, concursos públicos e carreiras militares envolvem regras próprias, prazos rígidos e consequências que podem ser duradouras. A atuação jurídica nesse campo exige conhecimento do ambiente institucional, dos limites legais da Administração e das garantias asseguradas ao cidadão diante do poder público.', 'tint'),
 b_checks('Principais temas atendidos', '', ['Processos administrativos disciplinares e sindicâncias','Investigação social em concursos públicos','Procedimentos disciplinares e penais militares','Defesa em IPM, PADM e ação penal militar','Recursos administrativos e controle judicial de atos','Retirada e restrição de antecedentes criminais']),
 b_details('Frentes de atuação', 'Áreas específicas de atuação do escritório em Direito Público.', [
   {'t':'Remoção de servidor público','p':'Pedidos de remoção, negativas administrativas e regras específicas para policiais penais do Rio Grande do Sul.','href':'remocao-servidor-publico.html','more':'Ver a página sobre remoção'},
   {'t':'Direito Administrativo Sancionador','p':'Defesa técnica em PAD, sindicância e procedimentos disciplinares contra servidores públicos.','href':'administrativo-sancionador.html','more':'Ver a página sobre PAD e sindicância'},
   {'t':'Investigação Social em Concursos','p':'Análise e questionamento de registros utilizados na investigação social de concursos públicos.','href':'investigacao-social.html','more':'Ver a página sobre investigação social'},
   {'t':'Direito Militar','p':'Defesa em IPM, sindicância, PADM e ação penal militar, com foco na proteção da carreira e da liberdade.','href':'../militar/index.html','more':'Ver a página de Direito Militar'}], tint=True),
 b_statement('Administrativo e controle judicial', 'A defesa técnica se articula tanto na reconstrução dos fatos em sede administrativa quanto, quando necessário, no controle de legalidade pela Justiça.', 'quiet'),
 b_faq('Dúvidas iniciais', 'Pontos iniciais para avaliar quando buscar orientação jurídica.', [
   ('O escritório atua apenas em processos judiciais?','Não. A atuação abrange a esfera administrativa, como sindicâncias, PADs e recursos, além do controle judicial de atos da Administração.'),
   ('Servidor público e militar têm garantias no processo disciplinar?','Sim. O contraditório, a ampla defesa, o acesso aos autos e o direito à assistência por advogado são garantias fundamentais que devem ser observadas em qualquer procedimento.'),
   ('É possível questionar a eliminação em concurso público?','Sim. A jurisprudência do STJ e do STF limita o uso de registros sem relevância jurídica atual para eliminar candidatos, e a decisão pode ser questionada administrativa e judicialmente.'),
   ('Como funciona o primeiro contato?','O primeiro contato serve para compreender a situação apresentada, verificar a viabilidade jurídica e indicar os próximos passos com objetividade.')]),
 lambda link: b_cta('Converse com o escritório para avaliar o caso', 'A análise inicial organiza os fatos, identifica riscos e indica a medida juridicamente cabível para a situação.', 'Entrar em contato', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre Direito Público.')

# ======================= DIREITO TRABALHISTA =======================
page_area('trabalhista',
 'Direito Trabalhista | Quartieri & Maldonado Advogados Associados',
 'Atuação objetiva em conflitos trabalhistas. Leitura técnica de verbas, jornada, rescisões e conflitos de trabalho.',
 'Direito Trabalhista',
 'Atuação objetiva em conflitos trabalhistas',
 'Leitura técnica de verbas, jornada, rescisões e conflitos de trabalho, com análise da prova e dos riscos do caso.',
 'Falar com o escritório', 'trabalhista', 'Ilustração de um capacete de trabalho e uma pasta.', 'jackson', [
 b_statement('Casos trabalhistas com análise direta e base técnica sólida', 'O escritório atua em demandas trabalhistas que exigem interpretação precisa da relação contratual, da jornada praticada, dos documentos disponíveis e dos reflexos jurídicos envolvidos. A avaliação considera riscos, viabilidade jurídica, produção de prova e a medida cabível para solução do conflito.', 'tint'),
 b_details('Principais temas trabalhistas analisados pelo escritório', '', [
   {'t':'Rescisão indireta','p':'Análise técnica e condução de pedidos de rescisão indireta por descumprimento contratual.','href':'rescisao-indireta.html','more':'Ver a página sobre rescisão indireta'},
   {'t':'Horas extras, intervalos e jornadas irregulares','p':'Análise objetiva de jornadas, controles de ponto, intervalos e reflexos decorrentes de horas extraordinárias.'},
   {'t':'Verbas rescisórias e divergências no encerramento do contrato','p':'Verificação técnica de valores rescisórios, prazos, descontos e inconsistências no término do vínculo.'},
   {'t':'Insalubridade, periculosidade e adicionais legais','p':'Exame jurídico de exposição a risco, condições de trabalho e cabimento de adicionais previstos em lei.'},
   {'t':'Acidente de trabalho e repercussões contratuais','p':'Avaliação das consequências contratuais e indenizatórias relacionadas a acidentes e afastamentos laborais.'},
   {'t':'Reconhecimento de vínculo de emprego','p':'Análise dos elementos da relação de trabalho para apuração da existência de vínculo empregatício.'},
   {'t':'Assédio moral e irregularidades no ambiente laboral','p':'Leitura técnica de condutas abusivas no ambiente de trabalho, identificando-se o contexto probatório e as medidas jurídicas cabíveis.'},
   {'t':'Defesa e acompanhamento em reclamações trabalhistas','p':'Atuação estratégica na defesa ou condução de reclamações trabalhistas com análise processual consistente.'}]),
 b_band('Frentes de atuação', 'Áreas específicas de atuação do escritório em matéria trabalhista.', [
   {'t':'Para trabalhadores','p':'Defesa de direitos, análise de verbas e condução de demandas para quem é parte como empregado.','href':'trabalhador.html','more':'Ver a página para trabalhadores'},
   {'t':'Para empresas','p':'Assessoria jurídica trabalhista preventiva e contenciosa para empregadores.','href':'empresas.html','more':'Ver a assessoria para empresas'}]),
 b_statement('Do preventivo ao contencioso', 'A mesma leitura técnica de verbas e jornada orienta acordos, defesas e medidas quando o conflito já está posto.', 'quiet'),
 b_faq('Dúvidas iniciais', 'Pontos iniciais para avaliar quando buscar orientação jurídica.', [
   ('É preciso já existir ação judicial em andamento para buscar o atendimento jurídico?','Não. O contato inicial pode ocorrer tanto para análise preventiva quanto para atuação em demandas já ajuizadas.'),
   ('O escritório atua para trabalhadores e empregadores?','Sim. A análise jurídica é direcionada conforme a posição ocupada no conflito e as particularidades do caso concreto.'),
   ('Como funciona o primeiro contato?','O primeiro contato serve para compreender a situação apresentada, verificar a viabilidade jurídica e indicar os próximos passos com objetividade.')]),
 lambda link: b_cta('Converse com o escritório para avaliar o caso', 'A análise inicial organiza os fatos, identifica riscos e indica a medida juridicamente cabível para a situação.', 'Entrar em contato', link),
 ], 'Olá! Vim pelo site e gostaria de orientação sobre Direito Trabalhista.')

exec(open(os.path.join(HERE,'areas3.py'),encoding='utf-8').read())
exec(open(os.path.join(HERE,'areas4.py'),encoding='utf-8').read())

