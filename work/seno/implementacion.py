import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 64  # Número de muestras en la tabla
x_table = np.linspace(0, 2 * np.pi, N, endpoint=False)
y_table = np.sin(x_table)

x_fine = np.linspace(0, 2 * np.pi, 1000)
y_interp = np.interp(x_fine, x_table, y_table)

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(x_fine, y_interp, label='Señal', color='blue')
plt.plot(x_table, y_table, 'o', label='Valores de la tabla', color='red')
plt.title('Muestreo de la función seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
