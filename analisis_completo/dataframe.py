# Importar la librería pandas, que es esencial para trabajar con DataFrames (tablas de datos) en Python.
import pandas as pd

# Leer el archivo CSV 'datos_estudio_examen.csv' y cargarlo en un DataFrame de pandas.
# Usamos directamente el nombre del archivo, ya que está en el mismo directorio de trabajo.
# Esto hace que el código sea más portable entre diferentes sistemas operativos.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

# Imprimir los nombres de las columnas del DataFrame.
# La propiedad .columns de un DataFrame devuelve una lista con los nombres de todas las columnas.
print(datos.columns)
print(datos.head())  # Mostrar las primeras filas del DataFrame para verificar su contenido
print(datos.describe())  # Mostrar estadísticas descriptivas del DataFrame