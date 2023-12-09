import numpy as np
import matplotlib.pyplot as plt

def benford_law(data):
    # Obtener el primer dígito de cada número en el conjunto de datos
    first_digits = [int(str(abs(x))[0]) for x in data if x != 0]

    # Calcular la frecuencia esperada según la Ley de Benford
    benford_freq = np.log10(1 + 1/np.arange(1, 10))

    # Calcular la frecuencia observada en el conjunto de datos
    observed_freq = [first_digits.count(d) / len(first_digits) for d in range(1, 10)]

    return benford_freq, observed_freq


def plot_benford(benford_freq, observed_freq, column_name):
    # Graficar la distribución esperada y observada
    digits = range(1, 10)
    plt.bar(digits, benford_freq, color='blue', alpha=0.5, label='Expected')
    plt.bar(digits, observed_freq, color='red', alpha=0.5, label='Observed')
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.title(f"Benford's Law Distribution - {column_name}")
    plt.legend()
    plt.show()
