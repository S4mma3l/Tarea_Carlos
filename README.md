# Análisis de Regresión Lineal: Horas de Estudio vs. Nota de Examen

Este documento detalla el análisis de regresión lineal realizado para determinar la relación entre las **horas semanales de estudio** y la **nota obtenida en el examen final**.

## a) Diagrama de Dispersión

Un diagrama de dispersión es una herramienta gráfica que nos permite visualizar la relación entre dos variables cuantitativas. Cada punto en el gráfico representa un par de valores (en este caso, horas de estudio y nota del examen para un estudiante).

![Diagrama de Dispersión con Datos Reales](diagrama_dispersion_real.png)

**Observación:** El gráfico muestra una tendencia positiva. A medida que las horas de estudio aumentan, las notas del examen tienden a ser más altas, lo que sugiere una **relación lineal positiva**.

---

## b) Ecuación de Regresión

El objetivo es encontrar la línea recta que mejor se ajuste a los datos. Esta línea, llamada línea de regresión, se describe con la siguiente ecuación:

$$\hat{y} = b_0 + b_1 x$$

Donde:
- $\hat{y}$ es la **nota del examen pronosticada**.
- $x$ son las **horas de estudio**.
- $b_0$ es la **intersección** con el eje Y (la nota pronosticada si se estudiaran 0 horas).
- $b_1$ es la **pendiente** de la línea (cuánto aumenta la nota por cada hora adicional de estudio).

Las fórmulas para calcular los coeficientes son:
- **Pendiente ($b_1$)**: $b_1 = \frac{\sum(x_i -  ar{x})(y_i -  ar{y})}{\sum(x_i -  ar{x})^2}$
- **Intersección ($b_0$)**: $b_0 =  ar{y} - b_1  ar{x}$

Para los datos proporcionados, la ecuación de regresión resultante es:

**Nota del Examen = 25.80 + 3.61 * (Horas de Estudio)**

---

## c) Pronóstico

Una vez que tenemos la ecuación de regresión, podemos usarla para pronosticar la nota esperada para un número de horas de estudio que no estaba en nuestros datos originales.

**Fórmula:**
$$\hat{y}_{nuevo} = b_0 + b_1 x_{nuevo}$$

Para un estudiante que invierte **17 horas** de estudio semanales ($x=17$):

- **Nota Pronosticada**: 87.25

---

## d) Coeficiente de Correlación

El **coeficiente de correlación de Pearson ($r$)** es una medida numérica que cuantifica la fuerza y la dirección de la relación lineal entre dos variables. Su valor varía entre -1 y +1.

- **+1**: Correlación lineal positiva perfecta.
- **-1**: Correlación lineal negativa perfecta.
- **0**: Sin correlación lineal.

**Fórmula:**
$$r = \frac{\sum(x_i -  ar{x})(y_i -  ar{y})}{\sqrt{\sum(x_i -  ar{x})^2 \sum(y_i -  ar{y})^2}}$$

El coeficiente de correlación para estos datos es:

- **$r  pprox$ 0.843**

Este valor cercano a 1 indica una **correlación lineal positiva fuerte**, lo que confirma la observación del diagrama de dispersión.

---

## e) Error Estándar de la Estimación

El **error estándar de la estimación ($S_e$)** mide la dispersión promedio de los puntos de datos reales con respecto a la línea de regresión. En otras palabras, nos da una idea del error típico de nuestros pronósticos.

**Fórmula:**
$$S_e = \sqrt{rac{\sum(y_i - \hat{y}_i)^2}{n-2}}$$

Donde:
- $y_i$ es el valor real de la nota.
- $\hat{y}_i$ es el valor de la nota pronosticado por el modelo.
- $n$ es el número de observaciones.

El error estándar para este modelo es:

- **$S_e  pprox$ 14.40**

Esto significa que, en promedio, las notas pronosticadas por nuestro modelo se desvían aproximadamente **14.40 puntos** de las notas reales.