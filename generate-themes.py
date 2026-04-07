"""Generiert VS Code Theme-Dateien aus den textual-themes Farbpaletten.

Einmalig ausfuehren: python generate-themes.py
Erzeugt 15 JSON-Dateien im themes/ Ordner.
"""
import json
import os


def hex_alpha(color: str, alpha: str) -> str:
    """Haengt Alpha-Wert an Hex-Farbe an."""
    return f"{color}{alpha}"


def lighten(color: str, amount: int = 20) -> str:
    """Hellt eine Hex-Farbe auf."""
    r = min(255, int(color[1:3], 16) + amount)
    g = min(255, int(color[3:5], 16) + amount)
    b = min(255, int(color[5:7], 16) + amount)
    return f"#{r:02X}{g:02X}{b:02X}"


def darken(color: str, amount: int = 20) -> str:
    """Dunkelt eine Hex-Farbe ab."""
    r = max(0, int(color[1:3], 16) - amount)
    g = max(0, int(color[3:5], 16) - amount)
    b = max(0, int(color[5:7], 16) - amount)
    return f"#{r:02X}{g:02X}{b:02X}"


def build_theme(name: str, display_name: str, colors: dict, dark: bool) -> dict:
    """Baut ein vollstaendiges VS Code Theme aus der Farbpalette."""
    bg = colors["background"]
    fg = colors["foreground"]
    primary = colors["primary"]
    secondary = colors["secondary"]
    accent = colors["accent"]
    surface = colors["surface"]
    panel = colors["panel"]
    warning = colors["warning"]
    error = colors["error"]
    success = colors["success"]

    # Abgeleitete Farben
    border = lighten(panel, 15) if dark else darken(panel, 15)
    line_highlight = hex_alpha(accent, "15") if dark else hex_alpha(accent, "10")
    selection = hex_alpha(accent, "40")
    find_highlight = hex_alpha(warning, "55")
    inactive_fg = hex_alpha(fg, "80")
    comment_color = hex_alpha(fg, "70") if dark else hex_alpha(fg, "90")
    widget_bg = surface if dark else panel

    return {
        "name": display_name,
        "type": "dark" if dark else "light",
        "colors": {
            # Editor
            "editor.background": bg,
            "editor.foreground": fg,
            "editor.lineHighlightBackground": line_highlight,
            "editor.selectionBackground": selection,
            "editor.inactiveSelectionBackground": hex_alpha(accent, "25"),
            "editor.findMatchBackground": find_highlight,
            "editor.findMatchHighlightBackground": hex_alpha(warning, "33"),
            "editor.wordHighlightBackground": hex_alpha(accent, "25"),
            "editorCursor.foreground": accent,
            "editorWhitespace.foreground": hex_alpha(fg, "20"),
            "editorIndentGuide.background": hex_alpha(fg, "15"),
            "editorIndentGuide.activeBackground": hex_alpha(fg, "30"),
            "editorLineNumber.foreground": inactive_fg,
            "editorLineNumber.activeForeground": fg,
            "editorBracketMatch.background": hex_alpha(accent, "25"),
            "editorBracketMatch.border": accent,
            "editorGutter.addedBackground": success,
            "editorGutter.modifiedBackground": primary,
            "editorGutter.deletedBackground": error,
            "editorOverviewRuler.errorForeground": error,
            "editorOverviewRuler.warningForeground": warning,

            # Editor widget (find/replace, suggest)
            "editorWidget.background": widget_bg,
            "editorWidget.foreground": fg,
            "editorWidget.border": border,
            "editorSuggestWidget.background": widget_bg,
            "editorSuggestWidget.border": border,
            "editorSuggestWidget.foreground": fg,
            "editorSuggestWidget.selectedBackground": hex_alpha(accent, "30"),

            # Title bar
            "titleBar.activeBackground": panel,
            "titleBar.activeForeground": fg,
            "titleBar.inactiveBackground": darken(panel, 10) if dark else lighten(panel, 10),
            "titleBar.inactiveForeground": inactive_fg,

            # Activity bar (links)
            "activityBar.background": panel,
            "activityBar.foreground": fg,
            "activityBar.inactiveForeground": inactive_fg,
            "activityBarBadge.background": accent,
            "activityBarBadge.foreground": "#FFFFFF" if dark else "#000000",

            # Sidebar
            "sideBar.background": surface,
            "sideBar.foreground": fg,
            "sideBar.border": border,
            "sideBarTitle.foreground": fg,
            "sideBarSectionHeader.background": panel,
            "sideBarSectionHeader.foreground": fg,

            # List (Explorer, Sidebar)
            "list.activeSelectionBackground": hex_alpha(accent, "40"),
            "list.activeSelectionForeground": fg,
            "list.inactiveSelectionBackground": hex_alpha(accent, "20"),
            "list.hoverBackground": hex_alpha(accent, "15"),
            "list.focusOutline": accent,
            "list.highlightForeground": accent,

            # Status bar (unten)
            "statusBar.background": panel,
            "statusBar.foreground": fg,
            "statusBar.border": border,
            "statusBar.debuggingBackground": warning,
            "statusBar.debuggingForeground": "#000000",
            "statusBar.noFolderBackground": darken(panel, 10) if dark else lighten(panel, 10),

            # Tabs
            "tab.activeBackground": bg,
            "tab.activeForeground": fg,
            "tab.inactiveBackground": surface,
            "tab.inactiveForeground": inactive_fg,
            "tab.border": border,
            "tab.activeBorderTop": accent,
            "editorGroupHeader.tabsBackground": surface,
            "editorGroupHeader.tabsBorder": border,

            # Panel (Terminal, Output)
            "panel.background": panel,
            "panel.foreground": fg,
            "panel.border": border,
            "panelTitle.activeBorder": accent,
            "panelTitle.activeForeground": fg,
            "panelTitle.inactiveForeground": inactive_fg,

            # Terminal
            "terminal.background": bg,
            "terminal.foreground": fg,
            "terminalCursor.foreground": accent,

            # Input (Suchfeld etc.)
            "input.background": darken(bg, 10) if dark else lighten(bg, 10),
            "input.foreground": fg,
            "input.border": border,
            "input.placeholderForeground": inactive_fg,
            "focusBorder": accent,
            "inputOption.activeBorder": accent,

            # Dropdown
            "dropdown.background": widget_bg,
            "dropdown.foreground": fg,
            "dropdown.border": border,

            # Button
            "button.background": accent,
            "button.foreground": "#FFFFFF" if dark else "#000000",
            "button.hoverBackground": lighten(accent, 15),

            # Badge
            "badge.background": accent,
            "badge.foreground": "#FFFFFF" if dark else "#000000",

            # Scrollbar
            "scrollbar.shadow": hex_alpha("#000000", "40"),
            "scrollbarSlider.background": hex_alpha(fg, "15"),
            "scrollbarSlider.hoverBackground": hex_alpha(fg, "25"),
            "scrollbarSlider.activeBackground": hex_alpha(fg, "35"),

            # Minimap
            "minimap.findMatchHighlight": hex_alpha(warning, "80"),
            "minimap.selectionHighlight": hex_alpha(accent, "60"),

            # Breadcrumb
            "breadcrumb.foreground": inactive_fg,
            "breadcrumb.focusForeground": fg,
            "breadcrumb.activeSelectionForeground": fg,

            # Peek view
            "peekView.border": accent,
            "peekViewEditor.background": surface,
            "peekViewResult.background": panel,
            "peekViewTitle.background": panel,

            # Diff editor
            "diffEditor.insertedTextBackground": hex_alpha(success, "20"),
            "diffEditor.removedTextBackground": hex_alpha(error, "20"),

            # Merge
            "merge.currentHeaderBackground": hex_alpha(success, "40"),
            "merge.incomingHeaderBackground": hex_alpha(primary, "40"),

            # Notification
            "notifications.background": widget_bg,
            "notifications.foreground": fg,
            "notifications.border": border,

            # Git decoration
            "gitDecoration.modifiedResourceForeground": primary,
            "gitDecoration.untrackedResourceForeground": success,
            "gitDecoration.deletedResourceForeground": error,
            "gitDecoration.conflictingResourceForeground": warning,
            "gitDecoration.ignoredResourceForeground": inactive_fg,
        },
        "tokenColors": build_token_colors(fg, accent, primary, secondary,
                                           warning, error, success, comment_color, dark),
    }


