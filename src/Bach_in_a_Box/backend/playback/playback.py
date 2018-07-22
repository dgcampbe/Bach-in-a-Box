import os.path
import math
from pyaudio import PyAudio
import pysynth_b

def sine_tone(frequency, duration, volume=1, sample_rate = 22050):

    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1), channels = 1, rate = sample_rate, output = True)

    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))

    for buf in zip(*[samples]*sample_rate): #write several samples at a time

        stream.write(bytes(bytearray(buf)))

    #fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)
    stream.stop_stream()
    stream.close()
    p.terminate()

def pysynth_play(name, song, tempo):
  
    pysynth_b.make_wav(song, fn = "pysynth - " + str(name) + ".wav", bpm = tempo)
