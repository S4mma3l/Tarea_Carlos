import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Creación de un DataFrame de ejemplo
# En un caso real, cargaríamos el CSV con:
# datos = pd.read_csv('datos_estudio_examen.csv')
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

print(datos.columns)

# a) Diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(datos['Horas_semanales_de_estudio'], datos['Nota_obtenida_examen_final'], color='blue', label='Datos reales')
plt.title('Diagrama de Dispersión: Horas de Estudio vs. Nota del Examen')
plt.xlabel('Horas de Estudio Semanales')
plt.ylabel('Nota del Examen Final')
plt.grid(True)

# Desarrollo del modelo de regresión para la línea de ajuste
X = datos[['Horas_semanales_de_estudio']]
y = datos['Nota_obtenida_examen_final']
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)
plt.plot(datos['Horas_semanales_de_estudio'], y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.legend()
plt.savefig('img\\figura_1.png')

# b) Ecuación de regresión
beta_0 = modelo.intercept_
beta_1 = modelo.coef_[0]

# c) Pronóstico
horas_estudio_nuevo = 17
nota_pronosticada = modelo.predict([[horas_estudio_nuevo]])[0]

# d) Coeficiente de correlación
coef_correlacion = datos['Horas_semanales_de_estudio'].corr(datos['Nota_obtenida_examen_final'])

# e) Error estándar de la estimación
n = len(datos)
error_estandar = np.sqrt(np.sum((y - y_pred)**2) / (n - 2))

# Imprimir resultados
print("Resultados del Análisis de Regresión Lineal:")
print("-" * 50)
print(f"a) El diagrama de dispersión ha sido guardado como 'figura_1.png'")
print(f"b) Ecuación de Regresión: Nota_Examen = {beta_0:.2f} + {beta_1:.2f} * (Horas_Estudio)")
print(f"c) Pronóstico para 17 horas de estudio: {nota_pronosticada:.2f}")
print(f"d) Coeficiente de Correlación (r): {coef_correlacion:.3f}")
print(f"e) Error Estándar de la Estimación (Se): {error_estandar:.2f}")