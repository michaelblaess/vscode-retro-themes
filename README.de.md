# Retro Themes for VS Code

<p align="center">
  <img src="docs/flags/gb.svg" height="13" alt=""> <a href="README.md">English</a> ·
  <img src="docs/flags/de.svg" height="13" alt=""> <b>Deutsch</b>
</p>

---

[![Stars](https://img.shields.io/github/stars/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=fbbf24)](https://github.com/michaelblaess/vscode-retro-themes/stargazers)
[![Forks](https://img.shields.io/github/forks/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=34d399)](https://github.com/michaelblaess/vscode-retro-themes/network/members)
[![Issues](https://img.shields.io/github/issues/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=f87171)](https://github.com/michaelblaess/vscode-retro-themes/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/michaelblaess/vscode-retro-themes?logo=github&logoColor=white&color=a78bfa)](https://github.com/michaelblaess/vscode-retro-themes/pulls)

[![Last Commit](https://img.shields.io/github/last-commit/michaelblaess/vscode-retro-themes?logo=git&logoColor=white&color=3b82f6)](https://github.com/michaelblaess/vscode-retro-themes/commits/main)
[![License](https://img.shields.io/badge/license-Apache_2.0-3b82f6)](LICENSE)
[![VS Code](https://img.shields.io/badge/vscode-1.70+-3b82f6?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Themes](https://img.shields.io/badge/themes-31-fbbf24)](themes)

31 Farb-Themes für VS Code — Paletten im Stil von Vintage-8-Bit, Terminal-Phosphor, Unix-Workstation, Armbanduhren, Comic-Pulp und 80er-Pastell.

Diese Erweiterung ist ein 1:1-Abbild des Python-Pakets [textual-themes](https://github.com/michaelblaess/textual-themes) — gleiche Slugs, gleiche Anzeigenamen, gleiche Farben. So nutzt du dasselbe Theme in deinen Terminal-TUI-Apps und in deinem Editor.

> **⚠ Markenrechtlicher Hinweis**
>
> Dies ist ein **unabhängiges, von Fans erstelltes, nicht-kommerzielles**
> Projekt. Die Theme-Namen beschreiben ausschließlich den visuellen Stil —
> es werden keine Marken Dritter als Theme-Namen verwendet. Jeder
> verbleibende Markenbezug in beschreibendem Text (z. B. "PETSCII style",
> "GEM Desktop") ist rein beschreibend und steht in keiner Verbindung zu
> den jeweiligen Markeninhabern, wird von ihnen nicht unterstützt und ist
> nicht von ihnen lizenziert.

## Dunkle Themes (26)

| Theme | Stil |
|-------|------|
| **Brotkasten** | Hellblau auf Königsblau, der ikonische 8-Bit-Farbton (PETSCII) |
| **Boing** | Dreifarbige Workbench-Palette: Blau/Weiß/Orange |
| **Classic Terminal** | Phosphor-Grün auf Schwarz (CRT) |
| **Next** | Dunkelgrau mit Magenta-Akzenten — 3D-Fasen der Workstation-Ära |
| **BeBox** | Blaugrau mit gelbem Statusleisten-Akzent |
| **Bunty** | Aubergine mit warmen Orange-Akzenten |
| **Luna** | Himmelblaue Taskleiste mit grünem Start-Button |
| **Commandr** | Blau/Cyan/Gelb-Palette eines Dateimanagers |
| **Motif** | Beige-schiefergraues Unternehmens-Unix-Toolkit |
| **Warp** | Dunkelblau mit Türkis-Akzenten |
| **Geeko** | Dunkelgrün mit Weiß |
| **Minty** | Warmes Minzgrün auf Anthrazit |
| **Crimson** | Tiefes Rot auf dunklem Anthrazit |
| **Razzy** | Himbeerrot auf dunklem Schiefer |
| **Beastie** | Daemon-Rot auf dunklem Schiefer |
| **Fifty-Eight** | Schwarzes Zifferblatt mit gealtertem Gold-Lume + Lünetten-Rot (Vintage-Taucheruhr) |
| **Bluesy** | Königsblau mit satten gelb-goldenen Akzenten |
| **Goldfinder** | Tiefes Schwarz mit 18-Karat-Gold-Akzenten — Bösewicht-Glamour |
| **Hulkula** | Leuchtend grüne Wut mit stahlgrauen Kanten |
| **Flughund** | Mitternachtsschwarz & mondbeschienenes Blau |
| **Classic Navy** | Tiefes Marineblau mit Silber und gedämpftem Ziegelrot |
| **Synthwave** | Tiefes Violett mit Neonpink und elektrischem Cyan |
| **Miami** | 80er-Pastell — dämmriges Türkis, Flamingo-Pink, Sonnenuntergangs-Koralle |
| **Racing** | Anthrazit mit tiefem Blau, Kirschrot und silbernen Streifen |
| **Metropolis** | Kräftige Primärtriade aus Blau, Karminrot und Sonnengelb |
| **Spiderized** | Rotes & königsblaues Helden-Kostüm (hoher Kontrast) |

## Helle Themes (5)

| Theme | Stil |
|-------|------|
| **Gemstone** | Monochromer GEM-Desktop-Look |
| **Cupertino** | Klares Hellgrau mit blauen Akzenten |
| **Plan 9** | Pulpiges Gelb/Blau/Grün |
| **Brick** | Olivgrünes Handheld-LCD auf beige-grauem Gehäuse |
| **Clipper** | Globusblau auf Elfenbein — Jet-Age-Lackierung |

## Installation

### Aus dem Quellcode

```bash
git clone https://github.com/michaelblaess/vscode-retro-themes.git
cd vscode-retro-themes
npx @vscode/vsce package --no-dependencies
code --install-extension retro-themes-1.0.0.vsix
```

Öffne nach der Installation die Befehlspalette (`Ctrl+Shift+P`), wähle **Preferences: Color Theme** und dann ein beliebiges Theme, das mit **Retro —** beginnt.

## Themes neu generieren

Die `themes/*.json`-Dateien werden aus `generate-themes.py` generiert — dieses Skript hält alle 31 Paletten an einer Stelle und gibt das VS-Code-JSON aus. Um eine Farbe anzupassen oder ein Theme hinzuzufügen: bearbeite `THEMES` im Skript, führe `python generate-themes.py` aus, und die JSON-Dateien werden direkt überschrieben (und jede veraltete Datei wird entfernt).

```bash
python generate-themes.py
```

## Begleitpaket

Für Textual-TUI-Anwendungen installiere [textual-themes](https://github.com/michaelblaess/textual-themes) — gleiche Slugs, gleiche Farben, gleiches Flair.

```bash
pip install git+https://github.com/michaelblaess/textual-themes.git
```

## Lizenz

Apache License 2.0 — siehe [LICENSE](LICENSE).

## Autor

Michael Blaess — [GitHub](https://github.com/michaelblaess)
