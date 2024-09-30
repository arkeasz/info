import numpy as np
import matplotlib.pyplot as plt

# Datos
tiempo_cuadrado = np.array([0.1444, 0.130321, 0.118336, 0.087616, 0.061009, 0.051076])
posicion = np.array([0.71, 0.64, 0.58, 0.43, 0.30, 0.25])

# Ajuste lineal
coeficientes = np.polyfit(tiempo_cuadrado, posicion, 1)
pendiente, interseccion = coeficientes

# Generar valores ajustados
tiempo_cuadrado_ajustado = np.linspace(tiempo_cuadrado.min(), tiempo_cuadrado.max(), 100)
posicion_ajustada = pendiente * tiempo_cuadrado_ajustado + interseccion

# Graficar
plt.plot(tiempo_cuadrado, posicion, 'o', label='Datos')
plt.plot(tiempo_cuadrado_ajustado, posicion_ajustada, 'r-', label='Ajuste Lineal')
plt.title('Ajuste lineal')
plt.xlabel('Tiempo Cuadrado (s^2)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Añadir la ecuación al gráfico
plt.text(0.1, 0.45, f'y = {pendiente:.4f} * t² + {interseccion:.4f}', fontsize=12, color='blue')

plt.legend()
plt.show()

