# Map-first merge — final 1,000-world catalog

**Deliverables:** `proposed_catalog.json` (exactly 1,000 entries, current-catalog schema),
`bench.json` (next 100 alternates, ranked, pool-entry fields). Staged only — nothing pushed.
Supporting artifacts: `merge.py`, `select.py`, `build_catalog.py`, `verify_merge.py`,
`union.json`, `selection.json`, `eyeball-merge/` (samples, sheets, re-verify results).

## Headline numbers

| | |
|---|---|
| Candidates in (4 pools) | 1,709 |
| After URL dedupe | 1,581 (−128) |
| After (game, target) place dedupe | **1,389 unique places** (−192, of which 20 cross-platform) |
| **Final catalog** | **1,000** |
| View split | **side 650 · top 268 · other 82** |
| Distinct games | 282 |
| Continuity with current catalog | 115 of 1,000 (game, target) pairs kept |
| Spot re-verification | **30/30 URLs live** (HTTP 200/206 + `image/*`) |

## How the selection worked

- **Ranking:** score = iconic×2 + detail (the pools' common formula), +0.5 continuity bonus
  for (game, target) pairs already in the current catalog; each pool's internal rank order
  used as tiebreak (pool percentile). Pool D's platform labels were normalized before
  selection (old-catalog tranche labels like "NES / Famicom" resolved via the image's
  VGMaps Atlas section — the map's actual platform — with B's Sega-CD-in-Genesis-section
  exception preserved).
- **Per-game caps:** soft 10 / hard 16, counted per game across all platforms. Picks 11–16
  admitted only for iconic-5 games with detail ≥4 (exceptions tallied below).
- **Platform floors:** every platform with ≥20 union candidates was guaranteed its top 20.
- **Breadth protection (rank-based, see audit below):** Atari 2600 floor of 10; platforms
  with 5–19 candidates guaranteed their top 2 (detail ≥2); platforms with 3–4 candidates
  guaranteed their top 1 (detail ≥3). Protected picks are exempt from view-band displacement.
- **View band (650–750 side):** the pure score-order greedy landed at 541 side. 109 swaps
  brought it to **650**: swapped-in side picks all have detail ≥3 and score ≥10 (the quality
  bar was never bent — no detail ≤2 map was taken for the band); swapped-out picks were the
  lowest-ranked non-side picks, **excluding** all iconic-5 top-down/other maps (protected by
  rule), all floor/protection picks, and any platform's last pick. 55 eligible side
  candidates (detail ≥3, score ≥10) remain unselected, so 650 is a deliberate stop at the
  band's lower edge, not a supply limit: pushing toward 750 would have displaced
  progressively stronger top-down/other references for the weakest remaining side maps.
  That is the one real band-vs-mix tension, resolved in favor of mix quality and recorded
  here rather than hidden.

## Counts by platform × view

| Platform | side | top | other | total |
|---|---|---|---|---|
| NES | 199 | 44 | 8 | 251 |
| Genesis | 117 | 36 | 32 | 185 |
| SNES | 120 | 45 | 13 | 178 |
| Game Boy Advance | 33 | 37 | 0 | 70 |
| Game Boy (GB/GBC combined) | 15 | 44 | 1 | 60 |
| Master System | 50 | 4 | 0 | 54 |
| Arcade | 29 | 2 | 7 | 38 |
| PlayStation | 3 | 24 | 0 | 27 |
| Game Gear | 18 | 7 | 0 | 25 |
| PC | 15 | 2 | 3 | 20 |
| Nintendo DS | — | — | — | 12 |
| Atari 2600 | 1 | 1 | 8 | 10 |
| Sega CD | 2 | 5 | 3 | 10 |
| Neo Geo | — | — | — | 9 |
| TurboGrafx-16 | — | — | — | 8 |
| Commodore 64 | — | — | — | 7 |
| Nintendo 64 | — | — | — | 6 |
| PlayStation 2 | — | — | — | 5 |
| Amstrad CPC / Nintendo 3DS / Wii | — | — | — | 3 each |
| Amiga / CD-i / MSX / Virtual Boy / WonderSwan | — | — | — | 2 each |
| Apple II / Atari 5200 / Atari 7800 / ColecoVision / PSP / X68000 | — | — | — | 1 each |
| **Total** | **650** | **268** | **82** | **1,000** |

## Per-game tallies

Top 15: Dragon Warrior III **16** · Mega Man 14 · Shining Force: The Legacy Of Great
Intention 14 · Shining Force II 14 · The Legend Of Zelda 14 · Super Mario Bros. 14 ·
Final Fantasy VII 13 · Castlevania III: Dracula's Curse 12 · Final Fantasy Adventure 12 ·
Sonic & Knuckles 11 · then ten games at exactly 10 (incl. Kirby's Adventure, Super Metroid,
Golden Sun, Mario & Luigi: Superstar Saga, Alundra).

**Cap exceptions (11–16 picks) — all ten are iconic-5 franchises whose extra maps are
distinct, detail ≥4 areas**, e.g. Dragon Warrior III's 16 spans its NES and Game Boy
versions' dungeons/towers (counted under one game key across platforms); the two Shining
Force titles' 14 each are individual tactical-battle maps, each a self-contained place.
Nothing exceeds the hard cap of 16.

## Continuity

- 115 of the final 1,000 (game, target) pairs exist in the current catalog.
- Of the **39 already-generated scenes' pairs, 15 survive**. The other 24 were mostly
  description-first picks whose maps failed this pass's image bar outright (whole-game
  composites, stacked stage strips, sub-320px images — the same failures tranche D's
  audit catalogued). Their scene files are untouched; only the catalog going forward
  changes. Catalog entry #1 is again Adventure "Castles & Mazes" (Atari 2600) with the
  same VGMaps map the current catalog uses.

