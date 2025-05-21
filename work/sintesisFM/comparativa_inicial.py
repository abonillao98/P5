import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

# Cargar el archivo WAV
rate, data = wav.read("fm.wav")  # Cambia la ruta si es necesario

# Convertir a mono si es estéreo
if data.ndim > 1:
    data = data[:, 0]

# Función para convertir segundos a muestras
def time_to_sample(t, rate):
    return int(t * rate)

# Definir segmentos: (inicio, fin, título)
segments = [
    (0.165, 0.688, "seno fm N1=1 N2=20 I=0.5"),  # Tramo grande fila 1
    (0.998, 1.522, "seno fm N1=5 N2=1 I=24"),  # Tramo grande fila 2
    (0.245, 0.275, "zoom seno fm N1=1 N2=20 I=0.5"),  # Subplot izquierdo fila 3
    (1.085, 1.11,  "zoom seno fm N1=5 N2=1 I=24")   # Subplot derecho fila 3
]

# Crear figura con 3 filas
fig = plt.figure(figsize=(14, 10))

# Subplot 1 - Fila completa
ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)
start, end, title = segments[0]
t = np.linspace(start, end, time_to_sample(end, rate) - time_to_sample(start, rate))
ax1.plot(t, data[time_to_sample(start, rate):time_to_sample(end, rate)])
ax1.set_title(title)
ax1.grid(True)

# Subplot 2 - Fila completa
ax2 = plt.subplot2grid((3, 2), (1, 0), colspan=2)
start, end, title = segments[1]
t = np.linspace(start, end, time_to_sample(end, rate) - time_to_sample(start, rate))
ax2.plot(t, data[time_to_sample(start, rate):time_to_sample(end, rate)])
ax2.set_title(title)
ax2.grid(True)

# Subplot 3 - Izquierda de fila 3
ax3 = plt.subplot2grid((3, 2), (2, 0))
start, end, title = segments[2]
t = np.linspace(start, end, time_to_sample(end, rate) - time_to_sample(start, rate))
ax3.plot(t, data[time_to_sample(start, rate):time_to_sample(end, rate)])
ax3.set_title(title)
ax3.grid(True)

# Subplot 4 - Derecha de fila 3
ax4 = plt.subplot2grid((3, 2), (2, 1))
start, end, title = segments[3]
t = np.linspace(start, end, time_to_sample(end, rate) - time_to_sample(start, rate))
ax4.plot(t, data[time_to_sample(start, rate):time_to_sample(end, rate)])
ax4.set_title(title)
ax4.grid(True)

plt.tight_layout()
plt.show()
