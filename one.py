
import numpy as np
import matplotlib.pyplot as plt

# Datos de posición (r) y tiempo (t)
r = [0, 0.13, 0.18, 0.23, 0.28, 0.33, 0.39, 0.43, 0.49, 0.53, 0.58, 0.63, 0.68, 0.73, 0.78]
t = [0, 1.40, 2.05, 2.25, 2.45, 2.65, 2.90, 3.05, 3.30, 3.55, 3.70, 3.90, 4.10, 4.30, 4.50]

# Ajuste lineal
coeficientes = np.polyfit(r, t, 1)  # Calcular los coeficientes de la línea
linear_fit = np.poly1d(coefficients)  # Crear una función polinómica
r_fit = np.linspace(min(r), max(r), 100)  # Generar valores para r
t_fit = linear_fit(r_fit)  # Calcular los valores correspondientes de t

# Graficar los datos y la línea de ajuste
plt.plot(r, t, 'o', label='Datos originales')
plt.plot(r_fit, t_fit, '-', label='Línea de ajuste lineal')
plt.xlabel('Posición (r)')
plt.ylabel('Tiempo (t)')
plt.title('Grafica MRU')
plt.legend()
plt.show()
