import pandas as pd
from utils.imports import benford_law, plot_benford

# Leer el conjunto de datos (reemplaza 'tu_archivo.csv' con el nombre de tu archivo CSV)
data = pd.read_csv('data/winequality_red.csv')

# Iterar sobre cada columna del conjunto de datos
for column_name in data.columns:
    # Seleccionar la columna actual
    column_data = data[column_name]

    # Ejecutar la Ley de Benford en la columna actual
    benford_freq, observed_freq = benford_law(column_data)

    # Graficar la distribución de Benford para la columna actual
    plot_benford(benford_freq, observed_freq, column_name)

