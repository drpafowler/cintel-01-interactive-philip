from shiny.express import input, render, ui
from shinywidgets import render_plotly

ui.page_opts(title="Penguins dashboard", fillable=True)

with ui.sidebar():
    ui.input_selectize(
        "xvar", "Select x-axis variable",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"]
    )
    ui.input_numeric("bins", "Number of bins", 30)

    ui.input_selectize(
        "yvar", "Select y-axis variable",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"]
    )

with ui.card(full_screen=True):
    @render_plotly
    def hist():
        import plotly.express as px
        from palmerpenguins import load_penguins
        return px.histogram(load_penguins(), x=input.xvar(), nbins=input.bins())


with ui.card(full_screen=True):
    @render_plotly
    def scatter():
        import plotly.express as px
        from palmerpenguins import load_penguins
        penguins = load_penguins()
        return px.scatter(penguins, x=input.xvar(), y=input.yvar(), color="species")
