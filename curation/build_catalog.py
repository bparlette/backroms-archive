#!/usr/bin/env python3
"""Stage 3: build proposed_catalog.json (schema mirrored from the current
catalog) and bench.json from selection.json."""
import json, collections

BASE = '/home/hatch/workspace/worlds-game/map-first'
sel = json.load(open(f'{BASE}/selection.json'))
final, bench = sel['selected'], sel['bench']

HEAD = ['Atari 2600', 'NES', 'SNES', 'Genesis', 'Master System', 'Arcade',
        'Game Gear', 'Sega CD', 'Game Boy', 'Game Boy Advance']
counts = collections.Counter(r['platform'] for r in final)
rest = sorted((p for p in counts if p not in HEAD), key=lambda p: (-counts[p], p))
GROUP_ORDER = HEAD + rest

def rank_key(r):
    return (-r['score_adj'], -r['pool_pct'], r['pool_rank'])

final.sort(key=lambda r: (GROUP_ORDER.index(r['platform']),) + rank_key(r))

PROMPT = ("Generate a fully interactive 3D WebGL Three.js world representing "
          "'{target}' from {game} ({platform}). World brief: {brief} "
          "Include lighting, fog, textures/materials, animated environmental "
          "elements, and mouse/touch orbit camera controls.")

catalog = []
for i, r in enumerate(final, 1):
    brief = f"{r['target']}, {r['game']} ({r['platform']})."
    catalog.append({
        'id': i,
        'platform': r['platform'],
        'game': r['game'],
        'target': r['target'],
        'url': r['source_page'],
        'description': brief,
        'qwen_prompt': PROMPT.format(target=r['target'], game=r['game'],
                                     platform=r['platform'], brief=brief),
        'brief': brief,
        'page_title': r['game'],
        'image_url': r['image_url'],
        'image_kind': 'map',
        'image_urls': [r['image_url']],
        'image_kinds': ['map'],
        'view': r['view'],
    })

POOL_FIELDS = ['game', 'target', 'platform', 'image_url', 'view', 'dims',
               'source', 'source_page', 'iconic', 'detail']
bench_out = [{k: r[k] for k in POOL_FIELDS} for r in bench]

json.dump(catalog, open(f'{BASE}/proposed_catalog.json', 'w'), indent=1, ensure_ascii=False)
json.dump(bench_out, open(f'{BASE}/bench.json', 'w'), indent=1, ensure_ascii=False)
print('catalog entries:', len(catalog), '| bench:', len(bench_out))
print('group order:', [(p, counts[p]) for p in GROUP_ORDER])
print('first entry:', json.dumps(catalog[0], indent=1))
