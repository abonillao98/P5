import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav

# Cargar el archivo WAV
rate, data = wav.read("senoPlano_vs_tanh_vs_hard.wav")  # Asegúrate de que el archivo esté en el mismo directorio o da la ruta completa

# Si el audio es estéreo, tomamos solo un canal
if data.ndim > 1:
    data = data[:, 0]

# Función para convertir segundos a índice de muestra
def time_to_sample(t, rate):
    return int(t * rate)

# Definir los segmentos (inicio, fin, título)
segments = [
    (0.0, 0.555, "Seno plano sin efectos"),
    (0.749, 1.3, "Seno plano con Distorsion Tanh (Ganancia = 3.0)"),
    (1.58, 2.135, "Seno plano con Distorsion Hard (Umbral 75%)")
]

# Crear el gráfico
fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=False)

for i, (start_t, end_t, title) in enumerate(segments):
    start_idx = time_to_sample(start_t, rate)
    end_idx = time_to_sample(end_t, rate)
    t = np.linspace(start_t, end_t, end_idx - start_idx)
    axs[i].plot(t, data[start_idx:end_idx])
    axs[i].set_title(title)
    axs[i].grid(True)

plt.tight_layout()
plt.show()
