# catalog-v1 — Snapshot Record

- **Source repo:** bparlette/worlds (live project — this archive is a frozen copy, not the working tree)
- **Source commit (main tip at snapshot time):** `d1823670c11493028d74983643f6cad7e3586634`
- **Commit date:** 2026-11-01 14:53:28 UTC (Nov 1, 2026, ~9:53 AM ET)
- **Snapshot taken:** November 1, 2026
- **Verification:** every file below was downloaded from that pinned commit and its git blob SHA-1 was checked against the commit's tree — all match.

## Files

| Archived file | Path in live repo at tip | Bytes | Blob SHA-1 |
|---|---|---|---|
| `game_worlds_extracted.json` | `game_worlds_extracted.json` | 1,980,151 | `70a5dcefbe1f1af1b3d0790f3318971c60eb531c` |
| `index.html` | `index.html` | 1,358,754 | `e72cd602b401ad529f63dd7634febdd41af07848` |
| `worlds.json` | `walk/worlds.json` | 1,308 | `ac529515115cebb9d68e3a2d5553f2c6da47e85c` |
| `generation_progress.json` | `generation_progress.json` | 9,809 | `079e441fc9f12a1eabc57dd0c0d16fea5131fd5a` |
| `WALKER-PIPELINE-ADD.md` | `WALKER-PIPELINE-ADD.md` | 9,383 | `3283f5455653716b6317936634cb215d488164e3` |
| `PIPELINE-PROMPT-BLOCK.md` | `PIPELINE-PROMPT-BLOCK.md` | 1,953 | `03f1959a7af6168cff42692e7695a538b65cb597` |
| `BACKROMS-IDEAS.md` | `BACKROMS-IDEAS.md` | 7,106 | `6a42b8b8ad57cf641119fb72c18c9b2bab81e7cf` |

## Naming notes

- The v1 catalog has **no file literally named `catalog.json`** in the live repo — the catalog is `game_worlds_extracted.json`, and it is archived under its real name.
- There is likewise **no root `worlds.json`**; the walker manifest lives at `walk/worlds.json` and is archived here as `worlds.json`.
- `generation_progress.json` is generation state, not catalog data; it is included because it records the verified-progress state at snapshot time.

## State at snapshot

- **Verified progress: 16 of 39 generated scenes** (007 Mountain King was the 16th, flipped to verified in this very commit).
- Walkable in the World Walker at snapshot time: worlds 001–005, 007, 011, 019, 020.
- The catalog at this tip already includes the morning's updates for worlds 001–010 (enrichment + VGMaps images); worlds 011+ are unchanged from the prior main. This is the last state of the v1 catalog before the map-first catalog swap.

## Not archived

- **`walk/thumbs/*.png` (baked top-down thumbnails) are binary and intentionally not archived** — they live in the live repo's git history at this commit, and the GitHub connector path used for this archive corrupts binaries.
- Scene HTML files (`scenes/`) likewise remain in the live repo's history at this commit; this archive preserves the catalog, gallery, manifest, progress, and spec docs that define them.
