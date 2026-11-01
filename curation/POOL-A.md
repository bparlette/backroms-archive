# Tranche A — VGMaps NES + SNES candidate pool

**Deliverable:** `pool-a.json` — 600 ranked candidates (300 NES + 300 SNES, best first within each
platform block), every URL verified live (HTTP 200 + `image/*`), live pixel dims recorded for every
entry. This is an over-supplied pool for the merge pass — per-game caps and the final 1,000
selection happen there, not here.

## Counts

| | Entries | Distinct games | side | top | other |
|---|---|---|---|---|---|
| NES | 300 | 83 | 214 | 69 | 17 |
| SNES | 300 | 76 | 162 | 111 | 27 |
| **Total** | **600** | **159** | **376** | **180** | **44** |

- **Side-view total is 376 — comfortably above the 250 watch-line**, so no shortfall finding.
  NES skews side (platformer/action library); SNES skews top (its RPG catalog is deep).
- Dims: long-edge median 2,306 px; 537 of 600 sit in the 800–3,200 px sweet band for Qwen's
  vision budget; min 432, max 5,920 (bar ceiling 6,000).

## How the pool was built

1. **Universe:** the existing VGMaps enumeration (`vgmaps-pass/vgmaps_games.json`) — NES 9,260 +
   SNES 8,379 maps with catalogued dims.
2. **Bar filter** (dims + names, applied to all): single-area only — long edge ≤ 6,000 px, aspect
   ≤ 8:1, long edge ≥ 320, short edge ≥ 120, ≥ 45k pixels; name rejects for item/enemy charts,
   legends, password/ending/title screens, menus, diagrams, box/manual art; whole-world composites
   ("world map / overworld / complete / full / entire") rejected when long edge > 2,600 px.
   **12,477 maps passed** (NES 5,748, SNES 6,729).
3. **Ranking:** score = iconic-franchise weight + continuity with the current catalog (same map
   URL or same game already in it) + detail sweet-spot (long edge 800–3,200, 0.4–6 MP) +
   place-name signals. Selection per platform: top slice at per-game cap 16 (giant franchises) /
   12, then a breadth fill at cap 6 so the pool spans 159 games instead of a few franchises.
4. **Verification:** every candidate URL was fetched live — status, content type, and true pixel
   dims read from the image header (PIL). Across all sets touched in this tranche, **1,643/1,643
   URLs returned 200 + image/\***; VGMaps never blocked or throttled. Dims in `pool-a.json` are
   the live-measured ones (they matched the enumeration).
5. **`view` tags:** one representative map per distinct game (159 images) was assembled into
   labeled contact sheets and read visually; each game was tagged side/top/other from its actual
   maps, with mixed-genre games (Blaster Master, ActRaiser, Zelda II, TMNT, Contra III,
   Gargoyle's Quest II) tagged **other**, fighting/puzzle/first-person/behind-view games
   (Punch-Out!!, Mortal Kombat II, Shadowgate, Rad Racer, Tetris Attack…) also **other**.
   Track-plan maps (Super Mario Kart, Super Off Road) are tagged **top** — the map itself is a
   top-down layout. Tags are per game; individual maps in a game overwhelmingly share the view.
6. **`iconic` (1–5)** per game: 5 = top-tier franchises (Mario, Zelda, Metroid, Castlevania,
   Mega Man, Final Fantasy, Dragon Quest, Kirby, Donkey Kong, Chrono Trigger…), 4 = well-known,
   3 = in the current catalog / cult-recognized, 2 = enthusiast-known. Distribution in pool:
   5→215, 4→328, 3→50, 2→7 (the ranked pool is deliberately fame-heavy).
7. **`detail` (1–5)** from live dims only: 5 = 1–8 MP with long edge 900–3,400 (tiles stay legible
   at the ~1,200 px vision downscale); stepping down by megapixels/edge from there.
   Distribution: 5→461, 4→85, 3→41, 2→12, 1→1.

## Per-game tallies over the ~10 soft cap (flagged for merge, not trimmed here)

| Game | Maps |
|---|---|
| Kirby's Adventure | 16 |
| Kirby's Dream Land 3 | 16 |
| Castlevania III: Dracula's Curse | 15 |
| Adventure Island II | 12 |
| Zombies Ate My Neighbors | 12 |
| ActRaiser 2 | 12 |
| Blackthorne | 12 |
| The Lost Vikings | 12 |

All other games ≤ 10. The 16s sit at the giant-franchise ceiling used during selection.

## Caveats the merge pass should know

- **Single-screen screen-grids:** a handful of entries for single-screen games are per-screen
  grids/stacks rather than one continuous map (Dig Dug (J) ×1, Lode Runner ×2, Mario Bros. ×1).
  Each cell is a complete stage, but if the merge wants strictly one-area images, drop these first.
- **Chart-adjacent singletons (1 entry each):** Millipede (poster-style presentation),
  Stunt Race FX (track-select style), Tetris Attack (constellation-style stage map),
  Uniracers (sparse line-art track). They passed the mechanical bar; they are the pool's weakest
  generation references and are ranked accordingly.
- **Caption furniture:** some VGMaps maps carry small author/caption blocks (e.g. Dragon Warrior
  IV ×6). Content is a genuine area map; the caption is a thin strip, not annotation of the map.
- **Smallest entry:** Super Mario All-Stars' "Mushroom House" (288×432) — a real single-interior
  map with a decorative header; legitimately in the pool but minimal detail.
- **View tags are per game, not per image.** A game tagged side can contain an occasional
  overhead bonus/ hub map and vice versa (e.g. Kirby's Adventure's hub maps). If the side-scroller
  library needs purity, re-check the specific maps drawn from mixed catalogs (Kirby, Skyblazer,
  Demon's Crest).

## Blockers

None. VGMaps served everything (1,643/1,643 live checks passed). No source was dropped.

## Files

- `pool-a.json` — the 600 candidates: {game, target, platform, image_url, view, dims [w,h],
  source: "VGMaps", source_page (atlas index + game anchor), iconic, detail}.
- Checkpoints: `pool.json` (18,183 bar-passing maps, all platforms), `candidates_a.json`
  (selection), `verify_out.json` (1,643 live verifications), `games_a.json` + `views_map.py`
  (view classification table), `eyeball/sheetA1–3.png` (the classification contact sheets).
