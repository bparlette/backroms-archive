# MANIFEST — backroms-archive

Every file staged for the `backroms-archive` repo, with byte size and provenance.
Snapshot date: **November 1, 2026**. Catalog-v1 source: `bparlette/worlds` main @ `d1823670c11493028d74983643f6cad7e3586634`.

- **Files:** 31 (plus this manifest)
- **Total size:** 17,650,245 bytes (16.83 MiB), excluding this manifest
- **Extensions present:** `.html` x1, `.json` x12, `.md` x14, `.py` x4
- **Binary check: PASS** — no `.png/.jpg/.jpeg/.gif/.webp/.mp4/.glb/.woff/.woff2/.ttf` or any other binary files are staged; images are referenced by source URL only.
- **JSON check: PASS — every staged .json parses** (12 JSON files checked)

| File | Bytes | Provenance |
|---|---:|---|
| `README.md` | 2,592 | Archive overview — written for this archive (Nov 1, 2026). |
| `catalog-v1/BACKROMS-IDEAS.md` | 7,106 | Back Roms decisions record — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/PIPELINE-PROMPT-BLOCK.md` | 1,953 | Generator prompt block — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/SNAPSHOT.md` | 2,703 | Snapshot record — written for this archive; tip SHA + blob verification of the files below. |
| `catalog-v1/WALKER-PIPELINE-ADD.md` | 9,383 | Walker pipeline spec R1–R9 — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/game_worlds_extracted.json` | 1,980,151 | The v1 1,000-world catalog — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/generation_progress.json` | 9,809 | Generation/verification state (16 of 39 verified) — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/index.html` | 1,358,754 | Gallery page as of the snapshot — bparlette/worlds @ d1823670, repo root (blob-verified). |
| `catalog-v1/worlds.json` | 1,308 | Walker manifest — bparlette/worlds @ d1823670, walk/worlds.json (blob-verified). |
| `curation/POOL-A.md` | 5,868 | Tranche A report — map-first curation, Nov 1, 2026. |
| `curation/POOL-B.md` | 3,997 | Tranche B report — map-first curation, Nov 1, 2026. |
| `curation/POOL-C.md` | 5,934 | Tranche C report — map-first curation, Nov 1, 2026. |
| `curation/POOL-D.md` | 5,431 | Tranche D report — map-first curation, Nov 1, 2026. |
| `curation/README.md` | 2,111 | Curation scope note (what was left out and why) — written for this archive. |
| `curation/REPORT.md` | 10,033 | Merge report: how 1,709 candidates were pared to the new 1,000 — Nov 1, 2026. |
| `curation/bench.json` | 37,553 | The bench: next 100 ranked alternates behind the new 1,000 — Nov 1, 2026. |
| `curation/build_catalog.py` | 2,310 | Catalog builder (selected 1,000 -> proposed_catalog.json) — map-first curation tooling. |
| `curation/merge.py` | 4,462 | Merge script (pool union + dedupe) — map-first curation tooling. |
| `curation/pool-a.json` | 215,781 | Tranche A pool: 600 ranked VGMaps candidates (NES 300 + SNES 300) — map-first curation, Nov 1, 2026. |
| `curation/pool-b.json` | 151,191 | Tranche B pool: 400 ranked Sega-family candidates — map-first curation, Nov 1, 2026. |
| `curation/pool-c.json` | 152,957 | Tranche C pool: 406 ranked candidates (GB/GBC/GBA, arcade, Atari, all remaining platforms) — Nov 1, 2026. |
| `curation/pool-d.json` | 113,833 | Tranche D pool: 303 ranked candidates (re-judged prior maps + nesmaps/RPG sources) — Nov 1, 2026. |
| `curation/pool.json` | 8,496,238 | Combined bar-passer pool: 18,183 entries across all platforms, retained for reuse — Nov 1, 2026. |
| `curation/proposed_catalog.json` | 941,799 | The merged map-first catalog: the new 1,000 worlds selected from the four pools — Nov 1, 2026. |
| `curation/select.py` | 6,431 | Selection script (caps, breadth, view-band) — map-first curation tooling. |
| `curation/verify_merge.py` | 3,543 | Merge verifier (integrity + URL spot checks) — map-first curation tooling. |
| `research/alt-sources/REPORT.md` | 21,467 | Alt-sources scout report (15 sources fetch-verified) — Nov 1, 2026. |
| `research/enrich-repass/REPORT.md` | 14,947 | Enrichment re-pass report — Nov 1, 2026. |
| `research/enrich-repass/catalog_origin.json` | 1,979,860 | Enrichment re-pass catalog output (images 197 -> 298; 35 defective briefs fixed) — Nov 1, 2026. |
| `research/vgmaps-apply/APPLY-REPORT.md` | 39,881 | VGMaps apply report — vgmaps-apply pass, Nov 1, 2026. |
| `research/vgmaps-apply/merged_catalog.json` | 2,060,859 | v1 catalog after the approved VGMaps apply (map primaries 29 -> 313) — vgmaps-apply pass, Nov 1, 2026. |
| `MANIFEST.md` | (this file) | This manifest — generated at staging time, Nov 1, 2026. |

## Split files (connector per-file limit ~1.13 MB)

These files exceeded the GitHub connector per-file limit and are stored as sequential byte chunks. Reassemble with `cat <file>.part01 <file>.part02 ... > <file>` — byte-identical to the original (SHA-256 given).

- `catalog-v1/index.html` — 1358754 bytes — sha256 `ee03f5c910b04503c87d19b7672ec15b8a9d0b27462493a4791422699310a38d` — parts: `catalog-v1/index.html.part01`, `catalog-v1/index.html.part02`
- `catalog-v1/game_worlds_extracted.json` — 1980151 bytes — sha256 `4692d6029984a60327b71461fcf3a1e8a7db5e6e47d55c744d3d1439139c0976` — parts: `catalog-v1/game_worlds_extracted.json.part01`, `catalog-v1/game_worlds_extracted.json.part02`
- `curation/pool.json` — 8496238 bytes — sha256 `9fb34f5ca8113d9fde8c757235527e9b18054832a52608a6d4d89057c1ffd281` — parts: `curation/pool.json.part01`, `curation/pool.json.part02`, `curation/pool.json.part03`, `curation/pool.json.part04`, `curation/pool.json.part05`, `curation/pool.json.part06`, `curation/pool.json.part07`, `curation/pool.json.part08`, `curation/pool.json.part09`
- `research/vgmaps-apply/merged_catalog.json` — 2060859 bytes — sha256 `9488a83a13b424c15976a1f000330791cd473a1be178b5e1f215ac7784c89517` — parts: `research/vgmaps-apply/merged_catalog.json.part01`, `research/vgmaps-apply/merged_catalog.json.part02`, `research/vgmaps-apply/merged_catalog.json.part03`
- `research/enrich-repass/catalog_origin.json` — 1979860 bytes — sha256 `b102c66c187b672fccbba3fa9d8184feacce81614417f2e40d77f15b9c6b2cdf` — parts: `research/enrich-repass/catalog_origin.json.part01`, `research/enrich-repass/catalog_origin.json.part02`
