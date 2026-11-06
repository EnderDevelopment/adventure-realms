"""Create import archives for the Frontier Realms profiles.

This script packages the checked-in manifests and overrides. Add verified external
mod files and manifest entries before publishing a playable pack.
"""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ("power", "lite")


def add_tree(archive: ZipFile, source: Path, prefix: str) -> None:
    for path in sorted(source.rglob("*")):
        if path.is_file():
            archive.write(path, f"{prefix}/{path.relative_to(source).as_posix()}")


def build_profile(profile: str) -> None:
    base = ROOT / "profiles" / profile
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)

    curseforge_archive = output / f"frontier-realms-{profile}-curseforge.zip"
    with ZipFile(curseforge_archive, "w", ZIP_DEFLATED) as archive:
        archive.write(base / "curseforge" / "manifest.json", "manifest.json")
        add_tree(archive, base / "overrides", "overrides")

    modrinth_archive = output / f"frontier-realms-{profile}.mrpack"
    with ZipFile(modrinth_archive, "w", ZIP_DEFLATED) as archive:
        archive.write(base / "modrinth.index.json", "modrinth.index.json")
        add_tree(archive, base / "overrides", "overrides")


if __name__ == "__main__":
    for selected_profile in PROFILES:
        build_profile(selected_profile)
    print("Created starter archives in dist/. Add verified mod entries before publishing.")
