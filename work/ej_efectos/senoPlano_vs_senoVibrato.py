import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile

# Cargar archivo de audio
sample_rate, audio_data = wavfile.read("senoPlano_vs_senoVibrato.wav")

# Crear eje de tiempo
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# Definir los intervalos de tiempo
t1_start, t1_end = 0, 0.65
t2_start, t2_end = 0.75, 1.34
t3_start, t3_end = 0.0, 0.025
t4_start, t4_end = 0.75, 0.78

# Obtener los índices correspondientes
idx1 = np.logical_and(time >= t1_start, time <= t1_end)
idx2 = np.logical_and(time >= t2_start, time <= t2_end)
idx3 = np.logical_and(time >= t3_start, time <= t3_end)
idx4 = np.logical_and(time >= t4_start, time <= t4_end)

# Crear figura 2x2
fig, axs = plt.subplots(2, 2, figsize=(12, 6), sharey=True)

# Primer subplot: seno plano
axs[0,0].plot(time[idx1], audio_data[idx1])
axs[0,0].set_title("Seno plano sin efectos")
axs[0,0].grid()

# Segundo subplot: seno vibrato
axs[1,0].plot(time[idx2], audio_data[idx2])
axs[1,0].set_title("Seno plano con efecto vibrato I=0.6 fm=6")
axs[1,0].grid()

# Segundo subplot: curva ataque sin efectos
axs[0,1].plot(time[idx3], audio_data[idx3])
axs[0,1].set_title("Curva de atque sin efectos")
axs[0,1].grid()

# Segundo subplot: curva ataque con vibrato
axs[1,1].plot(time[idx4], audio_data[idx4])
axs[1,1].set_title("Curva de ataque con vibrato I=0.6 fm=6")
axs[1,1].grid()

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()