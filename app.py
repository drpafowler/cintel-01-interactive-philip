import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Philip's PyShiny Plot", fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_bins", "Number of Bins", 0, 100, 20)
    ui.input_slider("selected_number_samples", "Number of Samples", 100, 10000, 1000)
    ui.input_select("selected_distribution", "Select Distribution", {
        "standard_normal": "Standard Normal",
        "standard_t": "Standard T",
        "power": "Power",
        "poisson": "Poisson",
        "normal": "Normal",
        "lognormal": "Lognormal",
        "logistic": "Logistic",
        "laplace": "Laplace",
        "geometric": "Geometric",
        "binomial": "Binomial",
        "logseries": "Logseries",
        "uniform": "Uniform"
    })

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    dist = input.selected_distribution()
    size = input.selected_number_samples()  
    if dist == "standard_normal":
        x = np.random.standard_normal(size)
    elif dist == "standard_t":
        x = np.random.standard_t(df=10, size=size)
    elif dist == "power":
        x = np.random.power(a=5, size=size)
    elif dist == "poisson":
        x = np.random.poisson(lam=5, size=size)
    elif dist == "normal":
        x = np.random.normal(loc=0, scale=1, size=size)
    elif dist == "lognormal":
        x = np.random.lognormal(mean=0, sigma=1, size=size)
    elif dist == "logistic":
        x = np.random.logistic(loc=0, scale=1, size=size)
    elif dist == "laplace":
        x = np.random.laplace(loc=0, scale=1, size=size)
    elif dist == "geometric":
        x = np.random.geometric(p=0.5, size=size)
    elif dist == "binomial":
        x = np.random.binomial(n=100, p=0.5, size=size)
    elif dist == "logseries":
        x = np.random.logseries(p=0.5, size=size)
    elif dist == "uniform":
        x = np.random.uniform(low=0, high=1, size=size)
    else:
        x = np.random.standard_normal(size)  
        
    plt.hist(x, input.selected_number_bins(), density=True)
    plt.title(f"Histogram of {input.selected_distribution().replace('_', ' ').title()} Distribution")