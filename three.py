
import numpy as np
import matplotlib.pyplot as plt

r = np.array([0, 0.13, 0.18, 0.23, 0.28, 0.33, 0.39, 0.43, 0.49, 0.53, 0.58, 0.63, 0.68, 0.73, 0.78])
t = np.array([0, 1.40, 2.05, 2.25, 2.45, 2.65, 2.90, 3.05, 3.30, 3.55, 3.70, 3.90, 4.10, 4.30, 4.50])

# Ajuste cuadrático
coefficients = np.polyfit(t, r, 2)
quadratic_fit = np.poly1d(coefficients)
t_fit = np.linspace(min(t), max(t), 100)
r_fit = quadratic_fit(t_fit)

# Coeficientes
a = coefficients[0]
b = coefficients[1]
c = coefficients[2]

# Cálculo de la aceleración
aceleracion = 2 * a

# Etiquetas
plt.plot(t, r, 'o', label='Datos originales')
plt.plot(t_fit, r_fit, '-', label='Ajuste cuadrático')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Gráfica de MRUV')

# Mostrar los coeficientes y aceleración
plt.annotate(f'Ajuste: r = {a:.4f}t² + {b:.4f}t + {c:.4f}',
             xy=(1, quadratic_fit(1)), xytext=(1.5, quadratic_fit(1) + 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='red')

plt.annotate(f'Aceleración: {aceleracion:.4f} m/s²',
             xy=(3, quadratic_fit(3)), xytext=(4, quadratic_fit(4) + 0.1),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10)

plt.legend()
plt.grid()
plt.show()
print(f'Aceleración: {aceleracion:.4f} m/s²')
