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
print(f'Site gerado em dist/ com {len(lista)} publicação(ões).')
