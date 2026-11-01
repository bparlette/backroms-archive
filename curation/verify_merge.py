#!/usr/bin/env python3
"""Stage 4a: pick seeded-random eyeball (20) and re-verify (30) samples from
the proposed catalog; download eyeball images, downscale to 1200px long edge,
build labeled contact sheets; live-check the 30 URLs."""
import json, random, os, subprocess, urllib.request, urllib.error
from PIL import Image, ImageDraw

BASE = '/home/hatch/workspace/worlds-game/map-first'
OUT = f'{BASE}/eyeball-merge'
os.makedirs(OUT, exist_ok=True)
cat = json.load(open(f'{BASE}/proposed_catalog.json'))

rng = random.Random(20261101)
eyeball = rng.sample(cat, 20)
reverify = rng.sample(cat, 30)
json.dump({'eyeball_ids': [e['id'] for e in eyeball],
           'reverify_ids': [e['id'] for e in reverify]},
          open(f'{OUT}/samples.json', 'w'), indent=1)
print('eyeball ids:', [e['id'] for e in eyeball])
print('reverify ids:', [e['id'] for e in reverify])

# ---- download + downscale eyeball set ----
tiles = []
for e in eyeball:
    raw = f"{OUT}/raw_{e['id']}.png"
    if not os.path.exists(raw):
        subprocess.run(['curl', '-sL', '--max-time', '60', '-o', raw, e['image_url']], check=False)
    try:
        im = Image.open(raw).convert('RGB')
    except Exception as ex:
        print('eyeball download/open failed', e['id'], ex)
        continue
    w, h = im.size
    scale = 1200 / max(w, h)
    im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    small = f"{OUT}/small_{e['id']}.jpg"
    im.save(small, quality=82)
    tiles.append((e, small, (w, h)))
print('eyeball tiles ready:', len(tiles))

# ---- contact sheets: 2 sheets x 10, tiles thumbnailed at 560px wide ----
def sheet(chunk, path):
    TW, TH, PAD, LAB = 560, 420, 10, 22
    cols, rows = 2, 5
    W = cols * (TW + PAD) + PAD
    H = rows * (TH + LAB + PAD) + PAD
    canvas = Image.new('RGB', (W, H), (24, 24, 24))
    d = ImageDraw.Draw(canvas)
    for i, (e, small, orig) in enumerate(chunk):
        im = Image.open(small)
        im.thumbnail((TW, TH))
        x = PAD + (i % cols) * (TW + PAD)
        y = PAD + (i // cols) * (TH + LAB + PAD)
        d.text((x, y), f"#{e['id']} {e['game'][:34]} | {e['target'][:30]} | {e['platform']} | {e['view']} | orig {orig[0]}x{orig[1]}",
               fill=(255, 255, 120))
        canvas.paste(im, (x, y + LAB))
    canvas.save(path, quality=85)
    print('sheet:', path, canvas.size)

sheet(tiles[:10], f'{OUT}/sheet1.jpg')
sheet(tiles[10:], f'{OUT}/sheet2.jpg')

# ---- re-verify 30 URLs ----
results = []
for e in reverify:
    url = e['image_url']
    status, ctype = None, None
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=method,
                                         headers={'User-Agent': 'Mozilla/5.0', 'Range': 'bytes=0-2047'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = resp.status
                ctype = resp.headers.get_content_type()
            break
        except urllib.error.HTTPError as ex:
            status = ex.code
            if method == 'GET':
                break
        except Exception as ex:
            status = f'ERR {ex}'
            break
    ok = (status in (200, 206)) and (ctype or '').startswith('image/')
    results.append({'id': e['id'], 'url': url, 'status': status, 'ctype': ctype, 'ok': ok})
    print(('OK ' if ok else 'FAIL'), e['id'], status, ctype, url[:90])
n_ok = sum(1 for r in results if r['ok'])
print(f're-verify: {n_ok}/{len(results)} OK')
json.dump(results, open(f'{OUT}/reverify_results.json', 'w'), indent=1)
