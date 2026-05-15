# Plan — vscode-retro-themes

Stand: 16.05.2026

## Erledigt

- [x] Sync auf textual-themes 0.8 — 7 neue Themes (Ascot, Joker, Marley,
      Lenseflare, Platoon, Corleone, Golden Brown), jetzt 38 statt 31
- [x] Verifiziert: die 31 alten Paletten sind 1:1 unveraendert
- [x] `generate-themes.py`, `package.json`, beide READMEs aktualisiert
- [x] Flaggen SVG -> PNG (vsce verbietet SVG in der README)
- [x] `.vscodeignore` neu (Generator + `__pycache__` raus aus dem Paket)
- [x] Committet & gepusht — `ac79771` auf `main`
- [x] `retro-themes-1.0.0.vsix` gebaut (nicht eingecheckt, `.gitignore`)

## Offen

### Lesbarkeits-Ueberarbeitung der Themes (Hauptaufgabe morgen)

Mehrere Themes sind in VS Code schwer lesbar. Ursache: die VS-Code-JSONs
werden rein algorithmisch aus 10 textual-themes-Farbrollen abgeleitet —
zu wenig Kontrast bei Kommentaren, Selektion und Syntax-Tokens auf
dunklem Hintergrund.

- [ ] Konkrete Problem-Themes identifizieren (Michael nennt die kritischen)
- [ ] Pruefen: globale Ableitungslogik in `build_theme` /
      `build_token_colors` nachschaerfen vs. pro-Theme-Overrides
- [ ] Kontrast pruefen: Kommentar-Alpha, `editor.selectionBackground`,
      Token-Farben (Keyword/String/Function/Type)
- [ ] Aenderungen ausschliesslich im Generator `generate-themes.py` —
      NICHT in den generierten `themes/*.json` (werden ueberschrieben)
- [ ] `python generate-themes.py` ausfuehren, `.vsix` neu bauen

### Wichtig beim Wiederaufnehmen

- Aenderungen am Theme-Look gehen IMMER in `generate-themes.py`.
- Versionsbump auf `1.1.0` wurde bewusst nicht gemacht — Install laeuft
  ueber `code --install-extension retro-themes-1.0.0.vsix --force`.
  Bei der naechsten echten Release-Runde Bump nachholen.
- textual-themes bleibt die Quelle der Wahrheit fuer die 10 Kernfarben.
