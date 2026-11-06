# Import and publishing files

Each profile has two metadata formats:

- `curseforge/manifest.json` is the root manifest for a CurseForge Minecraft modpack ZIP.
- `modrinth.index.json` is the index used inside a `.mrpack` archive. Prism Launcher and Modrinth App can import this format.

Run `python tools/export_packs.py` from the project root to create archives in `dist/`. The script creates starter archives from the checked-in metadata and `overrides` directories.

The current manifests intentionally contain no third-party file entries because the project does not ship external jars and has no verified CurseForge project/file IDs. Before publishing, add every exact Forge 1.20.1 mod release to the CurseForge `files` array and the Modrinth `files` array, including its download URL and SHA-1 hash. Keep the same dependency set in both formats.

Use one profile per archive. Do not combine Power and Lite in one instance because their performance and visual settings are different.
