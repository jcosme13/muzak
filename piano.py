import numpy as np 

samplerate = 44100

def get_wave(freq, duration = 0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate*duration))
    wave = amplitude * np.sin(2*np.pi*freq*t)

    return wave

a_wave = get_wave(440, 1)

print(len(a_wave))
print(np.max(a_wave))
print(np.min(a_wave))