import pygame
from pygame import midi
import music21
import time

def playmidinote(notenum,lengthofnote):

    pygame.init()
    pygame.midi.init()
    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port, 0)
    midi_out.set_instrument(6)
    midi_out.note_on(notenum,127)
    time.sleep(lengthofnote)
    midi_out.note_off(notenum,127)
