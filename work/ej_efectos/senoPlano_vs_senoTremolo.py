import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile

# Cargar archivo de audio
sample_rate, audio_data = wavfile.read("senoPlano_vs_senoTremolo.wav")

# Crear eje de tiempo
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# Definir los intervalos de tiempo
t1_start, t1_end = 0, 0.65
t2_start, t2_end = 0.75, 1.34

# Obtener los índices correspondientes
idx1 = np.logical_and(time >= t1_start, time <= t1_end)
idx2 = np.logical_and(time >= t2_start, time <= t2_end)

# Crear figura 2x1
fig, axs = plt.subplots(2, 1, figsize=(12, 6), sharey=True)

# Primer subplot: seno plano
axs[0].plot(time[idx1], audio_data[idx1])
axs[0].set_title("Seno plano sin efectos")

# Segundo subplot: seno tremolo
axs[1].plot(time[idx2], audio_data[idx2])
axs[1].axvline(x=0.844, color='green', label='∆fm')
axs[1].axvline(x=0.885, color='green')
axs[1].axhline(y=4933, color='red', label='∆A')
axs[1].axhline(y=12269, color='red')
axs[1].set_title("Seno plano con efecto tremolo A=0.6 fm=24")
axs[1].legend()

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()
