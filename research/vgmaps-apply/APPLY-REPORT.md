# VGMaps Apply — Report

**STAGED ONLY — nothing pushed.** Merged catalog: `merged_catalog.json` in this directory. Moth reviews and pushes.

Inputs: base = enrichment re-pass catalog `enrich-repass/game_worlds_extracted.json` (1,000 entries, final); changes = `vgmaps-pass/proposal.json` as approved by Cherie 2026-11-01 (333 records: 204 add / 81 replace-layout / 48 crop; the 3 isometric low-value records excluded). Every proposal record was reconciled against the *current* base before applying, because the re-pass landed after the proposal was built.

## Final counts

| Metric | Before (re-pass base) | After (merged) |
|---|---|---|
| Entries | 1000 | 1000 |
| Worlds with a primary image | 298 | 474 |
| Map as primary | 29 | 313 |
| Screenshot as primary | 269 | 161 |
| Imageless | 702 | 526 |

## Applied

- **Adds applied: 176** — proposal `add` records whose world was still imageless in the re-passed catalog. VGMaps map set as primary (`image_url` + `image_kind: "map"`, singleton `image_urls`/`image_kinds`).
- **Replace-layouts applied: 108** — VGMaps map took the layout slot; the previous screenshot was retained in the set as palette (set order: map first, screenshot second — the catalog's existing convention).
  - 81 were proposed as `replace-layout` and still had a screenshot primary.
  - 27 were proposed as `add` but the re-pass had since filled the world with a screenshot, so they were applied as replace-layouts per the apply rules (recorded here as converted, not as adds):

Converted add → replace-layout world ids: 16, 29, 31, 106, 132, 140, 193, 195, 198, 260, 274, 276, 540, 543, 553, 573, 812, 813, 824, 830, 831, 832, 864, 874, 877, 881, 884

**Total records applied: 284 of 285 add/replace-layout proposals.** Full per-record detail is in `apply_log.json`.

## Superseded by the re-pass (kept existing, not applied)

- **World 810 — Mappy / Multi-Floor Trampoline Mansions, Microphones & Cat Doors** (proposal action: `add`): the re-pass had already filled this world with a map, so the existing primary was kept.
  - Kept (existing): https://cdn.wikimg.net/en/strategywiki/images/1/16/Mappy_Start.png
  - Not applied (VGMaps): https://vgmaps.com/Atlas/Arcade/Mappy-Rounds.png

  Reviewer note: world 810's retained image is `Mappy_Start.png` — the filename suggests a start screen, but the re-pass catalog classifies it `image_kind: "map"`. The apply rule (re-pass map wins) was followed; flagging in case Moth wants this one overridden by hand.

## Skipped / failed

- **URL verification failures: 0.** Every candidate VGMaps URL was re-verified live before being written (see Verification below); none failed, so no record was skipped for that reason.
- No other skips: every add/replace-layout record was either applied or superseded above. Crop and isometric records were handled per instructions (below), not skipped silently.

## Excluded isometric (exactly the 3 flagged not-recommended)

| World | Game | Target | Proposal action | VGMaps URL (not applied) |
|---|---|---|---|---|
| 128 | Snake Rattle 'n' Roll | Isometric Steps | add-low-value | https://vgmaps.com/Atlas/NES/SnakeRattleNRoll-Map.png |
| 567 | Snake Rattle 'n' Roll | Isometric Ice Ramps & Sky Stepping Blocks | add-low-value | https://vgmaps.com/Atlas/NES/SnakeRattleNRoll-Map.png |
| 664 | Light Crusader | Four Elemental Subterranean Dungeon Floors | replace-layout-low-value | https://vgmaps.com/Atlas/Genesis/LightCrusader-World.png |

## Pending crop — NOT applied (48)

These need a download/crop/host pass first; their catalog entries are unchanged. Current state after the re-pass: 31 imageless, 3 map, 14 screenshot. The crop region for each is the `crop_note` text from the proposal, quoted verbatim.

### World 5 — River Raid / Canyon Riverway (Atari 2600, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Atari2600/RiverRaid-Map.png (20160x10392)
- Crop region: CROP: source is a whole-world/composite map ('Map', 20160x10392) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Canyon Riverway' (the named Canyon Riverway area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 12 — The Legend of Zelda / Underworld Dungeons (NES, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/LegendOfZelda-FirstQuest-Hyrule.png (4352x1408)
- Crop region: CROP: source is a whole-world/composite map ('Hyrule', 4352x1408) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Underworld Dungeons' (the named Underworld Dungeons area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 13 — Zelda II: The Adventure of Link / Palace Temples (NES, confidence low, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/ZeldaII-AdventureOfLink-GreatPalace.png (13824x3360)
- Crop region: CROP: source is a whole-world/composite map ('Great Palace', 13824x3360) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Palace Temples' (the named Palace Temples area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 15 — Castlevania / Clock Tower (NES, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/Castlevania-Dracula'sCastle.png (9920x2096)
- Crop region: CROP: source is a whole-world/composite map ('Dracula's Castle', 9920x2096) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Clock Tower' (the named Clock Tower area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 26 — Final Fantasy / Flying Fortress (NES, confidence low, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/FinalFantasy-World.png (4096x4096)
- Crop region: CROP: source is a whole-world/composite map ('World', 4096x4096) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Flying Fortress' (the named Flying Fortress area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 53 — Illusion of Gaia / Sky-High Nazca Lines (SNES, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/SuperNES/IllusionOfGaia-AnkorWat.png (2052x7937)
- Crop region: CROP: source is a whole-world/composite map ('Ankor Wat', 2052x7937) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Sky-High Nazca Lines' (the named Sky-High Nazca Lines area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 60 — Lufia II / The Ancient Cave (SNES, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/SuperNES/LufiaII-RiseOfTheSinistrals-Overworld.png (4096x4096)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 4096x4096) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'The Ancient Cave' (the named The Ancient Cave area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 84 — Wonder Boy III / Desert Sandstone Pyramid (Master System, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/MasterSystem/WonderBoyIII-Dragon'sTrap-Village.png (16128x1056)
- Crop region: CROP: source is a whole-world/composite map ('Village', 16128x1056) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Desert Sandstone Pyramid' (the named Desert Sandstone Pyramid area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 86 — Phantasy Star / Camineet Spaceport City (Master System, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/MasterSystem/PhantasyStar-Palma.png (2048x1536)
- Crop region: CROP: source is a whole-world/composite map ('Palma', 2048x1536) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Camineet Spaceport City' (the named Camineet Spaceport City area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 131 — The Guardian Legend / Labyrinth & Void (NES, confidence med, currently map)
- Source map: https://vgmaps.com/Atlas/NES/GuardianLegend-Overworld.png (6144x4608)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 6144x4608) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Labyrinth & Void' (the named Labyrinth & Void area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 135 — Clash at Demonhead / Branching Mountain (NES, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/ClashAtDemonhead-Route42.png (1683x5327)
- Crop region: CROP: source is a whole-world/composite map ('Route 42', 1683x5327) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Branching Mountain' (the named Branching Mountain area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 154 — Kirby Super Star / Battleship Halberd (SNES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/SuperNES/Kirby-SuperStar-RevengeOfMetaKnight.png (7134x10556)
- Crop region: CROP: source is a whole-world/composite map ('Revenge Of Meta Knight', 7134x10556) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Battleship Halberd' (the named Battleship Halberd area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 176 — Dynamite Headdy / Puppeteer Stage Theater (Sega Genesis & Master System, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/DynamiteHeaddy-Scene1-1-Getaway.png (16192x224)
- Crop region: CROP: source is a whole-world/composite map ('Scene 1-1: The Getaway', 16192x224) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Puppeteer Stage Theater' (the named Puppeteer Stage Theater area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 188 — Golden Axe: Revenge of Death Adder / Manta Mount (Arcade, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/Arcade/GoldenAxe-RevengeOfDeathAdder-Scene4-EscapeTheTown&Scene6-MarchForthToTheCastleOfDeathAdder.png (5797x1321)
- Crop region: CROP: source is a whole-world/composite map ('Scene 4: Escape The Town & Scene 6: March Forth To The Castle Of Death Adder', 5797x1321) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Manta Mount' (the named Manta Mount area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 240 — The Guardian Legend / Sub-Zero Corridors & Asteroid Core (NES, confidence med, currently map)
- Source map: https://vgmaps.com/Atlas/NES/GuardianLegend-Overworld.png (6144x4608)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 6144x4608) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Sub-Zero Corridors & Asteroid Core' (the named Sub-Zero Corridors & Asteroid Core area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 253 — Solar Jetman / Hostile Gravity Caverns & Fuel Extraction (NES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/SolarJetman-Planet6-Lemonte.png (7056x4360)
- Crop region: CROP: source is a whole-world/composite map ('Planet 6: Lemonte', 7056x4360) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Hostile Gravity Caverns & Fuel Extraction' (the named Hostile Gravity Caverns & Fuel Extraction area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 258 — G.I. Joe: A Real American Hero / Amazon Cobra Outposts (NES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/GIJoe-RealAmericanHero-Mission3-Stages1&3.png (2832x2592)
- Crop region: CROP: source is a whole-world/composite map ('Stages 1 & 3', 2832x2592) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Amazon Cobra Outposts' (the named Amazon Cobra Outposts area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 262 — The Lone Ranger / Isometric Frontier Deserts & Ghost Towns (NES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/LoneRanger-Overworld.png (1447x1119)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 1447x1119) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Isometric Frontier Deserts & Ghost Towns' (the named Isometric Frontier Deserts & Ghost Towns area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 268 — Chip 'n Dale Rescue Rangers / Kitchen Sink & Treehouse (NES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/Chip'NDale-RescueRangers-AreaH.png (3850x944)
- Crop region: CROP: source is a whole-world/composite map ('Area H', 3850x944) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Kitchen Sink & Treehouse' (the named Kitchen Sink & Treehouse area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 273 — Clash at Demonhead / Underground Lava Caverns & Peaks (NES, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/ClashAtDemonhead-Route42.png (1683x5327)
- Crop region: CROP: source is a whole-world/composite map ('Route 42', 1683x5327) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Underground Lava Caverns & Peaks' (the named Underground Lava Caverns & Peaks area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 277 — Magic of Scheherazade / Arabian Desert Oasis & Time Portals (NES, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/MagicOfScheherazade-Chapter1-WaterWorldMooroon-World.png (2560x2496)
- Crop region: CROP: source is a whole-world/composite map ('World', 2560x2496) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Arabian Desert Oasis & Time Portals' (the named Arabian Desert Oasis & Time Portals area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 344 — Shining Force II / Grans Island Overworld & Ruined Cathedrals (Sega Genesis / Master System / Game Gear, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/ShiningForceII-World.png (6056x4544)
- Crop region: CROP: source is a whole-world/composite map ('World', 6056x4544) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Grans Island Overworld & Ruined Cathedrals' (the named Grans Island Overworld & Ruined Cathedrals area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 348 — Alien Soldier / High-Orbit Space Freight Hulls (Sega Genesis / Master System / Game Gear, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Genesis/AlienSoldier(E)-ThyHeartInvincible-Stages21&22.png (12570x619)
- Crop region: CROP: source is a whole-world/composite map ('Stages 21 & 22', 12570x619) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'High-Orbit Space Freight Hulls' (the named High-Orbit Space Freight Hulls area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 372 — Alisia Dragoon / Ruined Swamp Temples & Mountain Roosts (Sega Genesis / Master System / Game Gear, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/AlisiaDragoon-Temple.png (4944x2221)
- Crop region: CROP: source is a whole-world/composite map ('Temple', 4944x2221) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Ruined Swamp Temples & Mountain Roosts' (the named Ruined Swamp Temples & Mountain Roosts area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 389 — The Punisher / Castle Grand Hotel & Kingpin's Penthouses (Arcade, confidence low, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Arcade/Punisher-LastStage.png (3909x2149)
- Crop region: CROP: source is a whole-world/composite map ('Last Stage', 3909x2149) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Castle Grand Hotel & Kingpin's Penthouses' (the named Castle Grand Hotel & Kingpin's Penthouses area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 394 — Dungeons & Dragons: Shadow over Mystara / Broken River Bridges (Arcade, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Arcade/Dungeons&Dragons-ShadowOverMystara-Stage3b-BattleOnTheVesuvia.png (7678x1762)
- Crop region: CROP: source is a whole-world/composite map ('Stage 3b: Battle On The Vesuvia', 7678x1762) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Broken River Bridges' (the named Broken River Bridges area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 418 — ESP Ra.De. / High-Tech Tokyo 2018 Glass Atriums (Arcade, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/Arcade/ESPRADE-AD2018Tokyo-Stages.png (1927x4814)
- Crop region: CROP: source is a whole-world/composite map ('Stages', 1927x4814) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'High-Tech Tokyo 2018 Glass Atriums' (the named High-Tech Tokyo 2018 Glass Atriums area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 491 — Wonder Boy III: Monster Lair / Seaside Dunes & Volcanic Chasms (More Arcade, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Arcade/WonderBoyIII-MonsterLair-Rounds(Food).png (6272x5229)
- Crop region: CROP: source is a whole-world/composite map ('Rounds (Food)', 6272x5229) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Seaside Dunes & Volcanic Chasms' (the named Seaside Dunes & Volcanic Chasms area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 501 — Castlevania / Dracula's Gates, Catacombs & Belfry (NES / Famicom, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/Castlevania-Dracula'sCastle.png (9920x2096)
- Crop region: CROP: source is a whole-world/composite map ('Dracula's Castle', 9920x2096) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Dracula's Gates, Catacombs & Belfry' (the named Dracula's Gates, Catacombs & Belfry area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 520 — Chip 'n Dale Rescue Rangers / Kitchen Pantries, Toy Stores & Casino (NES / Famicom, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/Chip'NDale-RescueRangers-AreaH.png (3850x944)
- Crop region: CROP: source is a whole-world/composite map ('Area H', 3850x944) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Kitchen Pantries, Toy Stores & Casino' (the named Kitchen Pantries, Toy Stores & Casino area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 530 — Zoda's Revenge: StarTropics II / Ancient Nile Riverbanks & Citadels (NES / Famicom, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/NES/Zoda'sRevenge-StarTropicsII-Chapter2-YumYum'sCave.png (2304x2484)
- Crop region: CROP: source is a whole-world/composite map ('Yum-Yum's Cave', 2304x2484) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Ancient Nile Riverbanks & Citadels' (the named Ancient Nile Riverbanks & Citadels area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 572 — The Guardian Legend / Sub-Zero Labyrinth Halls & Cosmic Cores (NES / Famicom, confidence med, currently map)
- Source map: https://vgmaps.com/Atlas/NES/GuardianLegend-Overworld.png (6144x4608)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 6144x4608) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Sub-Zero Labyrinth Halls & Cosmic Cores' (the named Sub-Zero Labyrinth Halls & Cosmic Cores area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 574 — Clash at Demonhead / Branching Mountain Trails & Lava Underpasses (NES / Famicom, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/NES/ClashAtDemonhead-Route42.png (1683x5327)
- Crop region: CROP: source is a whole-world/composite map ('Route 42', 1683x5327) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Branching Mountain Trails & Lava Underpasses' (the named Branching Mountain Trails & Lava Underpasses area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 619 — Demon's Crest / Ghoulish Cemeteries & Dark Realm Spire Citadels (SNES / Super Famicom, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/SuperNES/Demon'sCrest-Overworld.png (1024x1024)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 1024x1024) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Ghoulish Cemeteries & Dark Realm Spire Citadels' (the named Ghoulish Cemeteries & Dark Realm Spire Citadels area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 633 — Lufia II: Rise of the Sinistrals / 99-Floor Ancient Cave Crypts (SNES / Super Famicom, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/SuperNES/LufiaII-RiseOfTheSinistrals-Overworld.png (4096x4096)
- Crop region: CROP: source is a whole-world/composite map ('Overworld', 4096x4096) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target '99-Floor Ancient Cave Crypts' (the named 99-Floor Ancient Cave Crypts area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 643 — Mystic Ark / Toy World Deserts & Clockwork Fairground Tents (SNES / Super Famicom, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/SuperNES/MysticArk(J)-WorldMap.png (3234x3213)
- Crop region: CROP: source is a whole-world/composite map ('World Map', 3234x3213) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Toy World Deserts & Clockwork Fairground Tents' (the named Toy World Deserts & Clockwork Fairground Tents area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 648 — Rudra no Hihou (Treasure of the Rudras) / Ruined Continents & Sanctuaries (SNES / Super Famicom, confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/SuperNES/RudranoHihou(J)-TownOfAvdol.png (5440x2944)
- Crop region: CROP: source is a whole-world/composite map ('Town Of Avdol', 5440x2944) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Ruined Continents & Sanctuaries' (the named Ruined Continents & Sanctuaries area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 667 — Pulseman / Cyber Mainframe Matrices & Submerged Neo Tokyo (Sega Genesis / Mega Drive, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/Pulseman(J)-Stage2.png (13766x4452)
- Crop region: CROP: source is a whole-world/composite map ('Stage 2', 13766x4452) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Cyber Mainframe Matrices & Submerged Neo Tokyo' (the named Cyber Mainframe Matrices & Submerged Neo Tokyo area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 668 — Alien Soldier / Flying Freight Convoys & High-Speed Skyways (Sega Genesis / Mega Drive, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Genesis/AlienSoldier(E)-ThyHeartInvincible-Stages21&22.png (12570x619)
- Crop region: CROP: source is a whole-world/composite map ('Stages 21 & 22', 12570x619) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Flying Freight Convoys & High-Speed Skyways' (the named Flying Freight Convoys & High-Speed Skyways area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 674 — Dynamite Headdy / Puppet Theater Stages & Sky High Scenery (Sega Genesis / Mega Drive, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/DynamiteHeaddy-Scene1-1-Getaway.png (16192x224)
- Crop region: CROP: source is a whole-world/composite map ('Scene 1-1: The Getaway', 16192x224) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Puppet Theater Stages & Sky High Scenery' (the named Puppet Theater Stages & Sky High Scenery area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 679 — ToeJam & Earl in Panic on Funkotron / Funkotron Terrains & Bubble Gates (Sega Genesis / Mega Drive, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/ToeJam&EarlInPanicOnFunkotron-Level3.png (15040x4160)
- Crop region: CROP: source is a whole-world/composite map ('Level 3', 15040x4160) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Funkotron Terrains & Bubble Gates' (the named Funkotron Terrains & Bubble Gates area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 680 — Ecco: The Tides of Time / Future Skyways & Prehistoric Coral Reefs (Sega Genesis / Mega Drive, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Genesis/Ecco-TidesOfTime-LostOrcas.png (5376x4608)
- Crop region: CROP: source is a whole-world/composite map ('The Lost Orcas', 5376x4608) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Future Skyways & Prehistoric Coral Reefs' (the named Future Skyways & Prehistoric Coral Reefs area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 710 — Alisia Dragoon / Ruined Swamp Temples & Mountain Dragon Roosts (Sega Genesis / Mega Drive, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/AlisiaDragoon-Temple.png (4944x2221)
- Crop region: CROP: source is a whole-world/composite map ('Temple', 4944x2221) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Ruined Swamp Temples & Mountain Dragon Roosts' (the named Ruined Swamp Temples & Mountain Dragon Roosts area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 738 — Robo Aleste / Feudal Japanese Steam Mecha Fortresses & Skies (Sega CD / Mega-CD / 32X, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Genesis/RoboAleste-MountainRailroad.png (322x55712)
- Crop region: CROP: source is a whole-world/composite map ('Mountain Railroad', 322x55712) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Feudal Japanese Steam Mecha Fortresses & Skies' (the named Feudal Japanese Steam Mecha Fortresses & Skies area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 820 — The Return of Ishtar / Multi-Room Ancient Citadel Mazes & Undead Crypts (Arcade, confidence med, currently screenshot)
- Source map: https://vgmaps.com/Atlas/Arcade/ReturnOfIshtar(J)-Map.png (17640x13518)
- Crop region: CROP: source is a whole-world/composite map ('Map', 17640x13518) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Multi-Room Ancient Citadel Mazes & Undead Crypts' (the named Multi-Room Ancient Citadel Mazes & Undead Crypts area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 856 — River Raid / Cobalt Water Canyons, Emerald Riverbanks & Bridges (Atari 2600 / 5200 / 7800, confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Atari2600/RiverRaid-Map.png (20160x10392)
- Crop region: CROP: source is a whole-world/composite map ('Map', 20160x10392) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Cobalt Water Canyons, Emerald Riverbanks & Bridges' (the named Cobalt Water Canyons, Emerald Riverbanks & Bridges area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 967 — Out Zone / Alien Labyrinth Battle Trenches, Energy Grids & Blast Silos (Arcade (Psikyo / Toaplan / Raizing / Video System), confidence med, currently imageless)
- Source map: https://vgmaps.com/Atlas/Arcade/OutZone-Stages.png (256x47107)
- Crop region: CROP: source is a whole-world/composite map ('Stages', 256x47107) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Alien Labyrinth Battle Trenches, Energy Grids & Blast Silos' (the named Alien Labyrinth Battle Trenches, Energy Grids & Blast Silos area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

### World 993 — Warrior Blade: Rastan Saga III / Dual-Screen Monster Plains & Citadel Arenas (Arcade (Taito / Irem), confidence low, currently imageless)
- Source map: https://vgmaps.com/Atlas/Arcade/WarriorBlade-RastanSagaEpisodeIII(J)-KeFaMountain.png (7745x4504)
- Crop region: CROP: source is a whole-world/composite map ('Ke Fa Mountain', 7745x4504) — no area-specific map; only the whole-world map exists. Crop to the single coherent region matching the world target 'Dual-Screen Monster Plains & Citadel Arenas' (the named Dual-Screen Monster Plains & Citadel Arenas area of the composite); discard the rest. If the target is an interior that does not appear on this composite, treat the map as unusable for this world instead.

## Verification

**Every** unique VGMaps URL among the applied records was re-verified live on 2026-11-01 before writing (not just a sample): **237/237 returned HTTP 200 with an `image/*` content type** (HEAD, with a ranged-GET fallback; per-URL results in `url_check.json`). The 284 applied records reference 237 unique URLs — some maps serve several worlds of the same game.

Sample of applied records with their URL check results:

| World | Game | Applied URL | Status | Content-Type |
|---|---|---|---|---|
| 1 | Adventure | https://vgmaps.com/Atlas/Atari2600/Adventure-Variation1.png | 200 | image/png |
| 16 | Mega Man 2 | https://vgmaps.com/Atlas/NES/MegaManII-BubbleMan.png | 200 | image/png |
| 21 | DuckTales | https://vgmaps.com/Atlas/NES/DuckTales-Moon.png | 200 | image/png |
| 24 | Kirby's Adventure | https://vgmaps.com/Atlas/NES/Kirby'sAdventure-Level7-RainbowResort.png | 200 | image/png |
| 25 | EarthBound Beginnings | https://vgmaps.com/Atlas/NES/Mother(J)-Magicant.png | 200 | image/png |
| 27 | Dragon Warrior | https://vgmaps.com/Atlas/NES/DragonWarrior-CharlockCastle.png | 200 | image/png |
| 29 | Rygar | https://vgmaps.com/Atlas/NES/Rygar-Lapis.png | 200 | image/png |
| 30 | Shadowgate | https://vgmaps.com/Atlas/NES/Shadowgate-CastleShadowgate.png | 200 | image/png |
| 31 | Crystalis | https://vgmaps.com/Atlas/NES/Crystalis-FloatingTower.png | 200 | image/png |
| 32 | A Boy and His Blob | https://vgmaps.com/Atlas/NES/BoyAndHisBlob-TroubleOnBlobolonia-Earth(NightWorld).png | 200 | image/png |
| 36 | A Link to the Past | https://vgmaps.com/Atlas/SuperNES/LegendOfZelda-ALinkToThePast-DarkWorld-PyramidOfPower.png | 200 | image/png |
| 37 | Super Metroid | https://vgmaps.com/Atlas/SuperNES/SuperMetroid-Maridia.png | 200 | image/png |
| 38 | Chrono Trigger | https://vgmaps.com/Atlas/SuperNES/ChronoTrigger-2300AD-ArrisDome.png | 200 | image/png |
| 39 | Chrono Trigger | https://vgmaps.com/Atlas/SuperNES/ChronoTrigger-65000000BC-TyranoLair.png | 200 | image/png |
| 40 | Final Fantasy VI | https://vgmaps.com/Atlas/SuperNES/FinalFantasyVI-WorldOfBalance-MagitekFactory.png | 200 | image/png |
| 41 | EarthBound | https://vgmaps.com/Atlas/SuperNES/EarthBound-Moonside.png | 200 | image/png |
| 42 | Donkey Kong Country | https://vgmaps.com/Atlas/SuperNES/DonkeyKongCountry-MonkeyMines-MineCartCarnage.png | 200 | image/png |
| 43 | Donkey Kong Country 2 | https://vgmaps.com/Atlas/SuperNES/DonkeyKongCountry2-Diddy'sKong-Quest-KrazyKremland-BrambleScramble.png | 200 | image/png |
| 44 | Mega Man X | https://vgmaps.com/Atlas/SuperNES/MegaManX-Highway.png | 200 | image/png |
| 46 | Contra III | https://vgmaps.com/Atlas/SuperNES/ContraIII-AlienWars-Stage3-NeoKobeSteelFactory.png | 200 | image/png |

Post-apply integrity checks (independent re-read of base vs merged): exactly 284 entries differ — precisely the applied set; **zero non-image fields changed** in any entry; entry order and ids 1–1000 preserved; every image set keeps `image_url == image_urls[0]`, kind/URL alignment, and no duplicate URLs; the 716 untouched entries are deep-equal to the base. The base catalog and the proposal were not modified (base still 2,016,260 bytes). Serialization matches the base file byte-for-byte for unchanged content (indent=1, ensure_ascii, no trailing newline).

## Method notes

- Image-field conventions were taken from the re-passed catalog itself: entries with images always carry all four fields (`image_url`, `image_kind`, `image_urls`, `image_kinds`) as the last block of the entry, in that order; sets are layout-first (every pre-existing 2-image set is `[map, screenshot]`). Adds to imageless entries append the four-field block in the same position and order.
- Reconciliation against the re-pass: of the 285 add/replace-layout proposals, 176 worlds were still imageless, 108 had a screenshot primary (81 as proposed + 27 filled by the re-pass), and 1 (world 810) had been filled with a map.
- Scripts kept for audit: `verify_urls.py`, `apply.py`, `build_report.py`; raw data: `url_check.json`, `apply_log.json`.
