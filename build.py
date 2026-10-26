# Monta o site completo na pasta dist/ (rodado automaticamente pelo Netlify a cada publicação)
import os, shutil, runpy, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'dist')
os.environ['SITE_OUT'] = OUT
sys.path.insert(0, os.path.join(ROOT, 'build'))

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(os.path.join(ROOT, 'src'), OUT)

g = runpy.run_path(os.path.join(ROOT, 'build', 'pages.py'))   # áreas, privacidade, termos, 404
import posts
lista = posts.build(g, OUT, os.path.join(ROOT, 'content', 'posts'))

# Mapa do site
urls = ['/']
for base, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith('.html') or f == '404.html' or 'admin' in base: continue
        rel = os.path.relpath(os.path.join(base, f), OUT).replace(os.sep, '/')
        if rel == 'index.html': continue
        rel = rel[:-len('index.html')] if rel.endswith('index.html') else rel[:-5]
        urls.append('/' + rel)
with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in sorted(set(urls)):
        fh.write(f'  <url><loc>https://quartierimaldonado.com{u}</loc></url>\n')
    fh.write('</urlset>\n')

# Tag do Google (Google Ads + Analytics) em modo sem cookies, conforme a Política de Privacidade
GTAG_ID = 'GT-TXBWT6T9'
GTAG = f"""<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('consent', 'default', {{ad_storage: 'denied', analytics_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'}});
gtag('js', new Date());
gtag('config', '{GTAG_ID}');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GTAG_ID}"></script>
"""
for base, _, files in os.walk(OUT):
    if 'admin' in base: continue
    for f in files:
        if not f.endswith('.html'): continue
        path = os.path.join(base, f)
        html = open(path, encoding='utf-8').read()
        if 'googletagmanager.com/gtag' in html or '</head>' not in html: continue
        open(path, 'w', encoding='utf-8').write(html.replace('</head>', GTAG + '</head>', 1))

# Imagens enviadas pelo painel: reduz e comprime automaticamente as muito grandes
try:
    from PIL import Image, ImageOps
    up = os.path.join(OUT, 'img', 'uploads')
    for base, _, files in os.walk(up):
        for f in files:
            if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): continue
            path = os.path.join(base, f)
            try:
                im = Image.open(path)
                if im.width <= 1600 and os.path.getsize(path) <= 400_000: continue
                im = ImageOps.exif_transpose(im)
                im.thumbnail((1600, 1600))
                if f.lower().endswith(('.jpg', '.jpeg')):
                    im.convert('RGB').save(path, quality=80, optimize=True, progressive=True)
                else:
                    im.save(path, optimize=True)
            except Exception as e:
                print('Aviso: não consegui otimizar', f, e)
except ImportError:
    print('Aviso: Pillow não instalado, imagens do painel não foram otimizadas.')

print(f'Site gerado em dist/ com {len(lista)} publicação(ões).')
