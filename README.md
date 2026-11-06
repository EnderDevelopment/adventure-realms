# Minecraft Modpack Project: Frontier Realms

Frontier Realms is a Minecraft modpack project for Forge 1.20.1 with a small companion mod, Power and Lite installation profiles, modpack manifests, optimization guidance, shader recommendations, and a curated plan for exploration, realistic terrain, bosses, new dimensions, parkour, TACZ firearms, and combat-focused gameplay. The repository provides the project structure and export tools; third-party mods, firearms content, and shader files must be added from their official sources.

## Install

Requirements:

- Minecraft Java Edition 1.20.1
- Java 17
- Minecraft Forge 47.3.0 or another compatible Forge 47.x release
- Python 3 for the pack export script
- A launcher that supports CurseForge packs or Modrinth `.mrpack` files

1. Clone or download this repository.
2. Review `profiles/power/mod-list.txt` or `profiles/lite/mod-list.txt`.
3. Download the selected Forge 1.20.1 mods from their official project pages.
4. Include TACZ and compatible official attachment or content packs if firearms are required.
5. Add the exact third-party project and file information to the selected CurseForge manifest and Modrinth index. The supplied manifests intentionally have empty file lists.
6. Run the following command from the project root:

```text
python tools/export_packs.py
```

7. Import the generated archive from `dist/` into Prism Launcher, Modrinth App, CurseForge, or another compatible launcher.
8. Install Java 17 and launch the profile with Forge 47.3.0.
9. Download compatible shader ZIP files when needed and place them, still compressed, in the instance `shaderpacks/` directory.

## Use

Choose the Power profile for stronger computers. It targets 10 to 12 GB of allocated RAM, 12 to 16 chunks of render distance, higher simulation distance, and medium or high shader presets.

Choose the Lite profile for low-end systems. It targets 5 to 6 GB of allocated RAM, 6 to 8 chunks of render distance, reduced particles, disabled entity shadows, and no shaders by default.

The recommended gameplay plan includes exploration-focused terrain, dungeons, hostile mobs, bosses, new dimensions, TACZ firearm combat, parkour or movement features, and progression systems. The profiles also recommend Embeddium, ModernFix, FerriteCore, Entity Culling, ImmediatelyFast, and Clumps for performance.

Shader recommendations are grouped in `profiles/shader-tiers.md`:

- Very low: MakeUp Ultra Fast and Sildur's Enhanced Default Lite
- Low: Complementary Reimagined and Sildur's Vibrant Lite
- Medium: Complementary Reimagined and BSL
- High: Complementary Reimagined, BSL, and Photon

Create a new world after changing terrain, biome, or structure mods. Back up existing worlds before switching profiles. Follow every third-party mod and shader license and keep each dependency matched to Minecraft 1.20.1 and Forge.

The companion mod can be built with:

```text
./gradlew build
```

Its output is written to `build/libs`. This project does not include Minecraft, Forge, third-party mod JARs, TACZ content packs, or shader archives.

---

More Minecraft mod projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/3791bd03-2b37-4199-9819-ef4a002d11f5?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=3791bd03-2b37-4199-9819-ef4a002d11f5
