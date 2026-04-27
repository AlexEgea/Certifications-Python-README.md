import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Importar los datos
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# Limpiar los datos eliminando el 2.5% más bajo y el 2.5% más alto
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Copiamos el dataframe para no modificar el original
    df_line = df.copy()

    # Crear figura
    fig, ax = plt.subplots(figsize=(16, 6))

    # Dibujar gráfica de líneas
    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)

    # Títulos y etiquetas obligatorias
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Guardar imagen
    fig.savefig("line_plot.png")

    return fig


def draw_bar_plot():
    # Copiamos el dataframe
    df_bar = df.copy()

    # Crear columnas de año y mes
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Agrupar por año y mes calculando la media
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Dibujar gráfica de barras
    fig = df_bar.plot(
        kind="bar",
        figsize=(12, 8)
    ).figure

    # Configurar gráfica
    ax = fig.axes[0]
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(
        title="Months",
        labels=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    )

    # Guardar imagen
    fig.savefig("bar_plot.png")

    return fig


def draw_box_plot():
    # Copiamos el dataframe
    df_box = df.copy()

    # Crear columnas necesarias
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Orden correcto de los meses
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Crear figura con dos gráficas
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Box plot por año
    sns.boxplot(
        x="year",
        y="value",
        data=df_box,
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Box plot por mes
    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Guardar imagen
    fig.savefig("box_plot.png")

    return fig