#!/usr/bin/env python
"""Playback."""
import pyaudio
import numpy as np
p = pyaudio.PyAudio()


def sine_tone(freq, duration, volume=0.5, fs=44100):
    """Play sinetone."""
    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write((volume*samples).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
