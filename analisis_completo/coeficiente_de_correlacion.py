# Importar la librería pandas, esencial para trabajar con datos.
import pandas as pd

# Cargar los datos desde tu archivo CSV.
datos = pd.read_csv('datos\\datos_estudio_examen.csv')

# Calcular la matriz de correlación para todas las variables del DataFrame.
# El método .corr() calcula el coeficiente de correlación de Pearson por defecto.
matriz_correlacion = datos.corr()

# Extraer el valor de correlación específico entre las dos variables de interés.
# Usamos .loc para acceder al valor en la fila 'Horas_semanales_de_estudio' 
# y la columna 'Nota_obtenida_examen_final'.
coeficiente_r = matriz_correlacion.loc['Horas_semanales_de_estudio', 'Nota_obtenida_examen_final']

# Imprimir la matriz completa y el coeficiente específico de forma clara.
print("Matriz de Correlación:")
print(matriz_correlacion)
print("\n----------------------------------------------------")
print(f"Coeficiente de Correlación de Pearson (r): {coeficiente_r:.4f}")