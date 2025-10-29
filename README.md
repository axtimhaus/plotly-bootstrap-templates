# Plotly Bootstrap Templates

>>> [!NOTE]
>>> has been forked from <https://github.com/AnnMarieW/dash-bootstrap-templates>. All dependencies on `dash` and `dash-bootstrap-components` have been removed from the installable package to allow usage with plain plotly graphing library without the need to install dash. Package management has been modernized to `uv` and the package code has been cleaned up for the targeted purpose.

## Figure Template Quickstart

> [!TIP]
> Learn more about Plotly figure templates and themes at: <https://plotly.com/python/templates/>

Install the package as usual with your favorite Python package manager, the package name is `plotly-bootstrap-templates`.
Then, use the main package function `load_figure_template` to load the template.
It is automatically stored in the `plotly.io.templates` dictionary.
`plotly.io.templates.default` will be automatically set to the requested template afterwards.

```python
from plotly_bootstrap_templates import load_figure_template

load_figure_template("flatly")
```

You may load several theme at once by giving a list, the default template will then be the first in this list.

```python
load_figure_template(["flatly", "solar"])
```

To get a full list of the available templates, print the `TEMPLATES` constant.
For each of them, also a `*_dark` variant exists, which are listed in the `TEMPLATES_DARK` constant.

```python
from plotly_bootstrap_templates import TEMPLATES, TEMPLATES_DARK

print("templates:\n", TEMPLATES)
print("dark templates:\n", TEMPLATES_DARK)
```

## Development

To create the project virtual environment using `uv` run:

```shell
uv sync
```

To regenerate the template data files, run:

```shell
./_create_templates.py
```

The script is equipped with a respective shebang to tell uv which dependencies to use for that (which are not necessary at runtime of the package).

To run the test suite, use:

```python
uv run pytest
```

This will generate an example plot of the gapminder test data set for every available theme and open the result in your default browser using the `webbrowser` package.

## Further Information

For further reading visit the [original repository](https://github.com/AnnMarieW/dash-bootstrap-templates).
