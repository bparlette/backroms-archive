# Back Roms catalog enrichment RE-PASS — report

**Scope:** all 1,000 worlds in `game_worlds_extracted.json`, re-passed in strict ID
order from #1 (the 39 already-generated worlds, ids 1–39, included), per Cherie's
2026-11-01 directive. Baseline: repo `bparlette/worlds` main @ `c987e8e0`
(catalog blob SHA `cfbd34ca72f102ea77a188945e63d0ce2638d02a`, verified after
download). Method: the shipped v2 extractor's own functions
(`scrape_world_v2` / `collect_images` / `build_brief` / `build_prompt` from
`extract_worlds.py` @ main, blob `aef58169…`), driven per-world with audit
guards — no new extraction logic invented. **Nothing was pushed to GitHub.**
Output catalog: `game_worlds_extracted.json` in this directory.

**Prefix statement: COMPLETE through #1000 of 1,000.** Every world was
processed (checkpointed to disk after each batch of 25); entry order and ids
are unchanged (verified by diff against the baseline).

## Counts before → after

| metric | before | after |
|---|---|---|
| worlds with a good primary image | 197 | 298 |
| worlds with an image set | 196 | 298 |
| worlds with a layout+palette pair | 12 | 14 |
| primary is a map | 21 | 29 |
| primary is a screenshot | 176 | 269 |
| briefs: real place text (v2 standard) | 583 | 583 |
| briefs: templated fallback (v2 standard) | 382 | 417 |
| briefs: defective (junk/dump/truncated) | 35 | 0 |
| worlds still imageless | 803 | 702 |

## Briefs

**Tier 1 — defective briefs re-derived: 35 worlds.**
Ids: 136, 138, 156, 158, 168, 176, 243, 250, 251, 265, 291, 320, 344, 391, 394, 437, 505, 559, 560, 568, 569, 570, 584, 594, 649, 659, 664, 674, 679, 690, 734, 745, 788, 795, 1000

