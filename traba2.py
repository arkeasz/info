import numpy as np
import matplotlib.pyplot as plt

# Datos
posicion = np.array([0.71, 0.64, 0.58, 0.43, 0.30, 0.25])
tiempo = np.array([0.380, 0.361, 0.344, 0.296, 0.247, 0.226])

# Ajuste cuadrático (polinomio de grado 2)
coeficientes = np.polyfit(tiempo, posicion, 2)

# Generar la función polinómica
polinomio = np.poly1d(coeficientes)

# Crear puntos para la gráfica del ajuste
tiempo_fit = np.linspace(min(tiempo), max(tiempo), 100)
posicion_fit = polinomio(tiempo_fit)

# Gráfica
plt.scatter(tiempo, posicion, color='red', label='Datos experimentales')
plt.plot(tiempo_fit, posicion_fit, label='Ajuste cuadrático', color='blue')

# Mostrar la ecuación en la gráfica
equacion_texto = f"y = {coeficientes[0]:.4f}t²+{coeficientes[1]:.4f}t + {coeficientes[2]:.4f}"
plt.text(0.25, 0.6, equacion_texto, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Ajuste cuadrático')
plt.legend()
plt.grid()
plt.show()
