# Tranche D candidate pool — non-VGMaps sources + pre-qualified existing pool

**Deliverable:** `pool-d.json` — **303 ranked candidates** (best first; ranked by iconic×2 + detail).
Every URL verified live (HTTP 200 + `image/*`, PIL header dims) via `verify.py`. Nothing pushed.

## Counts by source

| Source | Candidates | Notes |
|---|---|---|
| existing (pre-qualified pool, re-judged) | 241 | of 313 entries — see audit below |
| nesmaps.com | 62 | SMB 20, Zelda (1st Quest dungeons) 9, Ninja Gaiden 9, Crystalis 7, Castlevania 6, Mega Man 6, DuckTales 5 |
| RPGClassics / shmups.wiki / Zelda Wiki / Mario Wiki / Metroid Database / Castlevania Dungeon | 0 | not enumerated — target (~300) already met by the two sources above; see "Not harvested" |

**View split (whole pool):** side 189 · top 76 · other 38.
Existing-pool views are classified by the game's native view style; nesmaps views are per-map.

## Pre-qualified pool audit (313 → 241)

- 313 entries held **259 unique URLs; all 259 verified live** (200 + image). 50 passing entries were duplicate URLs under different target names → deduped (most specific target kept).
- **22 entries failed the bar** (18 unique URLs):
  - **Stacked / multi-stage strip composites (8):** Bubble Bobble *Cave of Monsters* (256×26144 — all ~100 floors stacked), Truxton ×2 (316×41379 full vertical game), Battletoads ×2 (272×7632, two+ stages end-to-end), DKC *Mine Cart Carnage* (18944×512), Ranger X (16591×256), Monster World IV (7299×224).
  - **Whole-game scale, long edge >14,000 (4):** Faxanadu *World Tree* ×2 (15440×4199), Gunstar Heroes *Underground Magma Mine Cart Runs* (14375×4804), Midnight Resistance (14220×1811).
  - **Too small to carry detail, long edge <320 (10):** SMB3 *Dark Land Airships* (297×249), Alien Syndrome (250×250), Iron Tank (164×292), Tiny Toon (160×160), Out of This World ×2 (224×294), Super Hang-On (318×222), Yoshi's Safari (208×152), Mappy (224×288), Hopping Mappy (288×224). Several are legitimately complete single-screen maps (Mappy) — excluded on bar 3 (detail at generation scale), a judgment call the merge pass may revisit.
- **Borderline kept, with detail-score penalties (flagged for merge):** single coherent areas over the ~6,000px guideline — Super Metroid *Maridia* 8560×5168 (eyeball-checked: fully legible downscaled to 1200px, small credit block in one corner), Sonic zone acts ≈10–12k wide, Gunstar Heroes *Flying Battleship* 2286×6771, Brain Lord *Tower of Light* 1920×7200, Mega Man 4 *Pharaoh Man* 6176 wide; and long single-level strips at aspect 10–16 (e.g. Gradius *Moai Head Graveyard* 3888×280) — kept under the "truly one level" exception.

## nesmaps method

Per game: map-selection page → per-level "Background Only" map pages. **BG-only versions chosen deliberately; the site's "Labeled" variants were rejected site-wide** (bar 3, annotations). All 62 are complete single levels/areas with dims from the selection tables, confirmed by live verification.
Disclosure: nesmaps BG maps carry a small maker credit stamp in a corner margin (seen on SMB 1-1, alongside the otherwise clean level) — the level art itself is unobstructed.

## Blocks encountered

- **nesmaps bot-check:** HTML pages intermittently return a "One moment, please…" verification interstitial (hit ~7 times, more often later in the session). Image files were never blocked — every image URL verified by direct GET. Consequences, recorded not circumvented:
  - **Kid Icarus:** map pages bot-checked and 18 filename-pattern probes 404'd → 0 entries.
  - **Metroid (nesmaps):** area-map filenames unresolved (probes 404) → 0 entries (Metroid is covered by the existing pool).
  - **Zelda Second Quest:** dungeon filenames differ from the Q1 pattern (404) → only 1st Quest dungeons taken.
  - **Mega Man 2 / Commando:** the easily probed URLs serve 256×240 single screenshots, not maps → not taken (fragments fail bar 2).
- No 403/429 hard walls on any source; no other site was pushed hard enough to rate-limit.

## Not harvested (and why)

RPGClassics, shmups.wiki, Zelda Wiki, Super Mario Wiki, Metroid Database, Castlevania Dungeon were **not enumerated**: the pool hit its ~300 target from the existing pool + nesmaps first. Spot evidence only: Castlevania Dungeon stage pages are prose walkthroughs with embedded screenshots, not clean full-level maps; the franchise wikis' classic map sets largely duplicate the nesmaps BG-only maps already taken. If the merge pass runs short, these are the next veins — shmups.wiki first for arcade-shmup stage maps, which this pool is thinnest on.

## Scoring

- **iconic 1–5:** franchise/level fame (5 = Mario/Zelda/Metroid/Mega Man/Castlevania/Sonic/DKC/Final Fantasy/Chrono Trigger/Contra/Kirby tier; 2 = genuinely obscure).
- **detail 1–5:** from verified dims — sweet spot (long edge 900–4200, short ≥480, aspect ≤6) = 5, degrading with thin strips, extremes, and Atari chunkiness (capped 3).
- Rank = iconic×2 + detail, descending. The merge pass should treat the bottom ~30 as first-cut material.

## Checkpoint files (this tranche)

`d_existing_raw.json`, `d_verify_out.json`, `d_existing_dims.json`, `d_existing_pass.json`, `d_existing_fails.json`, `d_nesmaps_cand*.json`, `d_nesmaps_verify*.json`, `d_metroid_cand.json` (failed probes), `d_eyeball_maridia.jpg`, `d_eyeball_smb11.jpg` (1200px legibility checks).