30 of the 35 carried literal navigation junk as their entire "place text"
(`"<Game>/Table of Contents"` — the v2 paragraph filter leaks this string from
stub game articles whose only qualifying paragraph is the subpage index; the
rest were meta/index text, e.g. "Encounter this track in Levels: 1, 3, 9, 20,
and 23", and two game-article reception dumps). Each was re-derived with
`scrape_world_v2`; the re-derived text was audit-checked before adoption, and
where it was still defective (in all 35 cases the source pages hold no usable
place prose) the entry received the compliant templated fallback instead of
the junk. Net effect: defective briefs 35 → 0; no Tier-1 world yielded real
place text — that is a property of those wiki pages, not of the driver
(verified by hand on #136/#250/#505 during smoke tests).

**Tier 2 — fallback briefs upgrade-attempted: 382 worlds, 0 upgraded.**
Every templated-fallback brief was re-run through full v2 resolution +
extraction, with an upgrade accepted only if the new brief was audit-clean
real place text from a page plausibly belonging to the game. None passed.
Spot checks (#36 A Link to the Past, #43 Donkey Kong Country 2, #146 Donkey
Kong Country 3) show why: resolution lands on the game article and
`extract_place_text` returns zero qualifying paragraphs (hub-style articles
whose content lives in tables, lists, and subpage links). This residue is
what the v2 method cannot reach; the earlier enrichment passes had already
taken everything it can. These 382 briefs remain the compliant templated
fallback — the class that measured 45% verified vs 23% for long dumps.

Briefs with real text that merely *contain* some game-level prose (reception,
release history) were deliberately left untouched: they pass the v2 audit
(length, no meta/imperative language, whole sentences), and re-running the
identical filter over the identical pages reproduces materially the same
brief. (Aggressive "no spatial word" classifiers false-positive on verified
worlds — e.g. #12 Zelda — so they were not used as a re-derive trigger.)

## Images

**Fills: 111 previously-imageless worlds received image sets**
via `collect_images` on the stored place page (v2 enrich-images semantics).
2 of the retained fills arrived as ready layout+palette pairs
(ids: 187, 807); primary maps rose
21 → 29 (e.g. #240/#572 The Guardian Legend area maps,
#514 Blaster Master Area 1 map).
Retained fill ids (101): 8, 16, 29, 31, 98, 101, 102, 103, 104, 106, 110, 111, 113, 115, 122, 131, 132, 133, 135, 140, 187, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201, 221, 222, 223, 232, 233, 240, 241, 247, 260, 272, 273, 274, 276, 360, 423, 466, 467, 469, 489, 497, 514, 540, 543, 550, 553, 572, 573, 574, 579, 589, 592, 598, 801, 802, 803, 804, 806, 807, 810, 812, 813, 814, 815, 816, 818, 821, 824, 827, 830, 831, 832, 836, 838, 839, 860, 862, 863, 864, 865, 868, 871, 872, 874, 877, 878, 880, 881, 884, 984, 996

**Pair completions for lone screenshots: 0 new.** All lone-screenshot worlds
were re-run through `collect_images`; in no case did the game/walkthrough
pages yield an additional map candidate (traced by hand for #12 — the
Underworld place page's own images are all icons/sprites the junk filter
correctly rejects — and #13). The 12 pre-existing pairs were already what
this method can find.

**Existing images: zero removed, zero replaced.** Every pre-existing primary
was re-validated: 0 filename-junk primaries, 0 dead URLs (404/410 confirmed
by GET) among all pre-existing set members. One set was normalized: #744 had
a primary with no `image_urls` array; the array was rebuilt from the primary
(no URL changed). Diff-verified: no baseline image URL disappeared without a
recorded reason (there were none).

**Post-pass removals (my own fills, quality review): 10.** The
filename classifier cannot distinguish a handful of arcade-hardware/HUD
photos whose names carry no skip-list words. These fills are not in-game
screenshots or maps, so they were removed (worlds returned to imageless and
added to the VGMaps target list below):
- #9: https://cdn.wikimg.net/en/strategywiki/images/0/02/Warlords_cocktail_cabinet.jpg
- #94: https://cdn.wikimg.net/en/strategywiki/images/7/79/R-Type_ARC_control_panel.jpg
- #99: https://cdn.wikimg.net/en/strategywiki/images/8/82/Battlezone_arcade_front.jpg
- #123: https://cdn.wikimg.net/en/strategywiki/images/5/53/Gradius_II_FC_power_meter.png
- #236: https://cdn.wikimg.net/en/strategywiki/images/0/0f/Ikari_Warriors_cpanel.jpg
- #585: https://cdn.wikimg.net/en/strategywiki/images/0/0f/Ikari_Warriors_cpanel.jpg
- #591: https://cdn.wikimg.net/en/strategywiki/images/5/53/Gradius_II_FC_power_meter.png
- #826: https://cdn.wikimg.net/en/strategywiki/images/9/99/Pac-Mania_cabinet.jpg
- #861: https://cdn.wikimg.net/en/strategywiki/images/0/02/Warlords_cocktail_cabinet.jpg
- #867: https://cdn.wikimg.net/en/strategywiki/images/8/82/Battlezone_arcade_front.jpg

**Sample verification:** 20 image URLs newly set by this pass, chosen at
random (seed 20261101): **20/20 returned HTTP 200 with an
image/* content type.** (3 of the 20 were among the hardware/HUD photos
above — they resolve fine as images; suitability, not liveness, was the
issue — and they were removed.)

**Known classifier limit (unchanged from shipped v2):** image kind is chosen
by filename. A game-article lead image whose filename is just the game's name
(e.g. #505's fill) may in reality be box art; filenames alone cannot settle
it. Flagged here rather than silently re-filtered with invented rules.

## Worlds still imageless after this pass — 702 (the VGMaps merge target list)

1, 2, 3, 4, 5, 6, 7, 9, 15, 17, 18, 20, 23, 28, 32, 33, 35, 36
40, 42, 43, 44, 45, 46, 47, 48, 49, 54, 55, 56, 58, 59, 60, 65, 66, 67
68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87
91, 94, 95, 97, 99, 100, 107, 108, 109, 112, 114, 116, 118, 123, 124, 125, 127, 128
130, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 148, 149, 150, 151, 152, 153, 154
156, 157, 158, 160, 161, 162, 163, 164, 165, 167, 168, 170, 173, 174, 175, 176, 177, 178
179, 180, 181, 182, 183, 184, 185, 188, 189, 190, 202, 203, 204, 205, 206, 207, 208, 209
210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 224, 225, 226, 227, 228, 229, 230
231, 234, 235, 236, 237, 238, 242, 243, 244, 249, 250, 252, 253, 254, 255, 256, 257, 258
259, 261, 262, 263, 264, 265, 266, 268, 269, 270, 271, 277, 278, 279, 280, 281, 282, 283
284, 285, 286, 287, 288, 291, 292, 293, 294, 295, 296, 298, 299, 300, 301, 302, 303, 304
306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323
324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341
342, 343, 344, 345, 346, 347, 349, 350, 351, 352, 353, 355, 356, 357, 358, 359, 361, 362
363, 364, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 382, 383
386, 387, 388, 390, 391, 392, 393, 394, 395, 397, 398, 402, 404, 405, 406, 407, 408, 409
410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 425, 426, 427, 430, 431, 432
433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 449, 450, 451
453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 468, 471, 472, 473, 474
475, 476, 477, 478, 479, 480, 481, 482, 483, 485, 486, 488, 492, 493, 494, 495, 496, 498
499, 500, 501, 502, 503, 504, 509, 512, 513, 515, 516, 519, 520, 523, 524, 525, 526, 529
530, 531, 535, 537, 538, 541, 542, 545, 547, 549, 552, 554, 555, 556, 557, 558, 559, 560
561, 562, 563, 564, 565, 567, 568, 571, 578, 580, 581, 582, 583, 584, 585, 586, 587, 591
593, 594, 595, 600, 602, 604, 606, 607, 608, 610, 612, 613, 614, 616, 619, 620, 621, 622
623, 624, 625, 627, 628, 629, 630, 632, 633, 634, 639, 640, 644, 645, 646, 647, 648, 649
650, 651, 652, 653, 654, 655, 657, 658, 660, 661, 663, 665, 666, 667, 669, 670, 671, 673
674, 675, 676, 677, 679, 681, 682, 683, 684, 685, 686, 687, 689, 690, 691, 692, 693, 695
696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713
714, 715, 717, 718, 719, 720, 721, 722, 723, 724, 725, 727, 728, 729, 730, 731, 733, 734
735, 736, 737, 738, 739, 740, 742, 743, 745, 746, 749, 750, 752, 754, 757, 758, 759, 760
761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778
779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796
797, 798, 799, 800, 805, 808, 825, 826, 835, 843, 844, 849, 850, 851, 852, 854, 855, 856
857, 858, 859, 861, 867, 869, 870, 873, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894
895, 896, 897, 898, 899, 900, 901, 903, 908, 912, 913, 915, 916, 917, 918, 919, 920, 921
922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939
940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957
958, 959, 961, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977
978, 979, 980, 981, 982, 983, 987, 989, 990, 991, 992, 993, 994, 995, 997, 998, 999, 1000

## World classes where the wiki simply has nothing usable

- **Early arcade / Atari-2600-era stubs:** game articles are near-empty hubs;
  their only images are cabinet/control-panel photos (removed above) — no
  in-game screenshots exist on the wiki for many of these.
- **Hub-style game articles** (much of the SNES/Genesis platformer tail):
  zero qualifying prose paragraphs and image galleries made of icons/sprites
  that the junk filter rejects by design.
- **Place pages that exist but carry no maps:** dungeon/area pages illustrate
  with item and boss imagery (skip-listed), and their maps, when the wiki has
  them, sit on walkthrough pages under filenames the map-word classifier
  doesn't always recognize.
- **Spec quirk (pre-existing):** #251/#569/#570 have the game name split
  across fields (`game="R.C. Pro"`, target beginning `"Am - …"` /
  `"Am II - …"`). Resolution still found `R.C. Pro-Am/Tracks`; noted for the
  catalog maintainers, not changed here.

## For the VGMaps matcher re-run: canonical single-area candidates

The VGMaps lane reported 281 worlds "game covered, target area not
identifiable", 186 of them with compound or purely descriptive targets.
(My punctuation rule — target contains `&`, `,`, or ` and ` — selects 188;
the 2-world difference is definitional.) For those worlds, a candidate
canonical single-area name is recorded below **only where my place-page
research makes it obvious**. No catalog fields were renamed.

Result: **9 candidates out of 188.** The scarcity is structural:
only 15 of the 188 worlds resolved to any wiki subpage at all — resolution
lands on the game article, and neither the article nor the brief singles out
one stage from a compound description. In the 9 cases below, the world's
brief place text names exactly one component of the compound target:

| id | game | current target | candidate canonical target | basis |
|---|---|---|---|---|
| 331 | The Lost Vikings | Egyptian Pyramids & Cyber-Ship Hulls | **Egyptian Pyramids** | only component named in brief place text |
| 378 | Herzog Zwei | Top-Down Island Base Outposts & Runways | **Runways** | only component named in brief place text |
| 435 | Violent Storm | Post-Apocalyptic Downtown & Smelting Foundry | **Smelting Foundry** | only component named in brief place text |
| 514 | Blaster Master | Subterranean Moss Caves & Top-Down Crypts | **Subterranean Moss Caves** | only component named in brief place text |
| 591 | Gradius II | Solar Prominences & Organic Bio-Platforms | **Solar Prominences** | only component named in brief place text |
| 700 | Ranger X | Ravaged Cyber-Settlements & Jungle Bases | **Jungle Bases** | only component named in brief place text |
| 826 | Pac-Mania | Isometric 3D Lego-Style Block Mazes & Block Towns | **Block Towns** | only component named in brief place text |
| 882 | The Empire Strikes Back (Atari 1985) | 3D Vector Hoth Ice Flats & AT-ATs | **3D Vector Hoth Ice Flats** | only component named in brief place text |
| 989 | The Ninja Warriors (Arcade) | Triple-Screen Invaded City Boulevards & Capitol Stairs | **Capitol Stairs** | only component named in brief place text |

For the remaining 179, no honest candidate exists from the
wiki side — the canonical name will have to come from the VGMaps side (their
map filenames) in the re-run. Fused two-stage targets without punctuation
(e.g. #17 Contra "Jungle Waterfall") sit outside the 186 by the lane's own
count and likewise got no candidate: resolution lands on the game article
and the brief covers the game generally.

## Files in this directory

- `game_worlds_extracted.json` — the re-passed catalog (deliverable).
- `catalog_origin.json` — pristine baseline @ c987e8e0 (SHA-verified).
- `extract_worlds.py` — the shipped v2 extractor @ main (SHA-verified copy used).
- `repass.py`, `audit.py`, `analyze.py`, `build_report.py` — driver + audit code.
- `actions.jsonl` — per-world action log (1,000 lines); `adjustments.jsonl` —
  the 10 post-pass removals; `state.json` — processed set;
  `sample_verification.json` — the 20-URL sample detail;
  `canonical_candidates.json` — machine-readable candidate list;
  `audit_baseline.json` — baseline audit detail.
