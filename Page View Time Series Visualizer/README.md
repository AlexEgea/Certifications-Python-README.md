# 📊 Page View Time Series Visualizer

Proyecto de análisis de datos desarrollado en Python que visualiza las visitas diarias del foro de freeCodeCamp mediante diferentes tipos de gráficas.

---

## 🚀 Descripción

Este proyecto analiza un dataset de visitas diarias y genera tres visualizaciones clave:

* 📈 **Line Plot** → evolución de visitas en el tiempo
* 📊 **Bar Plot** → media mensual agrupada por años
* 📦 **Box Plots** → distribución por año y por mes

Se aplican técnicas de limpieza de datos eliminando valores extremos para obtener resultados más precisos.

---

## 🛠️ Tecnologías utilizadas

* Python 🐍
* Pandas
* Matplotlib
* Seaborn

---

## 📂 Estructura del proyecto

```
Page View Time Series Visualizer/
│
├── fcc-forum-pageviews.csv
├── time_series_visualizer.py
├── main.py
├── test_module.py
├── line_plot.png
├── bar_plot.png
├── box_plot.png
└── README.md
```

---

## 📥 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/AlexEgea/python.git
cd "Page View Time Series Visualizer"
```

2. Crea un entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
```

3. Instala dependencias:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ Uso

Ejecuta el proyecto con:

```bash
python main.py
```

Se generarán automáticamente:

* `line_plot.png`
* `bar_plot.png`
* `box_plot.png`

---

## 🧪 Tests

Para ejecutar los tests:

```bash
python -m unittest test_module.py
```

---

## 🧹 Limpieza de datos

Se eliminan los valores extremos:

* 2.5% inferior
* 2.5% superior

Esto mejora la calidad de las visualizaciones.

---

## 📸 Resultados

### 📈 Line Plot

Visualiza la evolución de visitas diarias a lo largo del tiempo.

### 📊 Bar Plot

Muestra la media de visitas mensuales agrupadas por año.

### 📦 Box Plots

* Tendencia por año
* Estacionalidad por mes

---

## 🎯 Objetivo

Proyecto realizado como parte de la certificación de **Data Analysis with Python** de freeCodeCamp.

---

## 👨‍💻 Autor

**Alejandro Aguilera**
🔗 https://github.com/AlexEgea

---

## ⭐ Notas

* Dataset oficial de freeCodeCamp
* Proyecto orientado a análisis y visualización de datos
* Código estructurado y testeado

---
