# Importar las librerías necesarias:
# pandas para manejar los datos.
# LinearRegression de scikit-learn para el modelo.
# numpy para operaciones numéricas, especialmente la raíz cuadrada y la suma.
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos desde el archivo CSV.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

# Definir las variables independiente (X) y dependiente (y).
X = datos[['Horas_semanales_de_estudio']]
y = datos['Nota_obtenida_examen_final']

# Crear y entrenar el modelo de regresión lineal.
modelo = LinearRegression()
modelo.fit(X, y)

# Usar el modelo para predecir los valores de 'y' (ŷ) basándose en 'X'.
# Estos son los puntos que caen exactamente sobre la línea de regresión.
y_predichos = modelo.predict(X)

# Obtener el número total de observaciones (n) en el conjunto de datos.
n = len(datos)

# Calcular la Suma de los Cuadrados de los Errores (SSE).
# Esta es la suma de todas las diferencias al cuadrado entre los valores reales (y)
# y los valores predichos por el modelo (ŷ).
sse = np.sum((y - y_predichos)**2)

# Calcular el Error Estándar de la Estimación (Se).
# La fórmula es la raíz cuadrada del Error Cuadrático Medio (SSE dividido por los grados de libertad, n-2).
error_estandar_estimacion = np.sqrt(sse / (n - 2))

# Imprimir el resultado final formateado a cuatro decimales.
print(f"El Error Estándar de la Estimación (Se) es: {error_estandar_estimacion:.4f}")