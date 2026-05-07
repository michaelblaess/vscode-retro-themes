"""Generiert VS Code Theme-Dateien aus den textual-themes Farbpaletten.

Einmalig ausfuehren: python generate-themes.py
Erzeugt JSON-Dateien im themes/ Ordner.

Die Theme-Slugs, Display-Namen und Farbwerte sind 1:1 die der
textual-themes Library — einmal Pinsel anfassen, beide Welten
bekommen das gleiche Bild.
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


# ── Theme-Definitionen (mirror von textual-themes 0.5) ────────────────
# Reihenfolge: (slug, display_name, dark, palette)
# palette keys: primary, secondary, accent, foreground, background,
#               surface, panel, warning, error, success

THEMES = [
    ("brotkasten", "Retro — Brotkasten", True, {
        "primary": "#7C70DA", "secondary": "#3A2B8A", "accent": "#EDF171",
        "foreground": "#D0CCFF", "background": "#3A2B8A", "surface": "#5446B8",
        "panel": "#241870", "warning": "#EDF171", "error": "#C46C71", "success": "#A9FF9F",
    }),
    ("boing", "Retro — Boing", True, {
        "primary": "#FF8800", "secondary": "#0055AA", "accent": "#FF8800",
        "foreground": "#FFFFFF", "background": "#0055AA", "surface": "#0066BB",
        "panel": "#004499", "warning": "#FFAA00", "error": "#FF4444", "success": "#44BB44",
    }),
    ("gemstone", "Retro — Gemstone", False, {
        "primary": "#007700", "secondary": "#555555", "accent": "#009900",
        "foreground": "#111111", "background": "#E8E8E8", "surface": "#F2F2F2",
        "panel": "#DDDDDD", "warning": "#AA8800", "error": "#CC0000", "success": "#007700",
    }),
    ("classic-terminal", "Retro — Classic Terminal", True, {
        "primary": "#33FF33", "secondary": "#2A7A2A", "accent": "#88FF88",
        "foreground": "#33FF33", "background": "#0A0A0A", "surface": "#162616",
        "panel": "#0F1B0F", "warning": "#FFAA00", "error": "#FF4444", "success": "#33FF33",
    }),
    ("next", "Retro — Next", True, {
        "primary": "#9966CC", "secondary": "#555555", "accent": "#9966CC",
        "foreground": "#E0E0E0", "background": "#2A2A2A", "surface": "#3A3A3A",
        "panel": "#222222", "warning": "#CC9933", "error": "#CC4444", "success": "#44AA44",
    }),
    ("bebox", "Retro — BeBox", True, {
        "primary": "#FFD800", "secondary": "#5F5F5F", "accent": "#FFD800",
        "foreground": "#E8E8E8", "background": "#3A3A4A", "surface": "#4A4A5A",
        "panel": "#333344", "warning": "#FF9900", "error": "#DD3333", "success": "#33BB33",
    }),
    ("bunty", "Retro — Bunty", True, {
        "primary": "#DD4814", "secondary": "#77216F", "accent": "#E18B5C",
        "foreground": "#F2EAEA", "background": "#2C001E", "surface": "#4A2540",
        "panel": "#1F0014", "warning": "#F99B11", "error": "#DF382C", "success": "#38B44A",
    }),
    ("cupertino", "Retro — Cupertino", False, {
        "primary": "#007AFF", "secondary": "#5856D6", "accent": "#007AFF",
        "foreground": "#1D1D1F", "background": "#F5F5F7", "surface": "#FFFFFF",
        "panel": "#E8E8ED", "warning": "#FF9500", "error": "#FF3B30", "success": "#34C759",
    }),
    ("luna", "Retro — Luna", True, {
        "primary": "#0054E3", "secondary": "#21A121", "accent": "#0054E3",
        "foreground": "#FFFFFF", "background": "#003399", "surface": "#0044AA",
        "panel": "#002D8A", "warning": "#FFCC00", "error": "#E81123", "success": "#21A121",
    }),
    ("commandr", "Retro — Commandr", True, {
        "primary": "#FFFF55", "secondary": "#55FFFF", "accent": "#FFFF55",
        "foreground": "#FFFFFF", "background": "#0000AA", "surface": "#1A1ACC",
        "panel": "#000077", "warning": "#FFAA00", "error": "#FF5555", "success": "#55FF55",
    }),
    ("plan9", "Retro — Plan 9", False, {
        "primary": "#228844", "secondary": "#4488AA", "accent": "#228844",
        "foreground": "#111111", "background": "#FFFFEA", "surface": "#EAFFFF",
        "panel": "#D5E8D0", "warning": "#BB8800", "error": "#CC2222", "success": "#228844",
    }),
    ("motif", "Retro — Motif", True, {
        "primary": "#CC9966", "secondary": "#5F7B8A", "accent": "#CC9966",
        "foreground": "#D8D0C8", "background": "#3A4A5A", "surface": "#455565",
        "panel": "#303F4F", "warning": "#CCAA44", "error": "#CC5544", "success": "#55AA66",
    }),
    ("warp", "Retro — Warp", True, {
        "primary": "#00BBBB", "secondary": "#3333AA", "accent": "#00BBBB",
        "foreground": "#D0D0D0", "background": "#1A1A4E", "surface": "#25255E",
        "panel": "#141442", "warning": "#DDAA22", "error": "#DD4444", "success": "#44BB66",
    }),
    ("geeko", "Retro — Geeko", True, {
        "primary": "#73BA25", "secondary": "#35B9AB", "accent": "#73BA25",
        "foreground": "#EEEEEE", "background": "#173F0F", "surface": "#1E4D15",
        "panel": "#12330B", "warning": "#F0A30A", "error": "#DD3333", "success": "#73BA25",
    }),
    ("minty", "Retro — Minty", True, {
        "primary": "#8BB158", "secondary": "#6DAB76", "accent": "#8BB158",
        "foreground": "#E8E8E8", "background": "#2B2B2B", "surface": "#363636",
        "panel": "#232323", "warning": "#E5A50A", "error": "#CC3333", "success": "#8BB158",
    }),
    ("crimson", "Retro — Crimson", True, {
        "primary": "#CC0000", "secondary": "#A30000", "accent": "#EE0000",
        "foreground": "#E0E0E0", "background": "#1A0A0A", "surface": "#2A1515",
        "panel": "#140808", "warning": "#EEA500", "error": "#FF4444", "success": "#44AA44",
    }),
    ("razzy", "Retro — Razzy", True, {
        "primary": "#C51A4A", "secondary": "#6CC24A", "accent": "#C51A4A",
        "foreground": "#EEEEEE", "background": "#1E1E2E", "surface": "#2A2A3A",
        "panel": "#181828", "warning": "#E5A50A", "error": "#DD3333", "success": "#6CC24A",
    }),
    ("beastie", "Retro — Beastie", True, {
        "primary": "#AB2B28", "secondary": "#5E8AAA", "accent": "#AB2B28",
        "foreground": "#D4D4D4", "background": "#1C2028", "surface": "#262A32",
        "panel": "#161A20", "warning": "#CC9933", "error": "#DD4444", "success": "#55AA66",
    }),
    ("fifty-eight", "Retro — Fifty-Eight", True, {
        "primary": "#C9A96E", "secondary": "#6A6A6A", "accent": "#9E1B25",
        "foreground": "#E8C985", "background": "#100C08", "surface": "#1E1914",
        "panel": "#080605", "warning": "#C9A048", "error": "#B8252E", "success": "#6A9A5A",
    }),
    ("bluesy", "Retro — Bluesy", True, {
        "primary": "#D4AF37", "secondary": "#1E4FA0", "accent": "#F0C85A",
        "foreground": "#F5D76E", "background": "#081F54", "surface": "#0E2E6E",
        "panel": "#04133A", "warning": "#E8A838", "error": "#DD3344", "success": "#48B870",
    }),
    ("goldfinder", "Retro — Goldfinder", True, {
        "primary": "#E6B800", "secondary": "#8A6E20", "accent": "#FFD740",
        "foreground": "#E8DFC0", "background": "#080705", "surface": "#18140A",
        "panel": "#040302", "warning": "#E8A838", "error": "#CC4040", "success": "#5AAA5A",
    }),
    ("hulkula", "Retro — Hulkula", True, {
        "primary": "#2BA841", "secondary": "#BCC4CA", "accent": "#4DC962",
        "foreground": "#F0F2EE", "background": "#083C14", "surface": "#104B1B",
        "panel": "#042608", "warning": "#D4A040", "error": "#CC2222", "success": "#4DC962",
    }),
    ("flughund", "Retro — Flughund", True, {
        "primary": "#244B85", "secondary": "#BCC4CA", "accent": "#3D6FB8",
        "foreground": "#F0F2F5", "background": "#060810", "surface": "#0E1422",
        "panel": "#030509", "warning": "#D4A040", "error": "#CC3030", "success": "#50AA50",
    }),
    ("classic-navy", "Retro — Classic Navy", True, {
        "primary": "#C0C5CC", "secondary": "#1E4585", "accent": "#9E3A42",
        "foreground": "#EEF0F5", "background": "#0C2B5C", "surface": "#143465",
        "panel": "#061A3A", "warning": "#D4A040", "error": "#B04048", "success": "#50AA50",
    }),
    ("brick", "Retro — Brick", False, {
        "primary": "#8E2A5E", "secondary": "#5A4858", "accent": "#D63B68",
        "foreground": "#241F28", "background": "#D4CEBC", "surface": "#E2DCCA",
        "panel": "#B2AC9A", "warning": "#C85820", "error": "#A0203A", "success": "#4A7A3A",
    }),
    ("clipper", "Retro — Clipper", False, {
        "primary": "#1A4FA0", "secondary": "#C61F2C", "accent": "#D4222F",
        "foreground": "#1A1A1A", "background": "#F6F3E8", "surface": "#FCFAF0",
        "panel": "#EBE6D4", "warning": "#C88A20", "error": "#C61F2C", "success": "#2E8B3D",
    }),
    ("synthwave", "Retro — Synthwave", True, {
        "primary": "#FF2E93", "secondary": "#7B2D8E", "accent": "#05D9E8",
        "foreground": "#F5E9FF", "background": "#1A0B3D", "surface": "#261553",
        "panel": "#0E0524", "warning": "#FFD319", "error": "#FF3860", "success": "#39FF14",
    }),
    ("miami", "Retro — Miami", True, {
        "primary": "#FF6FAB", "secondary": "#1FB8BC", "accent": "#FFA06A",
        "foreground": "#FFE8E0", "background": "#0B2F3F", "surface": "#124050",
        "panel": "#051825", "warning": "#FFD76B", "error": "#E63970", "success": "#4ECDA8",
    }),
    ("racing", "Retro — Racing", True, {
        "primary": "#1A5CC8", "secondary": "#C0C6D0", "accent": "#E42030",
        "foreground": "#EEF0F5", "background": "#14161E", "surface": "#1F232E",
        "panel": "#080A10", "warning": "#E8A838", "error": "#E42030", "success": "#3AAA4A",
    }),
    ("metropolis", "Retro — Metropolis", True, {
        "primary": "#E02030", "secondary": "#1A5CC8", "accent": "#FFD53B",
        "foreground": "#F0F2F8", "background": "#0A2A5E", "surface": "#123876",
        "panel": "#051838", "warning": "#FFD53B", "error": "#C80A18", "success": "#3AAA4A",
    }),
    ("spiderized", "Retro — Spiderized", True, {
        "primary": "#D71920", "secondary": "#1F75FE", "accent": "#1F75FE",
        "foreground": "#FFFFFF", "background": "#0E1A3A", "surface": "#1A2C5F",
        "panel": "#070D24", "warning": "#FFA830", "error": "#C80A18", "success": "#4AA85A",
    }),
]


def main() -> None:
    os.makedirs("themes", exist_ok=True)

    # Vorhandene JSON-Files in themes/ einsammeln, am Ende die jetzt
    # nicht mehr aktiven loeschen.
    existing = {f for f in os.listdir("themes") if f.endswith(".json")}
    written: set[str] = set()

    for slug, display_name, dark, colors in THEMES:
        theme = build_theme(slug, display_name, colors, dark)
        filename = f"{slug}.json"
        path = os.path.join("themes", filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(theme, f, indent=2, ensure_ascii=False)
        written.add(filename)
        print(f"  + {path}")

    # Veraltete Theme-Files aufraeumen
    stale = sorted(existing - written)
    for f in stale:
        path = os.path.join("themes", f)
        os.remove(path)
        print(f"  - removed {path}")

    print(f"\n{len(THEMES)} Themes generiert ({len(stale)} veraltete entfernt).")


if __name__ == "__main__":
    main()
