import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Parámetros comunes
attack_start, attack_end = 0.5, 0.55
decay_start, decay_end = 0.55, 0.65
sustain_time = 0.73
release_start, release_end = 1.0 , 1.1

# Lista de archivos y títulos
audio_files = [
    ("generico.wav", "Instrumento genérico"),
    ("percusivo1.wav", "Percusivo 1"),
    ("percusivo2.wav", "Percusivo 2"),
    ("plano.wav", "Instrumento plano")
]

# Crear la figura
plt.figure(figsize=(14, 10))

for i, (filename, title) in enumerate(audio_files, 1):

    if i == 1: # tiempos Generico
        attack_start, attack_end = 0.5, 0.55
        decay_start, decay_end = 0.55, 0.65
        nivel_de_sustain = 2460
        release_start, release_end = 1.0 , 1.1
    elif i == 2: # tiempo percusivo 1
        attack_start, attack_end = 0.5, 0.6
        decay_start, decay_end = 0.6, 0.7
        nivel_de_sustain = 0
        release_start, release_end = 0.01 , 0.02
    elif i == 3: # tiempos percusivo 2
        attack_start, attack_end = 0.5, 0.8
        decay_start, decay_end = 0.8, 1.0
        nivel_de_sustain = 0
        release_start, release_end = 1.0 , 1.1
    elif i == 4:# tiempos plano
        attack_start, attack_end = 0.5, 0.52
        decay_start, decay_end = 0.01, 0.02
        nivel_de_sustain = 12269
        release_start, release_end = 1.0 , 1.1

    sample_rate, data = wav.read(filename)
    if data.ndim > 1:
        data = data.mean(axis=1)

    time = np.arange(len(data)) / sample_rate

    attack_indices = (time >= attack_start) & (time <= attack_end)
    decay_indices = (time >= decay_start) & (time <= decay_end)
    sustain_index = int(sustain_time * sample_rate)

    release_indices = (time >= release_start) & (time <= release_end)

    # Subgráfico
    plt.subplot(2, 2, i)
    plt.plot(time, data, label='Señal de audio', alpha=0.7)
    plt.plot(time[attack_indices], data[attack_indices], color='red', label='Ataque')
    plt.plot(time[decay_indices], data[decay_indices], color='blue', label='Decay')
    plt.axhline(y=nivel_de_sustain, color='green', linestyle='--', label='Sustain')
    plt.plot(time[release_indices], data[release_indices], color='green', label='Release')
    
    plt.title(title)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.legend()


plt.tight_layout()
plt.show()
