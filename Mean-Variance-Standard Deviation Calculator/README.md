# 📊 Mean-Variance-Standard Deviation Calculator

Proyecto desarrollado como parte de la certificación **Python for Data Analysis** de freeCodeCamp.

---

## 📌 Descripción

Este proyecto implementa una función que calcula:

* Media (Mean)
* Varianza (Variance)
* Desviación estándar (Standard Deviation)
* Máximo (Max)
* Mínimo (Min)
* Suma (Sum)

A partir de una lista de 9 números, transformándola en una matriz 3x3 usando **NumPy**.

---

## 🧠 Funcionamiento

La función:

```python
calculate([0,1,2,3,4,5,6,7,8])
```

Devuelve un diccionario con estadísticas calculadas:

```python
{
  'mean': [[...], [...], ...],
  'variance': [[...], [...], ...],
  'standard deviation': [[...], [...], ...],
  'max': [[...], [...], ...],
  'min': [[...], [...], ...],
  'sum': [[...], [...], ...]
}
```

---

## ⚙️ Tecnologías utilizadas

* Python
* NumPy

---

## 📁 Estructura

```bash
mean-variance-calculator/
│
├── mean_var_std.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Ejecución

```bash
python main.py
```

---

## ⚠️ Requisitos

```bash
pip install -r requirements.txt
```

---

## 🧪 Validación

La función:

* ✔ Acepta solo listas de 9 elementos
* ❌ Lanza error si no cumple

```python
ValueError: List must contain nine numbers.
```

---

## 📈 Habilidades demostradas

* Uso de NumPy
* Operaciones matriciales
* Cálculo de estadísticas
* Validación de datos
* Estructuración de resultados

---

## 👨‍💻 Autor

**Alejandro Aguilera**
🔗 https://github.com/AlexEgea
