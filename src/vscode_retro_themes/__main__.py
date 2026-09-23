"""Erzeugt die Themes, traegt sie in die package.json ein und zeigt ihre Kontrastwerte.

Verwendung:
    uv run python -m vscode_retro_themes                 alle Themes nach themes/
    uv run python -m vscode_retro_themes boing synthwave nur diese Themes
    uv run python -m vscode_retro_themes --report        nur die Kontrasttabelle, nichts schreiben
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from .color import contrast
from .derive import Scheme, derive
from .palettes import Base, load_all
from .render import min_syntax_distance, package_entry, write

ROOT = Path(__file__).resolve().parents[2]
THEMES_DIR = ROOT / "themes"
PACKAGE_JSON = ROOT / "package.json"


def _report_line(scheme: Scheme) -> str:
    syntax = (scheme.keyword, scheme.function, scheme.string, scheme.number, scheme.type_, scheme.special)
    min_contrast = min(contrast(color, scheme.bg) for color in (*syntax, scheme.comment, scheme.fg))
    return (
        f"{scheme.name:<18} Kommentar {contrast(scheme.comment, scheme.bg):5.2f}  "
        f"Zeilennr {contrast(scheme.fg_faint, scheme.bg):5.2f}  "
        f"Syntax min {min_contrast:5.2f}  Abstand min {min_syntax_distance(scheme):5.1f}"
    )


def _update_package_json(schemes: list[Scheme]) -> None:
    """Ersetzt die Themeliste, alles andere in der package.json bleibt wie es ist."""
    package = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))
    package["contributes"]["themes"] = [package_entry(scheme) for scheme in schemes]
    text = json.dumps(package, indent=2, ensure_ascii=False) + "\n"
    PACKAGE_JSON.write_text(text, encoding="utf-8", newline="\n")


def main(argv: list[str]) -> int:
    only = [arg for arg in argv if not arg.startswith("-")]
    report_only = "--report" in argv
    themes: list[Base] = [theme for theme in load_all() if not only or theme.name in only]
    unknown = set(only) - {theme.name for theme in themes}
    if unknown:
        print(f"Unbekannte Themes: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 1

    schemes = [derive(base) for base in themes]
    for scheme in schemes:
        print(_report_line(scheme))
        if not report_only:
            write(scheme, THEMES_DIR)
    # Die Liste nur bei einem vollstaendigen Lauf neu schreiben, sonst fehlten die anderen Themes
    if not report_only and not only:
        _update_package_json(schemes)
        stale = {path.stem for path in THEMES_DIR.glob("*.json")} - {scheme.name for scheme in schemes}
        for name in sorted(stale):
            (THEMES_DIR / f"{name}.json").unlink()
            print(f"entfernt: themes/{name}.json")
        print(f"{len(schemes)} Themes in {THEMES_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
