# Retro Themes for VS Code

31 color themes for VS Code — vintage 8-bit, terminal phosphor, Unix workstation, watch, comic-pulp and 80s-pastel palettes.

This extension is a 1:1 mirror of the [textual-themes](https://github.com/michaelblaess/textual-themes) Python package — same slugs, same display names, same colors. Use the same theme in your terminal TUI apps and your editor.

> **⚠ Trademark Disclaimer**
>
> This is an **independent, fan-made, non-commercial** project. Theme
> names are descriptive of the visual style only — no third-party
> trademarks are used as theme names. Any remaining brand reference in
> descriptive text (e.g. "PETSCII style", "GEM Desktop") is purely
> descriptive and not affiliated with, endorsed by, or licensed by the
> respective trademark owners.

## Dark Themes (26)

| Theme | Style |
|-------|-------|
| **Brotkasten** | Light blue on royal blue, the iconic 8-bit color cast (PETSCII) |
| **Boing** | Three-color workbench palette: blue/white/orange |
| **Classic Terminal** | Phosphor-green on black (CRT) |
| **Next** | Dark gray with magenta accents — workstation-era 3D bevels |
| **BeBox** | Blue-gray with yellow status-bar accent |
| **Bunty** | Aubergine with warm orange accents |
| **Luna** | Sky-blue task-bar with green start button |
| **Commandr** | Blue/cyan/yellow file-manager palette |
| **Motif** | Beige slate-gray corporate Unix toolkit |
| **Warp** | Dark blue with teal accents |
| **Geeko** | Dark green with white |
| **Minty** | Warm mint-green on charcoal |
| **Crimson** | Deep red on dark charcoal |
| **Razzy** | Raspberry red on dark slate |
| **Beastie** | Daemon red on dark slate |
| **Fifty-Eight** | Black dial with aged gold lume + bezel red (vintage diver) |
| **Bluesy** | Royal blue with rich yellow-gold accents |
| **Goldfinder** | Deep black with 18K gold accents — villain glamour |
| **Hulkula** | Vivid green rage with steel-gray edges |
| **Flughund** | Midnight black & moonlit blue |
| **Classic Navy** | Deep navy with silver and muted brick-red |
| **Synthwave** | Deep purple with neon pink and electric cyan |
| **Miami** | Pastel 80s — twilight teal, flamingo pink, sunset coral |
| **Racing** | Charcoal with deep blue, cherry red and silver stripes |
| **Metropolis** | Bold blue, crimson red and sun yellow primary triad |
| **Spiderized** | Red & royal-blue hero suit (high-contrast) |

## Light Themes (5)

| Theme | Style |
|-------|-------|
| **Gemstone** | Monochrome GEM Desktop look |
| **Cupertino** | Clean light gray with blue accents |
| **Plan 9** | Pulpy yellow/blue/green |
| **Brick** | Olive-green handheld LCD on beige-gray case |
| **Clipper** | Globe blue on ivory — jet-age livery |

## Installation

### From source

```bash
git clone https://github.com/michaelblaess/vscode-retro-themes.git
cd vscode-retro-themes
npx @vscode/vsce package --no-dependencies
code --install-extension retro-themes-1.0.0.vsix
```

After installation, open the Command Palette (`Ctrl+Shift+P`) and select **Preferences: Color Theme**, then choose any theme starting with **Retro —**.

## Regenerating themes

The `themes/*.json` files are generated from `generate-themes.py` — that script holds all 31 palettes in one place and emits the VS Code JSON. To tweak a color or add a theme: edit `THEMES` in the script, run `python generate-themes.py`, and the JSON files get rewritten in-place (and any obsolete file is removed).

```bash
python generate-themes.py
```

## Companion package

For Textual TUI applications, install [textual-themes](https://github.com/michaelblaess/textual-themes) — same slugs, same colors, same vibe.

```bash
pip install git+https://github.com/michaelblaess/textual-themes.git
```

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Author

Michael Blaess — [GitHub](https://github.com/michaelblaess)
