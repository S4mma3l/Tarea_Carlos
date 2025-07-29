# Importar las librerías necesarias.
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings 

# --- Recrear y entrenar el modelo (este paso asegura que partimos del modelo correcto) ---

# Cargar los datos desde el archivo CSV.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

# Definir las variables independiente (X) y dependiente (y).
X = datos[['Horas_semanales_de_estudio']]
y = datos['Nota_obtenida_examen_final']

# Crear y entrenar el modelo de regresión lineal.
modelo = LinearRegression()
modelo.fit(X, y)


# --- Realizar la Predicción ---

# Definir las horas de estudio para las que queremos hacer el pronóstico.
horas_a_pronosticar = 17

# Usar el método .predict() del modelo ya entrenado.
# Este método toma un valor de X y devuelve el valor predicho de y.
# Se debe pasar el valor dentro de una estructura de dos dimensiones, por eso los dobles corchetes [[...]].
nota_pronosticada = modelo.predict([[horas_a_pronosticar]])

# Imprimir el resultado de forma amigable y clara.
# Usamos [0] para acceder al valor numérico de la predicción y :.2f para redondearlo a 2 decimales.
print(f"Para un estudiante que invierte {horas_a_pronosticar} horas semanales de estudio,")
print(f"la nota pronosticada es de: {nota_pronosticada[0]:.2f}")