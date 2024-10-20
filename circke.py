import matplotlib.pyplot as plt

# Definimos las fuerzas
forces = {
    'Fuerza Gravitacional (Fg)': (0, -1),
    'Resistencia del Aire (Fr)': (-1, 0) 
}

# Figura
plt.figure(figsize=(8, 6))

# Dibuja la esfera
circle = plt.Circle((0, 0), 0.1, color='purple', label='Proyectil (Esfera)')
plt.gca().add_artist(circle)

# Fuerzas
plt.quiver(0, 0, 0, -1, angles='xy', scale_units='xy', scale=1, color='blue', label='Fg')
plt.quiver(0, 0, -1, 0, angles='xy', scale_units='xy', scale=1, color='red', label='Fr')

# Añadimos anotaciones
for force, vector in forces.items():
    plt.annotate(force, xy=vector, xytext=(vector[0] + 0.1, vector[1] - 0.5), fontsize=10)

# Configuraciones de la gráfica
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.title('Diagrama de fuerzas')
plt.xlabel('Eje Horizontal')
plt.ylabel('Eje Vertical')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')  
plt.show()
