from pathlib import Path
import plotly.express as px
import plotly_bootstrap_templates
import pytest
import webbrowser


@pytest.mark.parametrize(
    "theme",
    [v for t in plotly_bootstrap_templates.DBC_TEMPLATES for v in [t, f"{t}_dark"]],
)
def test_plot(theme: str, tmp_path: Path):
    df = px.data.gapminder()
    plotly_bootstrap_templates.load_figure_template(theme)
    file = tmp_path / "plot.html"

    fig = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=theme,
        title=f"Gapminder 2007: '{theme}' theme",
    )
    fig.write_html(file)

    webbrowser.open(str(file))
