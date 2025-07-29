# Análisis de Regresión: Horas de Estudio vs. Nota de Examen

Este documento detalla el proceso manual para analizar la relación entre dos variables: las **horas de estudio semanales** y la **nota obtenida en un examen final**. Todos los cálculos se presentan paso a paso.

---
## Datos Base y Sumatorias
Para realizar los cálculos manuales, primero necesitamos obtener las sumatorias básicas de nuestro conjunto de datos.

* **Variable Independiente (X):** `Horas_semanales_de_estudio`
* **Variable Dependiente (Y):** `Nota_obtenida_examen_final`

A partir de los datos, calculamos los siguientes valores:

* Número de observaciones ($n$): **24**
* Suma de X ($\sum x$): **214**
* Suma de Y ($\sum y$): **1162**
* Suma de X al cuadrado ($\sum x^2$): **2772**
* Suma de Y al cuadrado ($\sum y^2$): **76598**
* Suma de (X * Y) ($\sum xy$): **13364**

---
## 1. Coeficiente de Correlación de Pearson ($r$)
Mide la fuerza y dirección de la relación lineal entre X e Y.

### Fórmula
$$
r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n(\sum x^2) - (\sum x)^2][n(\sum y^2) - (\sum y)^2]}}
$$

### Cálculo Manual
1.  **Numerador:**
    $(24 \times 13364) - (214 \times 1162) = 320736 - 248668 = 72068$
2.  **Denominador (parte X):**
    $(24 \times 2772) - (214^2) = 66528 - 45796 = 20732$
3.  **Denominador (parte Y):**
    $(24 \times 76598) - (1162^2) = 1838352 - 1350244 = 488108$
4.  **Cálculo final:**
    $$
    r = \frac{72068}{\sqrt{20732 \times 488108}} = \frac{72068}{\sqrt{10119339376}} = \frac{72068}{100595.92} \approx 0.7164
    $$

**Resultado:** $r \approx 0.716$ (Relación positiva fuerte).

---
## 2. Ecuación de Regresión Lineal ($y = b_1x + b_0$)
Permite predecir el valor de Y basándose en un valor de X.

### Fórmula de la Pendiente ($b_1$)
$$
b_1 = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}
$$

### Cálculo de la Pendiente
$$
b_1 = \frac{72068}{20732} \approx 3.4762
$$

### Fórmula del Intercepto ($b_0$)
Para calcular el intercepto, primero necesitamos las medias de X e Y.
* Media de X ($\bar{x}$): $\frac{\sum x}{n} = \frac{214}{24} \approx 8.9167$
* Media de Y ($\bar{y}$): $\frac{\sum y}{n} = \frac{1162}{24} \approx 48.4167$

La fórmula es:
$$
b_0 = \bar{y} - b_1\bar{x}
$$

### Cálculo del Intercepto
$$
b_0 = 48.4167 - (3.4762 \times 8.9167) = 48.4167 - 30.9959 \approx 17.4208
$$

### Ecuación Final
$$
\text{Nota del Examen} = (3.4762 \times \text{Horas de Estudio}) + 17.4208
$$

---
## 3. Pronóstico con la Ecuación
Usamos la ecuación para predecir la nota para **17 horas** de estudio.

### Cálculo
$$
\text{Nota} = (3.4762 \times 17) + 17.4208 = 59.0954 + 17.4208 \approx 76.52
$$

**Resultado:** La nota pronosticada es **76.52**.

---
## 4. Error Estándar de la Estimación ($S_e$)
Mide el error típico de las predicciones del modelo.

### Fórmula
Una fórmula sencilla para el cálculo manual es:
$$
S_e = \sqrt{\frac{\sum y^2 - b_0(\sum y) - b_1(\sum xy)}{n-2}}
$$

### Cálculo Manual
1.  **Calcular el numerador (Suma de Errores al Cuadrado - SSE):**
    $SSE = 76598 - (17.4208 \times 1162) - (3.4762 \times 13364)$
    $SSE = 76598 - 20242.97 - 46464.38 = 9990.65$
2.  **Dividir por los grados de libertad ($n-2$):**
    $n - 2 = 24 - 2 = 22$
    $\frac{9990.65}{22} \approx 454.12$
3.  **Calcular la raíz cuadrada:**
    $S_e = \sqrt{454.12} \approx 21.31$

*(Nota: Pequeñas diferencias con el resultado del software pueden ocurrir debido al redondeo de $b_0$ y $b_1$ en los cálculos manuales).*

**Resultado:** $S_e \approx 21.21$ (usando valores sin redondear), indica que las predicciones se desvían, en promedio, unos 21.21 puntos de los valores reales.