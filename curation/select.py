#!/usr/bin/env python3
"""Stage 2: constrained selection of exactly 1,000 from union.json, view-band
adjustment, bench, and the proposed catalog build."""
import json, collections

BASE = '/home/hatch/workspace/worlds-game/map-first'
union = json.load(open(f'{BASE}/union.json'))
union.sort(key=lambda r: (-r['score_adj'], -r['pool_pct'], r['pool_rank']))

plat_cands = collections.Counter(r['platform'] for r in union)
FLOOR_PLATS = {p for p, c in plat_cands.items() if c >= 20}
FLOOR_N = 20

selected = {}          # image_url -> record
sel_order = []         # selection sequence (for diagnostics)
game_count = collections.Counter()
protected = set()      # urls protected from view-band displacement

def try_add(r, force=False):
    if r['image_url'] in selected:
        return False
    gc = game_count[r['gkey']]
    if gc >= 16:
        return False
    if gc >= 10 and not (r['iconic'] == 5 and r['detail'] >= 4):
        return False
    selected[r['image_url']] = r
    sel_order.append(r['image_url'])
    game_count[r['gkey']] += 1
    return True

# --- pass 1: platform floors (top-20 per >=20-candidate platform) ---
for p in sorted(FLOOR_PLATS):
    n = 0
    for r in union:
        if n >= FLOOR_N:
            break
        if r['platform'] == p and try_add(r):
            protected.add(r['image_url'])
            n += 1

# --- pass 2: breadth protection tiers ---
# The brief names Atari a major family that must stay meaningfully present;
# its maps are detail-capped by the tranche rubrics, so the generic score
# gate would zero it. Tier it explicitly instead:
#   Atari 2600 (14 candidates)      -> floor 10 (tranche C's curated set size)
#   platforms with 5-19 candidates  -> top 2 if score >= 11
#   platforms with 3-4 candidates   -> top 1 if score >= 11
def protect(p, want, min_detail):
    # Rank-based (within-platform), not absolute-score: tranche rubrics cap
    # some platforms' detail scores (Atari tops out at score 9), so an
    # absolute gate zeroes whole families the brief says to keep present.
    n = 0
    for r in union:
        if n >= want:
            break
        if r['platform'] == p and r['detail'] >= min_detail and try_add(r):
            protected.add(r['image_url'])
            n += 1

protect('Atari 2600', 10, 2)
for p, c in sorted(plat_cands.items()):
    if p == 'Atari 2600':
        continue
    if 5 <= c < 20:
        protect(p, 2, 2)
    elif 3 <= c < 5:
        protect(p, 1, 3)

floor_end = len(selected)

# --- pass 3: global greedy fill ---
for r in union:
    if len(selected) >= 1000:
        break
    try_add(r)

print(f"after floors+protection: {floor_end}; after greedy: {len(selected)}")

# --- pass 4: view band 650-750 (quality bar absolute) ---
def side_count():
    return sum(1 for r in selected.values() if r['view'] == 'side')

def plat_count(p):
    return sum(1 for r in selected.values() if r['platform'] == p)

swaps_in = swaps_out = 0
unselected = [r for r in union if r['image_url'] not in selected]

if side_count() > 750:
    # trim weakest selected side picks for best unselected non-side
    non_side_pool = [r for r in unselected if r['view'] != 'side']
    side_sel = sorted((r for r in selected.values() if r['view'] == 'side'),
                      key=lambda r: (r['score_adj'], r['pool_pct']))
    for out_r in side_sel:
        if side_count() <= 750:
            break
        cand = next((c for c in non_side_pool
                     if c['image_url'] not in selected
                     and game_count[c['gkey']] < 10), None)
        if cand is None:
            break
        if out_r['platform'] in FLOOR_PLATS and plat_count(out_r['platform']) <= FLOOR_N:
            continue
        del selected[out_r['image_url']]
        game_count[out_r['gkey']] -= 1
        selected[cand['image_url']] = cand
        game_count[cand['gkey']] += 1
        swaps_out += 1

if side_count() < 650:
    side_pool = [r for r in unselected if r['view'] == 'side' and r['detail'] >= 3 and r['score'] >= 10]
    # displacement candidates: non-side, not iconic-5 (protected class), not floor/protection picks
    disp = sorted((r for r in selected.values()
                   if r['view'] != 'side' and r['iconic'] < 5 and r['image_url'] not in protected),
                  key=lambda r: (r['score_adj'], r['pool_pct']))
    di = 0
    for in_r in side_pool:
        if side_count() >= 650:
            break
        if game_count[in_r['gkey']] >= 10:
            continue
        while di < len(disp):
            out_r = disp[di]; di += 1
            if out_r['image_url'] not in selected:
                continue
            if out_r['platform'] in FLOOR_PLATS and plat_count(out_r['platform']) <= FLOOR_N:
                continue
            if plat_count(out_r['platform']) <= 1:
                continue
            del selected[out_r['image_url']]
            game_count[out_r['gkey']] -= 1
            selected[in_r['image_url']] = in_r
            game_count[in_r['gkey']] += 1
            swaps_in += 1
            break

leftover_side = [r for r in union if r['image_url'] not in selected
                 and r['view'] == 'side' and r['detail'] >= 3 and r['score'] >= 10]
print(f"eligible side tail left unselected: {len(leftover_side)}")
print(f"view swaps: in={swaps_in} out={swaps_out}; final side={side_count()}")
assert len(selected) == 1000, len(selected)

# --- bench: next 100 unselected by rank ---
bench = [r for r in union if r['image_url'] not in selected][:100]

final = list(selected.values())
final.sort(key=lambda r: (-r['score_adj'], -r['pool_pct'], r['pool_rank']))

# diagnostics
print("final platforms:", dict(collections.Counter(r['platform'] for r in final).most_common()))
print("final views:", dict(collections.Counter(r['view'] for r in final)))
print("final continuity:", sum(1 for r in final if r['cont']))
gc = collections.Counter(r['gkey'] for r in final)
disp_name = {}
for r in final:
    disp_name[r['gkey']] = r['game']
print("games >10:", [(disp_name[g], c) for g, c in gc.most_common() if c > 10])
print("games ==10:", sum(1 for c in gc.values() if c == 10), "| distinct games:", len(gc))
print("bench views:", dict(collections.Counter(r['view'] for r in bench)))

json.dump({'selected': final, 'bench': bench,
           'diag': {'swaps_in': swaps_in, 'swaps_out': swaps_out,
                    'after_floors': floor_end}},
          open(f'{BASE}/selection.json', 'w'), indent=1)