## Breadth-rule audit

- **The ≥20-candidates / ~2% rule: satisfied for all 10 qualifying platforms with zero
  overrides** (NES 343→251, SNES 275→178, Genesis 236→185, Arcade 85→38, Master System
  73→54, GBA 71→70, Game Boy 65→60, Game Gear 36→25, PC 35→20, PlayStation 27→27).
- **Why the protection tiers are rank-based, not score-based:** tranche rubrics cap some
  platforms' scores (Atari 2600's best union candidate scores 9 of 15 — its detail scores
  are capped for chunkiness). An absolute score gate zeroes exactly the families the
  brief names for protection; within-platform rank does not. This is a documented
  deviation from a pure global score order, costing roughly 20 slots at the margin.
- **Platforms with zero representation, and why:** Neo Geo Pocket Color (3 candidates;
  its best is a detail-1 fighting-stage image — excluded on quality, the protection
  tier's detail ≥3 gate); ZX Spectrum (its only candidate game, Double Dragon, lost all
  3 maps to higher-ranked versions of the same missions under place dedupe — the
  dedupe rule working as specified); Atari ST, Arduboy (2 candidates each, below the
  protection tiers, outscored in the open pool); Atari Lynx, Atari 8-bit, Acorn
  Archimedes, Commodore PET, PC-98, PC-FX, Intellivision (1 candidate each, outscored).

## Eyeball check (20 random final picks, downscaled to ~1,200 px)

Seeded sample (ids in `eyeball-merge/samples.json`), viewed as contact sheets:

- **Clean and fully legible (13):** Zelda Level-4 #94 (a text header strip rides above
  the dungeon grid — furniture, dungeon itself perfect), SMB 8-2 #119 and 2-1 #45
  (complete level strips; small credit block in a corner), Castlevania III #62/#52,
  Earthworm Jim #404, Shatterhand #225, Kirby's Dream Land 3 #282, Crystalis #146
  (logo/legend strip along one edge), Shining Force II #458, Mario & Luigi #861,
  Wonder Boy #667, Kirby's Dream Course #338 (isometric single hole, tagged other).
- **Borderline (3):** Dragon Warrior "Garin's Grave" #129 — map legible but ~⅓ of the
  canvas is enemy/stat info panels; Golden Sun "Mercury Lighthouse" #853 — clean map
  with a few red-X annotations; Castlevania II "Rock Castle" #755 — genuine single area
  but line work on a mostly empty white canvas, detail-poor at downscale.
- **Weak but single-place (2):** Vampire Savior #712 — a single fighting-stage backdrop
  (character sprite included); palette/look reference only, no layout. Zelda's Adventure
  (CD-i) #988 — dark FMV room-still collage, murky at downscale.
- **Bar violations found and FIXED by swap (2):** Lemmings "Level Previews" (Amiga) — a
  multi-level preview sheet, not one area; Pulseman "Bonus Stages" (Genesis) — a
  six-panel sheet of separate mini-stages. Both were replaced with eyeballed single-area
  maps (Lemmings "Level 20: We Are Now At LEMCON ONE"; RoboCop Versus The Terminator
  "Secret Level" — a complete, intricate single area), preserving platform and view
  counts. The two violators were also excluded from the bench.
- **Sample-based estimate:** ~10% of the catalog likely carries some caption furniture,
  minor annotation, or borderline trait of the kinds above; ~1% may be multi-area
  sheets that name/dims filters can't catch. Also noted: 4 catalog entries are animated
  GIFs (e.g. a Battletoads room map) — harmless as references, flagged for awareness.
- Carried-forward caveats from the tranches remain in force: pool A's view tags are
  per-game (a side-tagged game can contain an occasional overhead hub map — the side
  library should spot-check Kirby/sky-hub titles before use), pool D's borderline
  keeps (e.g. Super Metroid Maridia at 8,560 px wide, eyeballed legible by tranche D)
  were retained where their scores justified it.

## Schema notes

Entries mirror the current catalog's well-formed image entries: `id, platform, game,
target, url` (= the pool's source page), `description`, `qwen_prompt`, `brief`,
`page_title` (= game), `image_url`, `image_kind: "map"`, singleton
`image_urls`/`image_kinds`, plus the new `view` field. Briefs follow the mandated format
exactly — `"{Target}, {Game} ({Platform})."` — no invented prose, no boilerplate; the
old extraction-metadata fields (`section_count`, `description_raw`, `canonical_title`)
are not carried over. Catalogue order: platform groups in the current catalog's family
sequence (Atari 2600, NES, SNES, Genesis, Master System, Arcade, …), rank order within
each group.

## Bench

`bench.json` — the next 100 by global rank (top 65 top-view / 31 other / 4 side; NES 31,
Arcade 26, SNES 21…). Its top entries score as high as the catalog's (up to iconic 5 /
detail 5): they are franchise depth blocked by the per-game caps and view-band
displacements, not weak maps — the right first source for swaps.
