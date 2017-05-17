import pygame
from pygame import midi
import music21
import time
import os.path

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
    
def playsong(songtoplay):
    
    for thisNote in songtoplay.streamname:

        playmidinote(thisNote.pitch.midi, songtoplay.speed)

def playfromfile(fileaddress):

    text_file = open(fileaddress, "r")
    songtester = text_file.read(5)

    if songtester == "song:":

        filecontents = text_file.read()
        strippedcontents = filecontents.strip("song: ")
        filenotes = strippedcontents.split(" - ")
        
        for note in filenotes:

            note2 = note.strip("-")
            tempnote = music21.note.Note(note2)
            midinotenum = tempnote.pitch.midi
            playmidinote(midinotenum, 60)

    else:

        print("Error in verifing syntax")


