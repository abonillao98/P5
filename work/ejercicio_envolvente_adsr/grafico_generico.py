import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Cargar el archivo WAV
sample_rate, data = wav.read("generico.wav")

# Convertir a mono si es estéreo
if data.ndim > 1:
    data = data.mean(axis=1)

# Eje temporal
time = np.arange(len(data)) / sample_rate

# Índices del ataque
attack_start, attack_end = 0.5, 0.55
attack_indices = (time >= attack_start) & (time <= attack_end)

# Índices del decay
decay_start, decay_end = 0.55, 0.65
decay_indices = (time >= decay_start) & (time <= decay_end)

# Sustain: Nivel de la señal en t = 0.73 s
target_time = 0.73
target_index = int(target_time * sample_rate)
signal_level_at_073 = abs(data[target_index])

# Índices del Release
release_start, release_end = 1.0 , 1.1
release_indices = (time >= release_start) & (time <= release_end)

# Graficar la señal
plt.figure(figsize=(12, 6))
plt.plot(time, data, label="Instrumento generico", alpha=0.7)
plt.plot(time[attack_indices], data[attack_indices], color='red', label='Ataque')
plt.plot(time[decay_indices], data[decay_indices], color='blue', label='Decay')
plt.axhline(y=signal_level_at_073, color='green', linestyle='--', label='Sustain')
plt.plot(time[release_indices], data[release_indices], color='green', label='Release')

# Etiquetas y leyenda
plt.title("Señal de audio con fase de ataque destacada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
