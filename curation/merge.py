#!/usr/bin/env python3
"""Merge the four map-first pools into the final 1,000-world catalog.
Stage 1: load pools, normalize pool-D platform labels, dedupe (URL, then
normalized game+target), compute ranking. Stage 2: constrained selection
(per-game caps, platform floors, view band), bench, catalog build.
Outputs: union.json (diagnostics), selection.json (picks + bench records).
"""
import json, re, collections, sys

BASE = '/home/hatch/workspace/worlds-game/map-first'

def load(name):
    return json.load(open(f'{BASE}/pool-{name}.json'))

# ---------- pool D platform normalization ----------
SECTION = {'NES':'NES','SuperNES':'SNES','Genesis':'Genesis','MasterSystem':'Master System',
           'GameGear':'Game Gear','Arcade':'Arcade','Atari2600':'Atari 2600'}
LABEL_FALLBACK = {'NES / Famicom':'NES','SNES / Super Famicom':'SNES','More Arcade':'Arcade',
    'More Atari 2600':'Atari 2600','Arcade (Neo Geo / SNK)':'Arcade','Arcade (Taito / Irem)':'Arcade',
    'Arcade (Psikyo / Toaplan / Raizing / Video System)':'Arcade',
    'Atari 2600 / 5200 / 7800':'Atari 2600','Sega CD / Mega-CD / 32X':'Sega CD',
    'Sega Genesis & Master System':'Genesis','Sega Genesis / Master System / Game Gear':'Genesis',
    'Sega Genesis / Mega Drive':'Genesis'}

def d_platform(e):
    raw = e['platform']
    m = re.search(r'vgmaps\.com/Atlas/([^/]+)/', e.get('image_url') or '')
    if e['source'] == 'nesmaps':
        return 'NES'
    if m and m.group(1) in SECTION:
        # B established the Genesis atlas section also files Sega CD titles;
        # the old-catalog Sega CD tranche label is the only signal for those.
        if raw == 'Sega CD / Mega-CD / 32X' and m.group(1) == 'Genesis':
            return 'Sega CD'
        return SECTION[m.group(1)]
    return LABEL_FALLBACK.get(raw, raw)

# ---------- normalization for dedupe / caps / continuity ----------
def norm_text(s):
    s = (s or '').lower()
    s = re.sub(r'\([^)]*\)', ' ', s)          # drop parentheticals in key only
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return ' '.join(s.split())

def place_key(game, target):
    return norm_text(game) + ' :: ' + norm_text(target)

def game_key(game):
    return norm_text(game)

# ---------- load + annotate ----------
pools = {}
for name in 'abcd':
    pools[name] = load(name)
pools['d'] = [dict(e, platform=d_platform(e)) for e in pools['d']]

old = json.load(open('/home/hatch/workspace/worlds-game/vgmaps-apply/merged_catalog.json'))
continuity = set(place_key(e['game'], e['target']) for e in old)

records = []
for name in 'abcd':
    p = pools[name]
    for i, e in enumerate(p):
        r = dict(e)
        r['pool'] = name
        r['pool_rank'] = i + 1
        r['pool_pct'] = (len(p) - i) / len(p)          # 1.0 at top of pool
        r['score'] = 2 * e['iconic'] + e['detail']
        r['cont'] = place_key(e['game'], e['target']) in continuity
        r['score_adj'] = r['score'] + (0.5 if r['cont'] else 0.0)
        r['gkey'] = game_key(e['game'])
        r['pkey'] = place_key(e['game'], e['target'])
        records.append(r)

records.sort(key=lambda r: (-r['score_adj'], -r['pool_pct'], r['pool_rank']))

# ---------- dedupe: URL first, then (game, target) ----------
seen_url, after_url, url_dupes = set(), [], 0
for r in records:
    if r['image_url'] in seen_url:
        url_dupes += 1
        continue
    seen_url.add(r['image_url'])
    after_url.append(r)

seen_place, union, place_dupes, cross_plat = set(), [], 0, 0
for r in after_url:
    if r['pkey'] in seen_place:
        place_dupes += 1
        kept = next(u for u in union if u['pkey'] == r['pkey'])
        if kept['platform'] != r['platform']:
            cross_plat += 1
        continue
    seen_place.add(r['pkey'])
    union.append(r)

print(f"raw records: {len(records)}")
print(f"URL dupes removed: {url_dupes}; place dupes removed: {place_dupes} (cross-platform: {cross_plat})")
print(f"union size: {len(union)}")
pc = collections.Counter(r['platform'] for r in union)
print("union platform candidates:")
for p, c in pc.most_common():
    print(f"  {p}: {c}")
print("union view split:", dict(collections.Counter(r['view'] for r in union)))
print("union side & detail>=3:", sum(1 for r in union if r['view']=='side' and r['detail']>=3))
print("platforms with >=20 candidates:", [p for p, c in pc.items() if c >= 20])
print("continuity hits in union:", sum(1 for r in union if r['cont']))

json.dump(union, open(f'{BASE}/union.json', 'w'), indent=1)
