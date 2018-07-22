#!/usr/bin/env python
#composition module

import random
import os #file writing
import time
import music21 #Music21 module from MIT
from backend import playback

class Voice(music21.stream.Voice):

    #This creates a Music21 Voice of random monophonoic notes
    def __init__(self, name = "", tempo = 60, length = 12, pitch = None, automake = False):

        print("Voice created.")
        super().__init__()
        self.name = name
        self.tempo = tempo
        self.length = length

        Pitch_Ranges = {"soprano": ("C4", "A5"),
                     "mezzo-soprano": ("A3", "F5"),
                     "alto": ("F3", "D5"),
                     "tenor": ("B2", "G4"),
                     "baritone": ("G2", "E4"),
                     "bass": ("E2", "C4")}
        
        if pitch in Pitch_Ranges:
            
            self.pitch = pitch
            self.range = Pitch_Ranges[self.pitch]

        else:

            self.pitch = "No pitch specified."
            self.range = "No range specified."
    
        self.default_save_directory = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir), "data", "generated", self.name)
        
        if automake != False:

            self.add_notes()

    def __str__(self):

        rep = ""

        for thisNote in self:
                
            rep += str(thisNote.fullName) + "\n"

        return rep

    def add_notes(self):

        i = 0
            
        while i < int(self.length):
                
            randomnote = random.randint(music21.note.Note(self.range[0]).pitch.midi, music21.note.Note(self.range[1]).pitch.midi)
            randommusic21note = music21.note.Note(randomnote)
            self.append(randommusic21note)            
            i += 1
         
        self.save_midi()
        
    def save_midi(self):

        #self.show("midi")
        mf = music21.midi.translate.streamToMidiFile(self)

        if not os.path.exists(self.default_save_directory):
            
            os.makedirs(self.default_save_directory)
        
        mf.open(os.path.join(self.default_save_directory, self.name + ".midi"), 'wb')
        mf.write()
        mf.close()

class Counterpoint_Voice(Voice):

    #later this will allow for specific rules for voices intended to be used for counterpoint
    def __init__(self):

        print("Counterpoint Voice created.")

        #the following text is just reference for me when I get to writing this part of the program- credit goes to wikipedia
        
        #spieces
        """
        1. Note against note;
        2. Two notes against one;
        3. Four notes against one;
        4. Notes offset against each other (as suspensions);
        5. All the first four species together, as "florid" counterpoint.
        """
        #rules of counterpoint
        """
        The following rules apply to melodic writing in each species, for each part:

        The final must be approached by step. If the final is approached from below, then the leading tone must be raised in a minor key (Dorian, Hypodorian, Aeolian, Hypoaeolian), but not in Phrygian or Hypophrygian mode. Thus, in the Dorian mode on D, a C♯ is necessary at the cadence.[5]
        Permitted melodic intervals are the perfect fourth, fifth, and octave, as well as the major and minor second, major and minor third, and ascending minor sixth. The ascending minor sixth must be immediately followed by motion downwards.
        If writing two skips in the same direction—something that must be only rarely done—the second must be smaller than the first, and the interval between the first and the third note may not be dissonant. The three notes should be from the same triad; if this is impossible, they should not outline more than one octave. In general, do not write more than two skips in the same direction.
        If writing a skip in one direction, it is best to proceed after the skip with motion in the other direction.
        The interval of a tritone in three notes should be avoided (for example, an ascending melodic motion F–A–B♮)[citation needed] as is the interval of a seventh in three notes.
        There must be a climax or high point in the line countering the cantus firmus. This usually occurs somewhere in the middle of exercise and must occur on a strong beat.
        An outlining of a seventh is avoided within a single line moving in the same direction.

        And, in all species, the following rules govern the combination of the parts:

        The counterpoint must begin and end on a perfect consonance.
        Contrary motion should predominate.
        Perfect consonances must be approached by oblique or contrary motion.
        Imperfect consonances may be approached by any type of motion.
        The interval of a tenth should not be exceeded between two adjacent parts unless by necessity.
        Build from the bass, upward.
        """
        
class Fugue_Voice(Counterpoint_Voice):

    #later this will allow for specific rules for voices intended to be used just for fugues
    def __init__(self, subject = None):

        print("Fugue Voice created.")

        if type(subject, Counterpoint_Voice):
        
            self.subject = subject

        else:

            self.subject = None
    
class Fugue(Fugue_Voice):

    #this is a fugue -- currently does basically nothing
    def __init__(self, name, voices, subject = None):

        print("Fugue created.")
        self.name = name
        self.voices = {"Subject": subject}

        for i in range(voices - 1):

            self.voices["Answer" + str(i + 1)] = None

    def __str__(self):

        rep = "Fugue:"

        for voice in self.voices:

            rep += str(voice)
            
        return rep

    def counterpoint(self):

        print("Counterpoint is hard.")

    def createanswer(self, semitones):

        rep = None
        
        for thisNote in self.subject:

             tempNote = thisNote.transpose(semitones)

        self.answers.append("")
        
    def createcountersubject(self):

        print("This program can't create a countersubject yet :(")
