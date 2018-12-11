#!/usr/bin/env python
#composition module

import random
import os #file writing
import time
#import numpy
#import scipy
import music21 #Music21 module from MIT
from backend import playback

#Default Global Variables
Pitch_Ranges = {"soprano": ("C4", "A5"),
             "mezzo-soprano": ("A3", "F5"),
             "alto": ("F3", "D5"),
             "tenor": ("B2", "G4"),
             "baritone": ("G2", "E4"),
             "bass": ("E2", "C4")}

for i in Pitch_Ranges: Pitch_Ranges[i] = tuple([music21.note.Note(x) for x in Pitch_Ranges[i]])
print(str(Pitch_Ranges))

#Classes
class Voice(music21.stream.Voice):

    #This creates a Music21 Voice of random monophonoic notes
    def __init__(self, name = "", first_note = "C4", length = 12, pitch = "tenor"):

        print("Voice created.")
        super().__init__()
        self.name = name
        self.first_note = music21.note.Note(first_note)
        self.length = length
        self.default_save_directory = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir), "data", "generated", self.name)
        
        if pitch in Pitch_Ranges:
            
            self.pitch = pitch
            self.range = Pitch_Ranges[self.pitch]

        else: raise
        
    def __str__(self):

        rep = ""

        for thisNote in self:
                
            rep += str(thisNote.fullName) + "\n"

        return rep

    def add_notes(self):

        self.append(self.first_note)
        self.intervals = []
        good_intervals = [music21.interval.Interval(x) for x in ["m2", "M2", "m3", "M3", "P4", "P5", "P8"]]
        good_intervals += [x.reverse() for x in good_intervals]
           
        while not len(self) == self.length:

            previous_note = self[-1]
            random_interval = random.choice(good_intervals)

            if previous_note.transpose(random_interval).pitch >= self.range[0].pitch and previous_note.transpose(random_interval).pitch <= self.range[1].pitch:

                self.append(previous_note.transpose(random_interval))
                self.intervals.append(random_interval)


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
        super().__init__()
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
        super().__init__()
        if isinstance(subject, Counterpoint_Voice):
        
            self.subject = subject

        else:

            self.subject = None
    
class Fugue(Fugue_Voice):

    #this is a fugue -- currently does basically nothing
    def __init__(self, name, voices, subject = None):

        print("Fugue created.")
        super().__init__()
        self.name = name
        self.voice_list = [subject] + [[None] for x in range(voices)]

    def __str__(self):

        rep = "Fugue:"

        for voice in self.voice_list:

            rep += str(voice)
            
        return rep

    def counterpoint(self):

        print("Counterpoint is hard.")

    def create_answer(self, semitones):

        pass
        
    def createcountersubject(self):

        print("This program can't create a countersubject yet :(")

class Canon_Voice(Counterpoint_Voice):
    #voice in a canon
    def __init__(self):

        print("Canon Voice created.")        
        super().__init__()

class Canon(Canon_Voice):
    #canon
    def __init__(self):

        print("Canon created.")        
        super().__init__()

    def gen_rand_chords(self):

        print("Generating random chords for ya'")

class Crab_Canon(Canon):
    #crab canon- as in the crab canon from Bach's musical offering
    def __init__(self):

        print("Crab Canon created.")
