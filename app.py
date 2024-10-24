import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Philip's PyShiny Plot", fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_bins", "Number of Bins", 0, 100, 20)

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_bins(), density=True)
    plt.title("Histogram of Random Data")  
