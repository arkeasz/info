import numpy as np
import matplotlib.pyplot as plt

g_ecuador= 9.780318
f_4= 0.0000058
Deformacion_gravitacional= 0.0053024
H= float(input("Ingrese la altura en metros:")) #En nuestro caso es 24.16
Φ= float(input("Ingrese la latitud en grados:")) #En nuestro caso es 12.0611
g= g_ecuador*(1+Deformacion_gravitacional*np.sin(Φ)**2-f_4*np.sin(2*Φ)**2)- 3.806*10**-6*H
print("La aceleracion de la gravedad local es:",g)