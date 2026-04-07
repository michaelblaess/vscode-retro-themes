# Retro Themes for VS Code

18 color themes inspired by classic computers and operating systems.

## Dark Themes

| Theme | Inspiration | Style |
|-------|-------------|-------|
| **C64** | Commodore 64 (1982) | Blue on light-blue, the PETSCII classic |
| **Amiga** | Workbench 1.3 (1987) | Blue/white/orange three-color scheme |
| **IBM Terminal** | IBM 3278 (1970s) | Phosphor-green on black |
| **NeXTSTEP** | NeXTSTEP (1989) | Dark gray with purple accents |
| **BeOS** | BeOS (1995) | Blue-gray with yellow Deskbar accent |
| **Ubuntu** | Ubuntu Desktop | Aubergine/purple with orange accents |
| **Windows XP** | Windows XP Luna (2001) | Blue taskbar with green Start button |
| **MS-DOS** | Norton Commander (1986) | Blue/cyan/yellow file manager |
| **OS/2 Warp** | IBM OS/2 Warp (1994) | Dark blue with teal accents |
| **openSUSE** | openSUSE Linux | Dark green with white |
| **Solaris CDE** | Sun CDE Desktop (1993) | Slate gray with warm accents |
| **Linux Mint** | Cinnamon Desktop | Warm mint-green on charcoal |
| **Red Hat** | Red Hat Linux | Shadowman red on dark |
| **Raspberry Pi** | Raspberry Pi OS | Raspberry red on dark blue-gray |
| **FreeBSD** | FreeBSD | Beastie red on dark slate |

## Light Themes

| Theme | Inspiration | Style |
|-------|-------------|-------|
| **Atari ST** | GEM Desktop (1985) | White/black/green, monochrome feel |
| **macOS** | macOS (modern) | Clean light gray with blue accents |
| **Plan 9** | Plan 9 from Bell Labs (1992) | Pale yellow/blue with green accents |

## Installation

### From VSIX

```bash
# Build VSIX
npx @vscode/vsce package --no-dependencies

# Install
code --install-extension retro-themes-0.2.0.vsix
```

### From source

```bash
git clone https://github.com/michaelblaess/vscode-retro-themes.git
cd vscode-retro-themes
npx @vscode/vsce package --no-dependencies
code --install-extension retro-themes-0.2.0.vsix
```

After installation, open Command Palette (`Ctrl+Shift+P`) and select **Preferences: Color Theme**, then choose any theme starting with **Retro —**.

## Color Palette

All themes share the same color palette as [textual-themes](https://github.com/michaelblaess/textual-themes) for Textual TUI applications.

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Author

Michael Blaess — [GitHub](https://github.com/michaelblaess)
