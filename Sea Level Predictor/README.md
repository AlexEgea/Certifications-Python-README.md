# 🌊 Sea Level Predictor

Proyecto de análisis de datos desarrollado en Python como parte de la certificación **Data Analysis with Python** de freeCodeCamp.

Este proyecto analiza la evolución histórica del nivel del mar y genera una predicción hasta el año 2050 utilizando regresión lineal.

---

## 📌 Descripción

El objetivo del proyecto es visualizar cómo ha cambiado el nivel del mar a lo largo del tiempo y predecir su comportamiento futuro.

Para ello se realiza:

- Representación de los datos reales mediante un gráfico de dispersión.
- Cálculo de una línea de tendencia utilizando todos los datos históricos.
- Cálculo de una segunda línea de tendencia usando únicamente datos desde el año 2000.
- Proyección de ambas tendencias hasta el año 2050.

Esto permite comparar la evolución global frente a la tendencia más reciente.

---

## 🧠 Tecnologías utilizadas

- **Python**
- **Pandas** → Manipulación de datos
- **Matplotlib** → Visualización
- **SciPy** → Regresión lineal
- **Unittest** → Testing

---

## 📁 Estructura del proyecto

```text
Sea Level Predictor/
│
├── epa-sea-level.csv        # Dataset original
├── sea_level_predictor.py   # Lógica principal del proyecto
├── main.py                  # Punto de entrada
├── test_module.py           # Tests automáticos
├── sea_level_plot.png       # Resultado generado
└── README.md

---

## 📊 Dataset

El dataset contiene datos históricos del nivel del mar proporcionados por la EPA.

📥 Fuente oficial:  
https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/main/epa-sea-level.csv

---

## ⚙️ Instalación

### 1. Clonar el repositorio
git clone https://github.com/AlexEgea/python.git

2. Acceder al proyecto
cd "Sea Level Predictor"

3. Crear entorno virtual
python -m venv .venv

4. Activar entorno virtual (Windows)
.venv\Scripts\activate

5. Instalar dependencias
pip install pandas matplotlib scipy