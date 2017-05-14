#The subject of Bach's Contrapunctus 1 from Die Kunst Der Fuge in MIDI form

import pygame
from pygame import midi
import time
import music21

def miditest():

    #Bach's Art of Fugue FTW!!!!!    
    pygame.init()
    pygame.midi.init()
    port = pygame.midi.get_default_output_id()
    midi_out = pygame.midi.Output(port, 0)
    midi_out.set_instrument(19)
    midi_out.note_on(74,127)
    time.sleep(1.5)
    midi_out.note_off(74,127)
    time.sleep(.1)

    midi_out.note_on(81,127)
    time.sleep(1.5)
    midi_out.note_off(81,127)
    time.sleep(.1)

    midi_out.note_on(77,127)
    time.sleep(1.5)
    midi_out.note_off(77,127)
    time.sleep(.1)

    midi_out.note_on(74,127)
    time.sleep(1.5)
    midi_out.note_off(74,127)
    time.sleep(.1)

    midi_out.note_on(73,127)
    time.sleep(1.5)
    midi_out.note_off(73,127)
    time.sleep(.1)
    
    midi_out.note_on(74,127)
    time.sleep(.75)
    midi_out.note_off(74,127)
    time.sleep(.1)

    midi_out.note_on(76,127)
    time.sleep(.75)
    midi_out.note_off(76,127)
    time.sleep(.1)    

    midi_out.note_on(77,127)
    time.sleep(2)
    midi_out.note_off(77,127)
    time.sleep(.1)

    midi_out.note_on(79,127)
    time.sleep(.5)
    midi_out.note_off(79,127)
    time.sleep(.1)

    midi_out.note_on(77,127)
    time.sleep(.5)
    midi_out.note_off(77,127)
    time.sleep(.1)    

    midi_out.note_on(76,127)
    time.sleep(.5)
    midi_out.note_off(76,127)
    time.sleep(.1)

    midi_out.note_on(74,127)
    time.sleep(2)
    midi_out.note_off(74,127)

    del midi_out
    pygame.midi.quit()
