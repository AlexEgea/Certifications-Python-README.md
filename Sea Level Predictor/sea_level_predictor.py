import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Leer datos
    df = pd.read_csv("epa-sea-level.csv")

    # Crear figura
    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Línea de mejor ajuste (todos los datos)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_all = list(range(1880, 2051))
    sea_levels_all = [
        res_all.slope * year + res_all.intercept for year in years_all
    ]

    ax.plot(years_all, sea_levels_all)

    # Línea de mejor ajuste desde el 2000
    df_2000 = df[df["Year"] >= 2000]

    res_2000 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000 = list(range(2000, 2051))
    sea_levels_2000 = [
        res_2000.slope * year + res_2000.intercept for year in years_2000
    ]

    ax.plot(years_2000, sea_levels_2000)

    # Etiquetas
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Guardar imagen
    plt.savefig("sea_level_plot.png")

    return ax