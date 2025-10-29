import json
from typing import List
import plotly.io as pio
from importlib.resources import files

TEMPLATES = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "cyborg",
    "darkly",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "morph",
    "pulse",
    "quartz",
    "sandstone",
    "simplex",
    "sketchy",
    "slate",
    "solar",
    "spacelab",
    "superhero",
    "united",
    "vapor",
    "yeti",
    "zephyr",
    "vizro",
]

TEMPLATES_DARK = [f"{t}_dark" for t in TEMPLATES]


def read_template(theme):
    try:
        with (
            files("plotly_bootstrap_templates") / "templates" / f"{theme}.json"
        ).open() as f:
            template = json.load(f)
    except IOError:
        with (
            files("plotly_bootstrap_templates") / "templates" / "bootstrap.json"
        ).open() as f:
            template = json.load(f)
    pio.templates[theme] = template


def load_figure_template(themes: List[str] | str = "bootstrap"):
    """Add figure template to plotly.io and sets the default template

    Keyword arguments:
    themes -- may be a string or list of strings. (Default "bootstrap")
              - The string is the lowercase name of a Bootstrap theme
              "all" will load all 52 themes.

    The plotly.io.templates.default will be the first theme if
    themes is a list. If the themes attribute is invalid, the
    "bootstrap" theme will be used.
    """
    if isinstance(themes, list):
        for theme in themes:
            read_template(theme)
        pio.templates.default = themes[0]

    elif themes == "all":
        for theme in TEMPLATES + TEMPLATES_DARK:
            read_template(theme)
        pio.templates.default = "bootstrap"

    else:
        read_template(themes)
        pio.templates.default = themes
