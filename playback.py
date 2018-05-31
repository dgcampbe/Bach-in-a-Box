import pygame
from pygame import midi
import music21
import time
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

#once exporting and importing to and from midi works properly, playing midi files using the code below will no longer be supported (as if it ever really worked anyway)

def playmidinote(notenum, tempo):

    try:
        
        lengthofnote = 60/int(tempo)
        pygame.init()
        pygame.midi.init()
        port = pygame.midi.get_default_output_id()
        midi_out = pygame.midi.Output(port, 0)
        midi_out.set_instrument(6)
        midi_out.note_on(notenum, 127)
        time.sleep(lengthofnote)
        midi_out.note_off(notenum, 127)

    finally:

        del midi_out
        pygame.midi.quit()

def midichord(notenum_array, seconds):

    try:

        pygame.init()
        pygame.init()
        pygame.midi.init()
        port = pygame.midi.get_default_output_id()
        midi_out = pygame.midi.Output(port, 0)
        midi_out.set_instrument(6)        

        for notenum in notenum_array:

            midi_out.note_on(notenum, 127)

        time.sleep(seconds)

        for notenum in notenum_array:

            midi_out.note_off(notenum, 127)
            
    finally:

        del midi_out
        pygame.midi.quit()        
    
def pysynth_play(name, song, tempo):
  
    pysynth_b.make_wav(song, fn = "pysynth - " + str(name) + ".wav", bpm = tempo)
