# Tranche B — Sega family candidate pool (map-first curation)

**Deliverable:** `pool-b.json` — **400 ranked candidates, best first**, every URL live-verified.
Audit trail: `pool-b-candidates.json` (4,171 bar-passing candidates, ranked),
`pool-b-verify.json` (per-URL HEAD results), `build_pool_b.py`, `select_verify_b.py`,
eyeball samples in `eyeball-b/`.

## Funnel

| Stage | Count |
|---|---|
| Sega-section maps in VGMaps enumeration (405 games) | 6,699 |
| Pass the bar (size / aspect / content rejects) | 4,171 |
| URLs HEAD-checked during selection | 590 |
| Verified OK (HTTP 200 + image/*) | 588 |
| **Final pool** | **400** |

## Counts

**By platform:** Genesis 235 · Master System 90 · Game Gear 45 · Sega CD 30 · 32X 0 · Saturn 0 · Dreamcast 0

**By source:** VGMaps 400 · Sega Retro 0 (blocked — see below)

**View split:** side 262 · top 102 · other 36

**Games represented:** 91. Iconic scores: 5 → 142 entries, 4 → 203, 3 → 48, 2 → 7.
Detail scores: 5 → 349, 4 → 45, 3 → 6. Long edge: min 576, median 2,040, max 5,629 px.

**Per-game tallies over 10 (flagged, all deliberate giant-franchise caps at 14):**
Sonic The Hedgehog 14 · Shining Force: The Legacy Of Great Intention 14 ·
Shining Force II 14 · Sonic & Knuckles 12 · Landstalker 10 (at cap).
No other game exceeds 8; 19 games contribute a single map.

## Sources — what actually happened

- **VGMaps** carried the whole tranche. The Genesis atlas section also files
  Sega CD (and 32X) titles; the 30 Sega CD entries come from there, with the
  platform field relabeled from the game title (URLs unchanged, still under
  `Atlas/Genesis/`). No (32X)-titled title passed the bar.
- **Sega Retro — BLOCKED, 0 entries.** segaretro.org sits behind an Anubis
  bot wall from this VM: the MediaWiki API and direct fetches return the
  "Making sure you're not a bot!" challenge, so image URLs cannot be
  live-verified from here, and unverifiable URLs are excluded by the pool
  rules. Not circumvented. A live-browser pass could still harvest Sega
  Retro (the alt-sources scout verified Gaiares stage images there earlier
  today) — recommended as a top-up, especially for Sega CD (Lunar etc.).
- **Saturn / Dreamcast — absent.** The VGMaps enumeration has no Saturn or
  Dreamcast sections at all, so there was nothing to draw from; 2D Saturn
  (Astal, Guardian Heroes…) is a known gap for a future source.

## Verification & QA

- Every one of the 400 URLs returned HTTP 200 + `image/*` on a HEAD check
  during this run (results in `pool-b-verify.json`).
- 2 candidate URLs failed and were excluded: Sonic 3D Blast — Volcano Valley
  Zone Acts 1 and 2 (HTTP 523, origin error).
- QA swap: Alien Soldier "Stages 14-17" (a multi-stage composite, against
  the one-area rule) was caught in the final pool and replaced with
  Earthworm Jim "Area 1".
- Eyeball check: 2 downloaded samples viewed in full — Sonic CD "Bad Future"
  (Wacky Workbench: complete, rich, only sparse START/EXIT/BOSS markers) and
  an SMS Sonic act map (complete single act; some areas render as outlined
  layout rather than filled tiles — still a full level reference).

## Notes for the merge pass

- Some targets carry VGMaps variant suffixes (e.g. "Act 2 (C)") — alternate
  renders of the same act; dedupe against other tranches by image URL.
- `view` tags are heuristic (franchise/genre rules): side-view platform and
  action maps dominate; RPG/strategy overhead maps are "top"; isometric
  titles (Landstalker, Light Crusader…) are "other", as are Sonic special
  stages.
- `iconic` is a franchise-tier score; `detail` is computed from pixel area /
  long-edge sweet spot, capped down for sprawling multi-screen composites
  (>6.5 MP) so they don't masquerade as high-detail.
- Selection protected breadth deliberately: per-platform quotas
  (Genesis 215 + 20 flex, MS 90, GG 45, CD 30) and staged per-game caps
  (4 → 8 → 14 for giant franchises), so the pool is not just the Sonic show.
