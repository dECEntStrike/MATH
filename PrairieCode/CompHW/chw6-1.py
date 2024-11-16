import numpy as np
import matplotlib.pyplot as plt

# Write your code to calculate denoised audio signal 

coordinates = create_dct_basis(audio_signal.shape[0])
coordinates = audio_signal @ coordinates
coordinates_filtered = np.zeros(1000)
for i in range(0, 1000):
    coordinates_filtered[i] = coordinates[i]
    if (np.abs(coordinates[i]) < 1):
        coordinates_filtered[i] = 0
denoised = create_dct_basis(coordinates_filtered.shape[0])
denoised = denoised @ coordinates_filtered


# Uncomment below to plot 
fig, ax = plt.subplots()
plt.plot(audio_signal)
plt.plot(denoised)