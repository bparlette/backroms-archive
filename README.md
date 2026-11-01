# Back Roms — Archive

A preservation snapshot of the Back Roms catalog work, taken **November 1, 2026**, at the moment the project switched from a description-first catalog to a map-first one. Nothing here is the live product — the live project (gallery, World Walker, generation loop) continues at **bparlette/worlds** (https://bparlette.github.io/worlds/). This repo exists so the pre-reset state and the full curation record behind the reset are never lost.

## What's inside

### (a) `catalog-v1/` — the original 1,000 worlds
The original description-first 1,000-world catalog exactly as it stood on the morning of Nov 1, 2026, before the map-first reset — snapshotted from `bparlette/worlds` main at commit `d1823670c11493028d74983643f6cad7e3586634`. See `catalog-v1/SNAPSHOT.md` for the file-by-file record (including why the catalog file is named `game_worlds_extracted.json` — that is its name in the live repo — and the verified-progress state, 16 of 39 scenes, at snapshot time).

### (b) `curation/` — the map-first rebuild
The Nov 1, 2026 map-first curation: **1,709 verified candidate maps** in four pools (A: VGMaps NES/SNES, B: Sega family, C: Game Boy/arcade/Atari/everything else, D: prior-pool survivors + nesmaps), the merge that pared them to the new 1,000 (`proposed_catalog.json`, selection rules: one coherent area per image, measured dimensions, legibility at ~1,200 px, per-game caps, mixed views with a deliberate side-view lean at 650/1,000), and `bench.json` — the next 100 ranked alternates. `REPORT.md` is the merge's audit; `POOL-A.md`–`POOL-D.md` are the tranche reports. See `curation/README.md` for what was deliberately left out (working scrapes and eyeball images) and why.

### (c) `research/` — the passes that fed the reset
- `research/enrich-repass/` — the enrichment re-pass over the v1 catalog (images 197 → 298, all 35 defective briefs fixed).
- `research/vgmaps-apply/` — the approved VGMaps pass applied to v1 (map primaries 29 → 313; `merged_catalog.json` is the last state of the v1 catalog line before the reset).
- `research/alt-sources/` — the scout of 15 alternative map/screenshot sources beyond VGMaps.

## A note on images

Images are **referenced by source URL throughout, not vendored**. Every catalog and pool entry points at the map or screenshot on its source site (VGMaps, nesmaps, etc.). No image binaries live in this archive — the URLs are the record, and the pools re-verified every one of them live during curation.

`MANIFEST.md` lists every file in this archive with its size and provenance.