def build_token_colors(fg, accent, primary, secondary, warning, error, success,
                       comment_color, dark):
    """Baut Syntax-Highlighting Token-Farben."""
    # Syntax-Farben aus der Palette ableiten
    keyword = accent
    string_color = success
    number_color = warning
    function_color = primary
    type_color = secondary if dark else darken(secondary, 20)
    variable_color = fg
    constant_color = lighten(warning, 20) if dark else darken(warning, 20)
    tag_color = accent
    attribute_color = primary

    return [
        {
            "name": "Comment",
            "scope": ["comment", "punctuation.definition.comment"],
            "settings": {"foreground": comment_color, "fontStyle": "italic"},
        },
        {
            "name": "Keyword",
            "scope": ["keyword", "storage.type", "storage.modifier"],
            "settings": {"foreground": keyword},
        },
        {
            "name": "String",
            "scope": ["string", "punctuation.definition.string"],
            "settings": {"foreground": string_color},
        },
        {
            "name": "Number",
            "scope": ["constant.numeric"],
            "settings": {"foreground": number_color},
        },
        {
            "name": "Constant",
            "scope": ["constant.language", "constant.character", "support.constant"],
            "settings": {"foreground": constant_color},
        },
        {
            "name": "Variable",
            "scope": ["variable", "variable.other"],
            "settings": {"foreground": variable_color},
        },
        {
            "name": "Variable parameter",
            "scope": ["variable.parameter"],
            "settings": {"foreground": fg, "fontStyle": "italic"},
        },
        {
            "name": "Function",
            "scope": [
                "entity.name.function",
                "support.function",
                "meta.function-call",
            ],
            "settings": {"foreground": function_color},
        },
        {
            "name": "Type / Class",
            "scope": [
                "entity.name.type",
                "entity.name.class",
                "support.type",
                "support.class",
            ],
            "settings": {"foreground": type_color},
        },
        {
            "name": "Tag (HTML/XML)",
            "scope": ["entity.name.tag", "punctuation.definition.tag"],
            "settings": {"foreground": tag_color},
        },
        {
            "name": "Attribute",
            "scope": ["entity.other.attribute-name"],
            "settings": {"foreground": attribute_color, "fontStyle": "italic"},
        },
        {
            "name": "Operator",
            "scope": ["keyword.operator"],
            "settings": {"foreground": fg},
        },
        {
            "name": "Punctuation",
            "scope": ["punctuation"],
            "settings": {"foreground": fg},
        },
        {
            "name": "Decorator / Annotation",
            "scope": [
                "meta.decorator",
                "punctuation.decorator",
                "storage.type.annotation",
            ],
            "settings": {"foreground": warning},
        },
        {
            "name": "Namespace / Module",
            "scope": ["entity.name.namespace", "entity.name.module"],
            "settings": {"foreground": type_color},
        },
        {
            "name": "Property",
            "scope": [
                "variable.other.property",
                "variable.other.object.property",
                "support.variable.property",
            ],
            "settings": {"foreground": primary},
        },
        {
            "name": "Invalid",
            "scope": ["invalid", "invalid.illegal"],
            "settings": {"foreground": error},
        },
        {
            "name": "Markup heading",
            "scope": ["markup.heading", "entity.name.section"],
            "settings": {"foreground": accent, "fontStyle": "bold"},
        },
        {
            "name": "Markup bold",
            "scope": ["markup.bold"],
            "settings": {"fontStyle": "bold"},
        },
        {
            "name": "Markup italic",
            "scope": ["markup.italic"],
            "settings": {"fontStyle": "italic"},
        },
        {
            "name": "Markup link",
            "scope": ["markup.underline.link", "string.other.link"],
            "settings": {"foreground": primary},
        },
        {
            "name": "Markup code",
            "scope": ["markup.inline.raw", "markup.fenced_code"],
            "settings": {"foreground": string_color},
        },
        {
            "name": "Inserted",
            "scope": ["markup.inserted"],
            "settings": {"foreground": success},
        },
        {
            "name": "Deleted",
            "scope": ["markup.deleted"],
            "settings": {"foreground": error},
        },
        {
            "name": "Changed",
            "scope": ["markup.changed"],
            "settings": {"foreground": warning},
        },
    ]


