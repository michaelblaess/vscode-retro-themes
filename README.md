# Retro Themes for VS Code

<p align="center">
  <img src="docs/flags/gb.png" height="13" alt=""> <b>English</b> ·
  <img src="docs/flags/de.png" height="13" alt=""> <a href="README.de.md">Deutsch</a>
</p>

---

<p align="center">
  <img src="docs/banner.jpg" alt="vscode-retro-themes - five editor windows, each in a different retro color scheme" width="100%">
</p>

[![Stars](https://img.shields.io/github/stars/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=fbbf24)](https://github.com/michaelblaess/vscode-retro-themes/stargazers)
[![Forks](https://img.shields.io/github/forks/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=34d399)](https://github.com/michaelblaess/vscode-retro-themes/network/members)
[![Issues](https://img.shields.io/github/issues/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=f87171)](https://github.com/michaelblaess/vscode-retro-themes/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=a78bfa)](https://github.com/michaelblaess/vscode-retro-themes/pulls)

[![Last Commit](https://img.shields.io/github/last-commit/michaelblaess/vscode-retro-themes?logo=git&logoColor=white&color=3b82f6)](https://github.com/michaelblaess/vscode-retro-themes/commits/main)
[![License](https://img.shields.io/badge/license-Apache_2.0-3b82f6)](LICENSE)
[![VS Code](https://img.shields.io/badge/vscode-1.70+-3b82f6?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Themes](https://img.shields.io/badge/themes-41-fbbf24)](themes)
[![Marketplace](https://img.shields.io/visual-studio-marketplace/v/michaelblaess.retro-themes?label=marketplace&logo=visualstudiocode&logoColor=white&color=3b82f6)](https://marketplace.visualstudio.com/items?itemName=michaelblaess.retro-themes)

41 color themes for VS Code, 36 dark and 5 light — vintage 8-bit, terminal phosphor, Unix workstation, watch, comic-pulp, 80s-pastel and mafia-noir palettes.

The palettes come from the [textual-themes](https://github.com/michaelblaess/textual-themes) Python package, the derivation is shared with [nvim-retro-themes](https://github.com/michaelblaess/nvim-retro-themes). So the same theme looks the same in your terminal TUI apps, in Neovim and in VS Code.

The colours are not copied one to one. A palette made for a TUI has small text fields, an editor is one large text surface. Every colour is therefore checked and lifted until it is readable, and syntax colours that would look alike are pulled apart.

![Retro — Synthwave](docs/vorschau/synthwave.png)

Synthwave on top, below it Classic Terminal and Clipper. **[See all 41 themes](docs/vorschau.md)**

![Retro — Classic Terminal](docs/vorschau/classic-terminal.png)

![Retro — Clipper](docs/vorschau/clipper.png)

> **⚠ Trademark Disclaimer**
>
> This is an **independent, fan-made, non-commercial** project. Theme
> names are descriptive of the visual style only — no third-party
> trademarks are used as theme names. Any remaining brand reference in
> descriptive text (e.g. "PETSCII style", "GEM Desktop") is purely
> descriptive and not affiliated with, endorsed by, or licensed by the
> respective trademark owners.

## Dark Themes (36)

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
| **Ascot** | Le-Mans racing green with signal yellow, silver and beige text |
| **Joker** | Royal purple suit, acid-green hair and yellow vest |
| **Marley** | Reggae roots palette: black, green, gold, red |
| **Lenseflare** | 80s orange-teal bichromatic on twilight blue |
| **Platoon** | Muted military olive-drab with khaki accent on near-black |
| **Corleone** | Cold mafia-noir: bronze, steel-grey and ash on bluish black |
| **Golden Brown** | Warm mafia-noir: antique gold, sepia and parchment on warm black |
| **Goldrunner** | Gold on a violet city skyline, 16-bit era |
| **Hercules** | Amber phosphor monochrome |
| **Christophorus** | Navy with gold keywords and cyan functions |

## Light Themes (5)

| Theme | Style |
|-------|-------|
| **Gemstone** | Monochrome GEM Desktop look |
| **Cupertino** | Clean light gray with blue accents |
| **Plan 9** | Pulpy yellow/blue/green |
| **Brick** | Olive-green handheld LCD on beige-gray case |
| **Clipper** | Globe blue on ivory — jet-age livery |

## Installation

### From the Marketplace

In VS Code open the Extensions view (`Ctrl+Shift+X`), search for **Retro Themes** by Michael
Blaess and install it, or from a terminal:

```bash
code --install-extension michaelblaess.retro-themes
```

The listing is at [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=michaelblaess.retro-themes).

### From a release

Every [release](https://github.com/michaelblaess/vscode-retro-themes/releases) carries the
`.vsix` file:

```bash
code --install-extension retro-themes-2.0.1.vsix --force
```

### From source

```bash
git clone https://github.com/michaelblaess/vscode-retro-themes.git
cd vscode-retro-themes
npx @vscode/vsce package --no-dependencies
code --install-extension retro-themes-*.vsix --force
```

After installation, open the Command Palette (`Ctrl+Shift+P`) and select **Preferences: Color Theme**, then choose any theme starting with **Retro —**.

## The rules behind the colours

- **Readable first.** Text and syntax reach a contrast of at least 4.5:1 on the editor, the
  current line and the hover windows, line numbers at least 3:1. Hue and saturation stay, so a
  theme keeps its character.
- **The surface moves away from the text.** Where a palette sits too close to its own text, a dark
  theme gets darker and a light one lighter, until the body text reaches 8:1.
- **Syntax colours stay apart**, from each other and from the body text: at least 22 in CIE76.
  Where a palette runs out of colours, the next one is taken from the same palette, first a shift
  in lightness, then another palette colour, then a shift in hue.
- **Text on coloured surfaces** such as buttons, badges and the status bar always takes the
  colour with the highest contrast, never a fixed white.

Every rule is covered by a test over all 41 themes, run against the finished JSON the way VS Code
reads it.

## Regenerating themes

The `themes/*.json` files and the theme list in `package.json` are generated. The palettes live in
`src/vscode_retro_themes/data/`, a snapshot of textual-themes 0.14.0, the derivation in
`derive.py`, the mapping onto VS Code in `render.py`.

```bash
uv run python -m vscode_retro_themes            # write themes/ and package.json
uv run python -m vscode_retro_themes --report   # contrast table only
uv run --extra dev pytest                       # check every theme
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
