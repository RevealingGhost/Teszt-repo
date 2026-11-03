"""Mood Palettes — matplotlib és plotly téma 3 palettával (Citrus, Electric, Visionary), világos/sötét módban.

Használat:
    from mood_palettes import use, PALETTES
    use("citrus")              # matplotlib + plotly alapértelmezés
    use("electric", mode="dark")

    import plotly.express as px
    px.bar(df, x="kategoria", y="arbevetel")   # automatikusan a téma színeivel

Szabályok röviden:
    - 1 sorozat: series[0]; kiemelés: highlight egy elemre, a többi deemph
    - több sorozat: series fix sorrendben, max 6, felette "Egyéb"
    - mennyiség: seq (7 lépcső); előjel/YoY: div (7 lépcső, div[3] = semleges)
"""
from __future__ import annotations

PALETTES = {
    "citrus": {
        "name": "Citrus",
        "tag": "Friss, energikus, FMCG-polc",
        "mood": {
            "m1": [
                "Mandarin Orange",
                "#FD550A"
            ],
            "m2": [
                "Forest Green",
                "#015D47"
            ],
            "acc": [
                "Crest Yellow",
                "#E0F354"
            ]
        },
        "light": {
            "page": "#f6f4ed",
            "surface": "#fdfcf9",
            "surface2": "#f1efe7",
            "ink": "#10261f",
            "ink2": "#45574f",
            "muted": "#5f6f68",
            "grid": "#e6e3da",
            "axis": "#c8c4b8",
            "band": "#015D47",
            "bandInk": "#ffffff",
            "bandAccent": "#E0F354",
            "accentInk": "#10261f",
            "highlight": "#fd550a",
            "deemph": "#cdd0c6",
            "series": [
                "#097b5d",
                "#fd550a",
                "#1f7dcf",
                "#b53c7f",
                "#b08509",
                "#0794a0"
            ],
            "mid": "#efede6",
            "seq": [
                "#c1f6e0",
                "#94e0c3",
                "#65c7a4",
                "#32a984",
                "#068968",
                "#06684e",
                "#024936"
            ],
            "divNeg": [
                "#ac3401",
                "#e75623",
                "#fea386"
            ],
            "divPos": [
                "#057558",
                "#25a37e",
                "#64d6af"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#0a7a0a",
            "badText": "#b52a2a"
        },
        "dark": {
            "page": "#02140d",
            "surface": "#061f17",
            "surface2": "#0b2a20",
            "ink": "#eef5f0",
            "ink2": "#b8cac1",
            "muted": "#8ea399",
            "grid": "#16352a",
            "axis": "#2c4d40",
            "band": "#015D47",
            "bandInk": "#ffffff",
            "bandAccent": "#E0F354",
            "accentInk": "#10261f",
            "highlight": "#E0F354",
            "deemph": "#3a5a4d",
            "series": [
                "#129a75",
                "#fa5617",
                "#2b87d9",
                "#ca5091",
                "#bb8d13",
                "#149eab"
            ],
            "mid": "#2a4a3e",
            "seq": [
                "#024936",
                "#06684e",
                "#068968",
                "#32a984",
                "#65c7a4",
                "#94e0c3",
                "#c1f6e0"
            ],
            "divNeg": [
                "#fd835d",
                "#d9480f",
                "#8f2c05"
            ],
            "divPos": [
                "#4fc39c",
                "#089772",
                "#026249"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#3fcf3f",
            "badText": "#ff7b7b"
        }
    },
    "electric": {
        "name": "Electric",
        "tag": "Digitális, tech, éjszakai",
        "mood": {
            "m1": [
                "Onyx Black",
                "#01010D"
            ],
            "m2": [
                "Electric Indigo",
                "#6331FB"
            ],
            "acc": [
                "Tropical Mint",
                "#88F9C0"
            ]
        },
        "light": {
            "page": "#f4f3fd",
            "surface": "#fdfdff",
            "surface2": "#efeefb",
            "ink": "#0e0c22",
            "ink2": "#47446a",
            "muted": "#625f85",
            "grid": "#e6e4f4",
            "axis": "#c7c4de",
            "band": "#6331FB",
            "bandInk": "#ffffff",
            "bandAccent": "#88F9C0",
            "accentInk": "#01010D",
            "highlight": "#16a56e",
            "deemph": "#cfcde0",
            "series": [
                "#6331fb",
                "#16a56e",
                "#ca8409",
                "#cd489d",
                "#088ec4",
                "#e05b4a"
            ],
            "mid": "#edecf5",
            "seq": [
                "#e4e6ff",
                "#c6c8fe",
                "#a6a6fe",
                "#867efd",
                "#6b4afe",
                "#5228d4",
                "#39169c"
            ],
            "divNeg": [
                "#af2c1f",
                "#e05b4a",
                "#ffa192"
            ],
            "divPos": [
                "#5c38e3",
                "#8075fc",
                "#b4b5fe"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#0a7a0a",
            "badText": "#b52a2a"
        },
        "dark": {
            "page": "#01010D",
            "surface": "#0a091d",
            "surface2": "#121029",
            "ink": "#f2f1ff",
            "ink2": "#c1bee3",
            "muted": "#9a96c0",
            "grid": "#1c1a38",
            "axis": "#33305a",
            "band": "#6331FB",
            "bandInk": "#ffffff",
            "bandAccent": "#88F9C0",
            "accentInk": "#01010D",
            "highlight": "#88F9C0",
            "deemph": "#36345a",
            "series": [
                "#7766ff",
                "#16a56e",
                "#ca8409",
                "#d852a6",
                "#0097d2",
                "#e05b4a"
            ],
            "mid": "#2b2945",
            "seq": [
                "#39169c",
                "#5228d4",
                "#6b4afe",
                "#867efd",
                "#a6a6fe",
                "#c6c8fe",
                "#e4e6ff"
            ],
            "divNeg": [
                "#fd816e",
                "#d24e3e",
                "#9b1207"
            ],
            "divPos": [
                "#9f9ffd",
                "#7562fc",
                "#4e1cce"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#3fcf3f",
            "badText": "#ff7b7b"
        }
    },
    "visionary": {
        "name": "Visionary",
        "tag": "Nyugodt, prémium, vezetői",
        "mood": {
            "m1": [
                "Seal Blue",
                "#DBF2FC"
            ],
            "m2": [
                "Navy Blue",
                "#072D59"
            ],
            "acc": [
                "Crimson Pink",
                "#FD6E88"
            ]
        },
        "light": {
            "page": "#DBF2FC",
            "surface": "#f8fdff",
            "surface2": "#eaf6fc",
            "ink": "#072D59",
            "ink2": "#3a5677",
            "muted": "#4f6886",
            "grid": "#dcebf3",
            "axis": "#b6cbd9",
            "band": "#072D59",
            "bandInk": "#DBF2FC",
            "bandAccent": "#FD6E88",
            "accentInk": "#072D59",
            "highlight": "#e74d6f",
            "deemph": "#c3d3df",
            "series": [
                "#1157a4",
                "#e74d6f",
                "#08978b",
                "#8951bf",
                "#cc8310",
                "#109ac2"
            ],
            "mid": "#e6eef3",
            "seq": [
                "#d9eaff",
                "#add1fe",
                "#7ab4fe",
                "#5494e4",
                "#3475c4",
                "#1c589d",
                "#0e3d72"
            ],
            "divNeg": [
                "#b51448",
                "#e74d6f",
                "#ff9eab"
            ],
            "divPos": [
                "#2063b0",
                "#4c8edf",
                "#92c1fe"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#0a7a0a",
            "badText": "#b52a2a"
        },
        "dark": {
            "page": "#00112b",
            "surface": "#041b39",
            "surface2": "#0a2547",
            "ink": "#DBF2FC",
            "ink2": "#a8c2d8",
            "muted": "#8099b4",
            "grid": "#123055",
            "axis": "#24476f",
            "band": "#0c3b70",
            "bandInk": "#DBF2FC",
            "bandAccent": "#FD6E88",
            "accentInk": "#072D59",
            "highlight": "#FD6E88",
            "deemph": "#2c4a6c",
            "series": [
                "#3a7bcb",
                "#f15778",
                "#14a195",
                "#9b63d3",
                "#c07b05",
                "#109ac2"
            ],
            "mid": "#2a4566",
            "seq": [
                "#0e3d72",
                "#1c589d",
                "#3475c4",
                "#5494e4",
                "#7ab4fe",
                "#add1fe",
                "#d9eaff"
            ],
            "divNeg": [
                "#fd7c92",
                "#d83f64",
                "#9a043a"
            ],
            "divPos": [
                "#6dadff",
                "#4081d2",
                "#07519d"
            ],
            "good": "#0ca30c",
            "warning": "#fab219",
            "serious": "#ec835a",
            "critical": "#d03b3b",
            "goodText": "#3fcf3f",
            "badText": "#ff7b7b"
        }
    }
}


def tokens(name: str = "citrus", mode: str = "light") -> dict:
    """Egy téma egy módjának összes tokenje (dict)."""
    return PALETTES[name][mode]


def use(name: str = "citrus", mode: str = "light") -> dict:
    """Beállítja a matplotlib rcParams-ot és (ha telepítve van) a plotly alap template-et."""
    t = tokens(name, mode)
    try:
        import matplotlib as mpl
        from cycler import cycler
        mpl.rcParams.update({
            "figure.facecolor": t["surface"], "axes.facecolor": t["surface"], "savefig.facecolor": t["surface"],
            "axes.edgecolor": t["axis"], "axes.labelcolor": t["ink2"], "axes.titlecolor": t["ink"],
            "axes.titleweight": "semibold", "axes.titlesize": 13, "axes.titlelocation": "left",
            "axes.prop_cycle": cycler(color=t["series"]),
            "axes.grid": True, "axes.grid.axis": "y", "grid.color": t["grid"], "grid.linestyle": "-", "grid.linewidth": 1,
            "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
            "xtick.color": t["muted"], "ytick.color": t["muted"], "text.color": t["ink"],
            "lines.linewidth": 2, "lines.solid_capstyle": "round", "lines.markersize": 6,
            "legend.frameon": False, "legend.labelcolor": t["ink2"],
            "font.family": ["Instrument Sans", "Segoe UI", "DejaVu Sans", "sans-serif"],
        })
    except ImportError:
        pass
    try:
        import plotly.graph_objects as go
        import plotly.io as pio
        axis = dict(gridcolor=t["grid"], linecolor=t["axis"], zerolinecolor=t["axis"], tickfont=dict(color=t["muted"]), title=dict(font=dict(color=t["ink2"])))
        pio.templates["mood"] = go.layout.Template(layout=dict(
            colorway=t["series"], paper_bgcolor=t["surface"], plot_bgcolor=t["surface"],
            font=dict(family="Instrument Sans, Segoe UI, sans-serif", color=t["ink"]),
            title=dict(font=dict(color=t["ink"], size=16), x=0, xanchor="left"),
            xaxis={**axis, "showgrid": False}, yaxis=axis,
            legend=dict(font=dict(color=t["ink2"])),
            colorscale=dict(sequential=[[i / 6, c] for i, c in enumerate(t["seq"])],
                            diverging=[[i / 6, c] for i, c in enumerate([*t["divNeg"], t["mid"], *reversed(t["divPos"])])]),
            hoverlabel=dict(bgcolor=t["surface"], font=dict(color=t["ink"]), bordercolor=t["grid"]),
        ))
        pio.templates.default = "mood"
    except ImportError:
        pass
    return t


def highlight_colors(categories, focus, name: str = "citrus", mode: str = "light") -> list[str]:
    """Kiemeléses diagramhoz: a focus elem highlight színt kap, a többi deemph-et."""
    t = tokens(name, mode)
    focus = {focus} if isinstance(focus, str) else set(focus)
    return [t["highlight"] if c in focus else t["deemph"] for c in categories]
