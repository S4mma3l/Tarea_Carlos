# Importar las librerías necesarias:
# pandas para la manipulación de datos.
# LinearRegression de scikit-learn para crear el modelo de regresión.
import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos desde el archivo CSV en un DataFrame de pandas.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

# Definir las variables del modelo:
# La variable independiente (X) es la causa, en este caso, las horas de estudio.
# La variable dependiente (y) es el efecto, es decir, la nota que queremos predecir.
# Nota: X debe ser un DataFrame (con doble corchete) y 'y' una Serie (con corchete simple).
X = datos[['Horas_semanales_de_estudio']]
y = datos['Nota_obtenida_examen_final']

# Crear una instancia del modelo de Regresión Lineal.
# Este objeto será el que "aprenderá" la relación entre X e y.
modelo = LinearRegression()

# Entrenar (o ajustar) el modelo utilizando nuestros datos.
# El método .fit() calcula los valores óptimos para la pendiente y el intercepto
# que mejor se ajustan a los datos proporcionados.
modelo.fit(X, y)

# Obtener los coeficientes calculados por el modelo.
# .intercept_ nos da el intercepto (el punto donde la línea cruza el eje Y).
# .coef_ nos da la pendiente de la línea (la inclinación).
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]

# Imprimir los resultados de forma clara.
print(f"El intercepto (b₀) es: {intercepto}")
print(f"La pendiente (b₁) es: {pendiente}")

# Mostrar la ecuación de regresión final de una manera fácil de entender.
print(f"\nLa ecuación de regresión es:")
print(f"Nota del Examen = {pendiente:.4f} * (Horas de Estudio) + {intercepto:.4f}")