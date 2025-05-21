import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

# Cargar el archivo WAV
rate, data = wav.read("significativo.wav")  # Ajusta la ruta si es necesario

# Convertir a mono si el audio es estéreo
if data.ndim > 1:
    data = data[:, 0]

# Función para convertir tiempo (s) a índice de muestra
def time_to_sample(t, rate):
    return int(t * rate)

# Segmentos y títulos
segments = [
    (0.165, 0.69, "Señal completo N1=3 N2=1 I=4"),
    (0.3, 0.33, "Tramo de 30 ms"),
    (0.3, 0.31, "Tramo de 10 ms")
]

# Crear la figura
fig, axs = plt.subplots(3, 1, figsize=(12, 8))

# Dibujar cada tramo
for i, (start_t, end_t, title) in enumerate(segments):
    start_idx = time_to_sample(start_t, rate)
    end_idx = time_to_sample(end_t, rate)
    t = np.linspace(start_t, end_t, end_idx - start_idx)
    axs[i].plot(t, data[start_idx:end_idx])
    axs[i].set_title(title)
    axs[i].grid(True)

plt.tight_layout()
plt.show()
