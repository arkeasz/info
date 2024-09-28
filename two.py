
import numpy as np

#Definiendo nuestras funciones
def calcular_minimos_cuadrados(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x*2) - (np.sum(x))*2)
    b = (np.sum(y) - m * np.sum(x)) / n
    return m, b

#Nuestros datos
def main():
    r = [0, 0.13, 0.18, 0.23, 0.28, 0.33, 0.39, 0.43, 0.49, 0.53, 0.58, 0.63, 0.68, 0.73, 0.78]
    t = [0, 1.40, 2.05, 2.25, 2.45, 2.65, 2.90, 3.05, 3.30, 3.55, 3.70, 3.90, 4.10, 4.30, 4.50]
    m, b = calcular_minimos_cuadrados(r, t)
    print(f"pendiente (m): {m}")
    print(f"Intersección (b): {b}")

if _name_ == "_main_":
    main()
