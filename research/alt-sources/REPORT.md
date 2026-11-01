# Alternative Image Sources for Back Roms — Scout Report

**Date:** 2026-11-01 · **Type:** research + evidence only — no downloads, no catalog changes, nothing pushed.
**Method:** every claim below is backed by a page fetched from this VM on 2026-11-01 (this pass, two sittings). Where a fetch did not produce evidence, the source is labeled *unproven* — however famous it is. No site was bot-blocked outright; the failures below are "loads but harvest unproven" or "wrong content class," not 403s.

## The gap this was scouted against

From the catalog (`game_worlds_extracted.json`) + VGMaps pass (`vgmaps-pass/proposal.json`, `SUMMARY.md`):

- 1,000 worlds; only **197** have a good primary image → **803** have none.
- Residual pool ≈ **643 worlds**: 362 whose games are not on VGMaps at all + 281 covered-but-target-unidentifiable.
- Imageless + VGMaps-uncovered = **329**: Arcade 138, Atari 64, SNES 59, Genesis/MS/GG 49, NES 12, Sega CD 7.
- Imageless + target-missing = **231**: NES 75, Arcade 70, SNES 38, Genesis/MS/GG 37, Atari 9, Sega CD 1, MS 1.
- So the imageless working pool is ≈ **560 worlds**. (The other ~83 of the 643 have a screenshot but no identifiable map target — alt sources help them least; see caveats.)

