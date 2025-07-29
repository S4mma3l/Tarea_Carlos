# Importar la librería pandas, que es esencial para trabajar con DataFrames (tablas de datos) en Python.
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV 'datos_estudio_examen.csv' y cargarlo en un DataFrame de pandas.
# Usamos directamente el nombre del archivo, ya que está en el mismo directorio de trabajo.
# Esto hace que el código sea más portable entre diferentes sistemas operativos.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')


# --- Creación del Diagrama de Dispersión ---

# Se crea una figura y ejes para el gráfico.
plt.figure(figsize=(10, 6))

# Se genera el diagrama de dispersión.
# Eje X: Horas de estudio
# Eje Y: Nota del examen
plt.scatter(datos['Horas_semanales_de_estudio'], datos['Nota_obtenida_examen_final'], alpha=0.7, color='blue')

# Añadir títulos y etiquetas para que el gráfico sea fácil de entender.
plt.title('Relación entre Horas de Estudio y Nota del Examen', fontsize=16)
plt.xlabel('Horas Semanales de Estudio', fontsize=12)
plt.ylabel('Nota Obtenida en el Examen Final', fontsize=12)
plt.grid(True) # Se añade una cuadrícula para facilitar la lectura de los valores.

# Guardar el gráfico como un archivo de imagen.
plt.savefig('img_new\\diagrama_dispersion.png')


# --- Cálculo de la Correlación ---

# Se calcula la matriz de correlación de Pearson para todas las variables del DataFrame.
correlacion = datos.corr()

# Se imprime la matriz de correlación en la consola.
print("Matriz de correlación:")
print(correlacion)