# ── Theme-Definitionen (aus textual-themes) ──────────────────────────

THEMES = [
    ("c64", "Retro — C64", True, {
        "primary": "#6C6CD6", "secondary": "#352879", "accent": "#6C6CD6",
        "foreground": "#D0D0FF", "background": "#352879", "surface": "#423498",
        "panel": "#2C2068", "warning": "#A87832", "error": "#CC5555", "success": "#68A941",
    }),
    ("amiga", "Retro — Amiga Workbench", True, {
        "primary": "#FF8800", "secondary": "#0055AA", "accent": "#FF8800",
        "foreground": "#FFFFFF", "background": "#0055AA", "surface": "#0066BB",
        "panel": "#004499", "warning": "#FFAA00", "error": "#FF4444", "success": "#44BB44",
    }),
    ("atari-st", "Retro — Atari ST GEM", False, {
        "primary": "#007700", "secondary": "#555555", "accent": "#009900",
        "foreground": "#111111", "background": "#E8E8E8", "surface": "#F2F2F2",
        "panel": "#DDDDDD", "warning": "#AA8800", "error": "#CC0000", "success": "#007700",
    }),
    ("ibm-terminal", "Retro — IBM Terminal", True, {
        "primary": "#33FF33", "secondary": "#1A8C1A", "accent": "#33FF33",
        "foreground": "#33FF33", "background": "#0A0A0A", "surface": "#111111",
        "panel": "#0D0D0D", "warning": "#22BB22", "error": "#FF3333", "success": "#33FF33",
    }),
    ("nextstep", "Retro — NeXTSTEP", True, {
        "primary": "#9966CC", "secondary": "#555555", "accent": "#9966CC",
        "foreground": "#E0E0E0", "background": "#2A2A2A", "surface": "#3A3A3A",
        "panel": "#222222", "warning": "#CC9933", "error": "#CC4444", "success": "#44AA44",
    }),
    ("beos", "Retro — BeOS", True, {
        "primary": "#FFD800", "secondary": "#5F5F5F", "accent": "#FFD800",
        "foreground": "#E8E8E8", "background": "#3A3A4A", "surface": "#4A4A5A",
        "panel": "#333344", "warning": "#FF9900", "error": "#DD3333", "success": "#33BB33",
    }),
    ("ubuntu", "Retro — Ubuntu", True, {
        "primary": "#E95420", "secondary": "#4A1942", "accent": "#E95420",
        "foreground": "#EEEEEE", "background": "#300A24", "surface": "#3B1530",
        "panel": "#280820", "warning": "#F99B11", "error": "#DF382C", "success": "#38B44A",
    }),
    ("macos", "Retro — macOS", False, {
        "primary": "#007AFF", "secondary": "#5856D6", "accent": "#007AFF",
        "foreground": "#1D1D1F", "background": "#F5F5F7", "surface": "#FFFFFF",
        "panel": "#E8E8ED", "warning": "#FF9500", "error": "#FF3B30", "success": "#34C759",
    }),
    ("windows-xp", "Retro — Windows XP", True, {
        "primary": "#0054E3", "secondary": "#21A121", "accent": "#0054E3",
        "foreground": "#FFFFFF", "background": "#003399", "surface": "#0044AA",
        "panel": "#002D8A", "warning": "#FFCC00", "error": "#E81123", "success": "#21A121",
    }),
    ("msdos", "Retro — MS-DOS", True, {
        "primary": "#00AAAA", "secondary": "#AAAA00", "accent": "#FFFF55",
        "foreground": "#AAAAAA", "background": "#0000AA", "surface": "#0000BB",
        "panel": "#000088", "warning": "#AAAA00", "error": "#FF5555", "success": "#55FF55",
    }),
    ("plan9", "Retro — Plan 9", False, {
        "primary": "#228844", "secondary": "#4488AA", "accent": "#228844",
        "foreground": "#111111", "background": "#FFFFEA", "surface": "#EAFFFF",
        "panel": "#D5E8D0", "warning": "#BB8800", "error": "#CC2222", "success": "#228844",
    }),
    ("solaris-cde", "Retro — Solaris CDE", True, {
        "primary": "#CC9966", "secondary": "#5F7B8A", "accent": "#CC9966",
        "foreground": "#D8D0C8", "background": "#3A4A5A", "surface": "#455565",
        "panel": "#303F4F", "warning": "#CCAA44", "error": "#CC5544", "success": "#55AA66",
    }),
    ("os2-warp", "Retro — OS/2 Warp", True, {
        "primary": "#00BBBB", "secondary": "#3333AA", "accent": "#00BBBB",
        "foreground": "#D0D0D0", "background": "#1A1A4E", "surface": "#25255E",
        "panel": "#141442", "warning": "#DDAA22", "error": "#DD4444", "success": "#44BB66",
    }),
    ("opensuse", "Retro — openSUSE", True, {
        "primary": "#73BA25", "secondary": "#35B9AB", "accent": "#73BA25",
        "foreground": "#EEEEEE", "background": "#173F0F", "surface": "#1E4D15",
        "panel": "#12330B", "warning": "#F0A30A", "error": "#DD3333", "success": "#73BA25",
    }),
    ("linux-mint", "Retro — Linux Mint", True, {
        "primary": "#8BB158", "secondary": "#6DAB76", "accent": "#8BB158",
        "foreground": "#E8E8E8", "background": "#2B2B2B", "surface": "#363636",
        "panel": "#232323", "warning": "#E5A50A", "error": "#CC3333", "success": "#8BB158",
    }),
]


def main() -> None:
    os.makedirs("themes", exist_ok=True)
    for filename, display_name, dark, colors in THEMES:
        theme = build_theme(filename, display_name, colors, dark)
        path = os.path.join("themes", f"{filename}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(theme, f, indent=2, ensure_ascii=False)
        print(f"  {path}")
    print(f"\n{len(THEMES)} Themes generiert.")


if __name__ == "__main__":
    main()