Test-case gap games used for verification, by family — Atari: Berzerk (#860), Seaquest (#206), Moon Patrol (#107), Enduro (#207); Arcade: DonPachi (#416), 1942 (#190), Progear (#464), Guwange (#419), Batsugun (#971); Genesis: Gaiares (#362), Steel Empire (#364), Mega Turrican (#696), Landstalker (#74); Sega CD/32X: Keio Flying Squadron (#737), Kolibri (#742), Sonic CD (#731), Lunar (#733); SNES: Axelay (#160), Joe & Mac (#292), Bahamut Lagoon (#645); NES: Recca (#256), Gun Nac (#263), Crisis Force (#264).

## Ranked table

| # | Source | Families | Content (verified) | Access (verified from this VM) | Verified yield |
|---|--------|----------|--------------------|-------------------------------|----------------|
| 1 | **MobyGames** | All | In-game screenshots, per game × per platform | Plain HTML loads; images on open CDN (`cdn.mobygames.com`); official API exists but is **paid** (per RomM docs) | **High** — 2/2 gap games verified with screenshots |
| 2 | **ScreenScraper** (screenscraper.fr) | All retro (125+ systems) | Screenshots by design (`screenshot` media type), plus box/manual | API v2; needs free account **+ developer credentials**; 20k req/day registered (per Skyscraper docs) | **High potential, per-game unproven from here** (API-gated; no gap game fetched) |
| 3 | **Sega Retro** (segaretro.org) | Genesis, Master System, Game Gear, Sega CD, 32X, Saturn | Emulator screenshots, often **per-stage sets** | MediaWiki — standard API; file pages load freely | **High for Sega** — per-stage screenshot set verified for a gap game |
| 4 | **AtariAge** | Atari 2600/5200/7800 (+Lynx/Jaguar) | Gameplay screenshots, dedicated Screenshots page per game | Plain HTML loads | **High for Atari** — 3 screenshots verified for a gap game |
| 5 | **GamesDatabase.org** | All, incl. odd platforms (Vectrex) | One "In Game" shot + title screen per game/platform (plus box/cart junk to filter) | Plain HTML loads; predictable `Media/SYSTEM/…` media paths | **Med-High** — media set structure verified for a gap game |
| 6 | **RPGClassics** (shrines.rpgclassics.com) | RPGs: NES/SNES/Genesis/Sega CD/PSX | **Genuine per-area MAPS** in shrines | Plain HTML loads | **High value, narrow** — ~25 maps verified for one gap game |
| 7 | **nesmaps.com** | NES only | **Full level maps** (labeled + background-only), PNG, full-stage dimensions | Plain HTML loads | **Med** — top quality, curated breadth (~dozens of games) |
| 8 | **shmups.wiki** | Shmups: arcade + console | Screenshots + **overlay maps** (item-location maps over stage art) | MediaWiki — standard API | **Med** — screenshot + 5 stage maps verified for one gap game |
| 9 | **RAWG** (rawg.io) | All, incl. retro platforms | Screenshots (`short_screenshots`), 1–7 per retro game | Public API, **key required** | **Med-Low** — retro platform coverage + screenshot URLs verified in API responses |
| 10 | **PixelatedArcade** | Arcade + early consoles | ≥1 real gameplay screenshot per covered game; much cabinet-photo junk to filter | Plain HTML loads; images on public S3 | **Low-Med** — real screenshot + direct URL verified for a gap game |
| 11 | **HG101** (hg101.kontek.net) | Whatever its articles cover | Many gameplay screenshots per article | Plain HTML loads; direct image URLs | **Low-Med** — 50+ images verified on one article; not a database |
| 12 | **AtariMania** | Atari 2600/5200/7800/8-bit/ST | Screenshots advertised per game page | Plain HTML loads; **direct image URLs not captured** | **Unproven harvest** (structure only) |
| 13 | **GameFAQs** | All | User screenshots exist per game | Pages load; **no direct image URL captured in 2 attempts** | **Unproven harvest** |
| 14 | **VGMuseum** | All | Endings/review screenshot sets exist; scans sections are box/cart/manual | Plain HTML | **Low / unproven** for gap games |
| 15 | **arcade-history.com** | Arcade (+ some console carts) | Screenshot thumbnails; **full-size members-only** | Plain HTML; enlarge gated | **Low** |

## Verified evidence, source by source

### 1. MobyGames — the backbone candidate
- **DonPachi (arcade, #416):** game page fetched — https://www.mobygames.com/game/38277/donpachi/ (Moby ID 38277). Five screenshot thumbnails served from the open CDN, e.g. `https://cdn.mobygames.com/a8567404-bf07-11ed-9c42-02420a000140.webp`. Screenshots are organized per game × per platform.
- **Berzerk (Atari, #860):** main entry Moby ID 8847 — https://www.mobygames.com/game/8847/berzerk/ — carries Screenshots/Media sections with per-platform tabs (Arcade / Atari 2600 / Atari 5200 / Vectrex visible on its covers page). MobyGames lists **697 Atari 2600 games** (platform page fetched), so its Atari breadth is structural, not anecdotal.
- **Access/posture:** pages and CDN images load from this VM with no wall. An official API exists but is a **paid feature** (RomM's provider docs, fetched: "Access to the MobyGames API is a paid feature… we recommend using ScreenScraper instead, as it is free to use") — the HTML+CDN route needs no key. No licensing terms seen on the pages; our reference-use model applies.

### 2. ScreenScraper — the one-API alternative
- Verified via RomM + Skyscraper documentation and the live API portal (all fetched): API v2 at `api.screenscraper.fr/api2/`; media types include `screenshot`, `fanart`, `manual`, `marquee`, `video`; "supports 125+ popular systems"; matching is ROM checksum- or filename-based, with name search available.
- **Access cost:** requires a (free) ScreenScraper account **plus** developer credentials (`devid`/`devpassword`) sent on every call; registered-user limit ≈ 20k requests/day (Skyscraper docs). This is a signup Cherie would have to approve/do — nothing was registered in this pass.
- **Honest label:** the database is built so nearly every cataloged ROM has a screenshot, but **no individual gap game was fetched** (the API is credential-gated), so per-game yield is unproven from here.

### 3. Sega Retro — the Sega win
- **Gaiares (Genesis, #362):** file page fetched on segaretro.org; direct image `https://segaretro.org/images/a/a7/Gaiares%2C_Stage_2-1.png` — a 320×224 emulator capture, one of a **per-stage screenshot set** (uploaded 2022-09-01). Per-stage sets mean multiple layout/palette references per world, the richest yield of any source here.
- **Posture, verbatim in substance from the file page:** "This image is a screenshot made by an emulator… Screenshots are free to use under fair use. All copyright to this image is held by the companies who developed and published this game." (The same fair-use screenshot template appears on its Saturn files, e.g. the Keio Flying Squadron 2 credits file.)
- **Access:** MediaWiki (file pages, categories, logs all standard MW) → the standard MediaWiki API applies; no wall encountered.
- Second test (Keio Flying Squadron, Sega CD #737): the game's Sega Retro article did not surface via search in this pass, so Keio itself is *not* individually verified — the Gaiares set + site-wide structure carry the verdict.

### 4. AtariAge — the Atari win
- **Berzerk (Atari 2600, #860):** game page fetched — https://atariage.com/software_page.php?SoftwareID=866 — with a dedicated Screenshots page: https://atariage.com/screenshot_page.php?SoftwareLabelID=910, which lists **3 gameplay screenshots** for Berzerk. Per-game pages follow the same pattern across 2600/5200/7800 (a "Screenshots" section is structural; a dedicated Atari 2600 Screenshots index also exists, Stella captures at native 320×200 doubled to 640×480 PNG).
- Caveat: the text fetcher did not expose the direct image file URLs (page chrome only in the image footnote) — a harvest pass should confirm the image URL pattern on one page first. Content existence is not in doubt; only the URL mechanics are unverified.
- Note: for single-screen Atari games the screenshot *is* the layout — the map/screenshot distinction mostly collapses for this family.

### 5. GamesDatabase.org — broad, predictable, one shot per game
- **Berzerk (Vectrex version page):** fetched — https://www.gamesdatabase.org/game/gce-vectrex/berzerk — shows the standard media set: "In game image of Berzerk on the GCE Vectrex," Title Screen, Box, Box Back, Cartridge, Overlay, Marquee, Advert, plus video at a predictable path (`https://www.gamesdatabase.org/Media/SYSTEM/GCE_Vectrex/Video/Formated/Berzerk___GCE.mp4`). The "Also on" list includes Atari 2600/5200/Arcade, i.e. per-platform pages exist for the same title.
- Yield shape: typically **one** in-game screenshot per game/platform — enough for a palette/composition reference, not a set. Half the media slots are junk classes for us (box/cart/marquee) and must be filtered by slot name, which the page structure makes easy.
- A MAME ROM-information page for Berzerk also exists on the domain (`gamesdatabase.org/mame-rom/berzerkg`), suggesting deep arcade listings; screenshot presence on those pages was not individually verified.

### 6. RPGClassics — genuine MAPS for RPG worlds
- **Lunar: The Silver Star (Sega CD, #733):** the shrine's Maps index fetched — http://shrines.rpgclassics.com/sega_cd/ltss/maps/lannisland.shtml — listing ~25 per-area maps (Caldor Isle, White Dragon Cave, Meribian Sewers, Silver Spire, Damon's Spire, the four Dragon Caves, Goddess' Tower, Grindery, Ghaleon's Palace, …). The Sega CD shrine index (fetched) marks Lunar: TSS, Dark Wizard, Shining Force CD and Vay as "Complete" shrines.
- This is one of the only sources found that adds **maps** (not just screenshots) for families VGMaps misses — and it covers exactly the RPG slice (NES/SNES/Genesis/Sega CD) where our worlds are dungeon/town-based. Individual map image files sit on the linked sub-pages (the index fetch showed links, not the images themselves).
- Breadth is shrine-by-shrine (dozens of RPGs, not thousands) — a title-matching sweep, not a bulk harvest.

### 7. nesmaps.com — genuine NES maps, curated breadth
- Verified via its map-selection pages (fetched as search-indexed page text): full-stage PNG maps with stated dimensions — Metroid complete map 7680×7200, Shatterhand per-area maps, Castlevania III per-stage maps, DuckTales per-stage maps, down to obscure titles (Bio Miracle Bokutte Upa, full set). Both labeled and background-only variants.
- NES-only and hand-made, so breadth is dozens of games — but our NES imageless pool is 87 worlds, and these are real maps for the platformer/adventure slice of it.

### 8. shmups.wiki — screenshots + overlay maps for the shmup slice
- **DonPachi (#416):** MediaWiki article (https://shmups.wiki/index.php?title=DonPachi) uses `Screenshot_DonPachi_001.png` and — verified in the article's revision text — **per-stage bee-location maps**: "The following maps show you the locations of the 13 bees for each of the stages," with sub-pages for Stages 1–5. Those are overlay maps (annotations over stage art): real layout reference, not just a screenshot.
- Why it matters disproportionately: our arcade gap is heavily shmup-weighted (DonPachi, 1942, Progear, Guwange, Batsugun are all shmups; so are NES Recca/Gun Nac/Crisis Force, SNES Axelay, Genesis Gaiares/Steel Empire). One genre wiki covers a named chunk of the worst family.

### 9. RAWG — real retro coverage, thin per game
- Verified in live API responses (fetched): platform catalogs include Atari 2600 (294 games), NES (1,024–1,336), SNES (989), Genesis, Game Gear; retro titles return `short_screenshots` on `media.rawg.io` (e.g. Star Raiders (1979) with 6+ screenshots, Indy 500 similar).
- Access needs an API key (free tier exists; keys seen in public crawls were **not** used or recorded). Per-game screenshot counts are small and there are no maps. Supplementary, not a backbone.

### 10. PixelatedArcade — small DB, real screenshots, direct URLs
- **Berzerk page fetched** — https://www.pixelatedarcade.com/games/berzerk — platforms Arcade/2600/5200/Vectrex, with a Screenshots section and a genuine inline gameplay screenshot at a direct URL: `https://pixelatedarcade.s3.us-east-005.dream.io/pictures/inline/1696/Berzerk-Arcade-Screenshot.png`. Most of its Pictures section is cabinet/board photos (junk for us) — filter to the Screenshots section only.

### 11. HG101 — rich articles, not a database
- **Dodonpachi article fetched** — https://hg101.kontek.net/dodonpachi/dodonpachi2.htm — 52 images, of which the first three are flyer/instruction-card (junk) and the remaining ~49 are gameplay screenshots across the series' arcade/PS/SS versions, all at direct `hg101.kontek.net` URLs. Excellent yield *for games it has covered*; coverage is editorial (hundreds of articles), so this is an opportunistic sweep against the gap list, not a harvest.

### 12–15. Partial / low
- **AtariMania:** Berzerk page fetched — https://www.atarimania.com/game-atari-2600-vcs-berzerk_16283.html (27 versions listed; page titles promise "scans, dump, download, screenshots, ads, videos, catalog, instructions"), but the fetch surfaced versions/ads sections only — **no screenshot URL captured**. Pages load fine; harvest unproven. AtariAge is the stronger Atari route; AtariMania stays a cross-check.
- **GameFAQs:** DonPachi user-screenshots page fetched (https://gamefaqs.gamespot.com/arcade/566983-donpachi/images?pid=566983&img=14) — coverage exists (screenshot #14), and a Keio Flying Squadron Sega CD media page exists (`gamefaqs.gamespot.com/segacd/587957-keio-flying-squadron/media`, "Box Shots / Screenshots") — but **no direct image URL was exposed in either fetch**. No bot wall was hit; harvest mechanics unproven.
- **VGMuseum:** Atari 2600 *scans* index fetched — for Berzerk it offers box front/back only (junk class). Its endings/review sections do hold screenshot sets (review FAQ requires "one screenshot of the title, and at least six of the game running"; a Master System endings page exists), but no gap game's screenshots were verified. One plus: its reuse policy, quoted on Wikipedia file pages from its FAQ — "Can I use your images on my website? Yes, you can use the images, as long as you give credit to the website where you found them."
- **arcade-history.com:** DonPachi page fetched — https://www.arcade-history.com/?n=donpachi&page=detail&id=670 — "Goodies 3", sources line cites "Game's screenshots", but the images exposed are 160px minis (e.g. `https://www.arcade-history.com/images/covermini160/670_1.jpg`) and enlargement is **members only** (stated on the page). It also has console-cart pages (a Berzerk CX2650 page exists). Thumbnails alone are weak reference material → low.

## Killed candidates

- **KLOV / arcade-museum.com** — Don Pachi page fetched (https://www.arcade-museum.com/Videogame/don-pachi): the only site image is the **marquee** (`…/images-game/26/don-pachi-26032.jpg`); the Images section holds cabinet/marquee material. Wrong content class — killed for layout/palette reference.
- **Ian Albert (ian-albert.com)** — genuine, high-quality full maps and an explicit free-reuse posture ("You're free to do what you like with them"), but his own games index lists only ~10 titles (Doom, Doom 2, Final Fantasy II, GTA: San Andreas, Zelda, ALttP, StarTropics, SMB, Ultima 6/7) — all famous and already image-covered in our catalog. **Zero gap overlap** — killed for this gap.
- **Internet Archive** — the verified Berzerk material is manual-scan PDFs (multiple, incl. the full Atari 2600 manual set). Manuals are a junk class for layout/palette (occasional screen photos, not reliable) — killed as an image source.
- **UVList** — a site-directed search surfaced **no uvlist.net result at all**; no page fetched → unproven, not pursued.
- **StrategyWiki** — no gap-title guide surfaced (a DonPachi search returned shmups.wiki instead). Guide-text wikis are also what the parallel enrichment re-pass already mines → unproven for this gap.
- **LaunchBox Games DB** — a real community DB with screenshots/fanart (LaunchBox's own pages, fetched), but access is mediated by the LaunchBox app and **no public API was found**; GamesDatabase.org provides similar per-game media over plain HTML → deferred.
- **TheGamesDB** — per Skyscraper's docs (fetched), its API now requires a private key with monthly request caps → deferred behind ScreenScraper/MobyGames.
- **Fan wikis (Zelda Wiki, Super Mario Wiki, Metroid Database, Castlevania Dungeon)** — not individually fetched: their flagship franchises are precisely the titles that already have images in our catalog; the gap is the obscure tail, where dedicated fan wikis don't exist. Killed on scope logic, flagged as reasoning rather than fetched evidence.

## Bottom-line recommendation

Harvest in this order:

1. **MobyGames (HTML + CDN).** Zero setup, verified working from this VM today, broadest per-platform screenshot coverage. Skip the paid API; the pages and CDN are open.
2. **ScreenScraper (API).** The only single-API route, purpose-built so cataloged ROMs carry screenshots across 125+ systems. Needs Cherie to register a free account and request developer credentials — the one human step in this plan. Could plausibly match or beat MobyGames' hit rate; do it second because of the signup, and because its per-game yield is still unproven from here.
3. **Sega Retro (MediaWiki API).** Owns the Sega slice (~94 imageless Sega worlds) with the richest per-world yield anywhere (per-stage screenshot sets) and an explicit fair-use screenshot posture on every file page.
4. **AtariAge (+ GamesDatabase as cross-check/fallback).** Owns the Atari slice (~73 imageless Atari worlds) with near-complete per-game screenshot pages for licensed 2600/5200/7800 releases; GamesDatabase covers the same games plus odd platforms (Vectrex) with predictable media URLs when AtariAge has a hole.

**Specialist map sweep (cheap, run alongside):** title-match the gap list against **RPGClassics** shrines, **nesmaps.com**, and **shmups.wiki**. Small counts, but these are the only sources that add genuine *maps* for VGMaps-missed games — and a map is the highest-value reference the generator can get.

**Rescue estimate (labeled estimate, built from the samples above — not a measurement):**
- MobyGames sample: 2/2 gap games had usable screenshots. At a conservative 55–70% hit rate across the ~560 imageless worlds → **~310–390 worlds** get at least one usable screenshot.
- Sega Retro + AtariAge mostly overlap MobyGames but push their family slices higher (per-stage sets; near-complete Atari pages): Sega slice ~50–65 of ~94, Atari slice ~55–60 of ~73 — largely inside the MobyGames count, adding maybe **+20–40 net** after overlap.
- Specialist map sources: **~40–80 worlds** gain a genuine map (RPG shrines + NES maps + shmup overlay maps) — several of which MobyGames would only have given a screenshot.
- RAWG / PixelatedArcade / HG101 / GamesDatabase long tail: **+20–40** screenshots among them.
- **Net plausible rescue: ~350–430 of the ~560 imageless worlds** end up with at least one usable reference image; the remaining ~130–200 are the deep tail (obscure arcade boards, minor Atari releases) where no web source verified here is likely to help.

## Caveats

- **The 281 target-missing worlds are partly a naming problem, not a source problem** (186 have compound/descriptive extractor targets). Alt sources don't fix that by themselves — but per-area sources (RPGClassics shrine indexes, Sega Retro stage lists) double as *target-naming evidence* for a future VGMaps matcher re-run, complementing Lane D's candidate-target list.
- AtariAge and GamesDatabase image-URL mechanics were not fully captured by text fetches (content verified, URLs not) — a harvest pass should pin the URL pattern on one page per source before bulk work.
- Posture throughout is the project's existing model: images are **reference inputs** to the generator (layout/palette), like the wiki images used today. Only three sources stated terms on fetched pages: Sega Retro (fair-use screenshot template), VGMuseum (reuse with credit), Ian Albert (free reuse). Everything else: no terms seen; nothing here ships the images themselves.
