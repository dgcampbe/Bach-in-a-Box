#!/usr/bin/env python
#Main music program

#import random module for some randomness in the music
import random
#for writing some files to a specified folder
import os
import time
#Music21 module from MIT
import music21
import playback

class Song(music21.stream.Voice):

    #This creates a Music21 Voice of random monophonoic notes
    def __init__(self, name = "", tempo = 60, length = 12, automake = False):

        super().__init__()
        print("Song created.")
        self.name = name
        self.tempo = tempo
        self.length = length

        if automake != False:

            self.add_notes()

    def __str__(self):

        rep = ""

        for thisNote in self:
                
            rep += str(thisNote.fullName) + "\n"

        return rep

    def add_notes(self, minimum_pitch, maximum_pitch):

        i = 0
            
        while i < int(self.length):
                
            randomnote = random.randint(music21.note.Note(minimum_pitch).pitch.midi, music21.note.Note(maximum_pitch).pitch.midi)
            randommusic21note = music21.note.Note(randomnote)
            self.append(randommusic21note)            
            i += 1
         
        self.save_midi()
        
    def save_midi(self):

        mf = music21.midi.translate.streamToMidiFile(self.transpose(0))

        if not os.path.exists(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), "data", "generated", self.name)):
            
            os.makedirs(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), "data", "generated", self.name))
        
        mf.open(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), "data", "generated", self.name, self.name + ".midi"), 'wb')
        mf.write()
        mf.close()
        
class Voice(Song):

    def __init__(self, pitch):

        print("Voice created.")

        Pitches = ["soprano",
                   "mezzo-soprano",
                   "alto",
                   "tenor",
                   "baritone",
                   "bass"]

        Pitch_Ranges = {"soprano": ["C4", "A5"],
                     "mezzo-soprano": ["A3", "F5"],
                     "alto": ["F3", "D5"],
                     "tenor": ["B2", "G4"],
                     "baritone": ["G2", "E4"],
                     "bass": ["E2", "C4"]}

        if pitch in Pitches:
            
            self.pitch = pitch
            self.range = Pitch_Ranges[self.pitch]
            print("Note range: " + str(self.range))

        else:

            self.pitch = "No pitch specified."

class Counterpoint_Voice(Voice):

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

    def __init__(self, subject = None):

        print("Fugue Voice created.")

        if type(subject, Counterpoint_Voice):
        
            self.subject = subject

        else:

            self.subject = None
    
class Fugue(Fugue_Voice):

    def __init__(self, name, voices, subject = None):

        print("Fugue created.")
        self.name = name
        self.subject = subject
        self.answers = []

    def __str__(self):

        rep = "Fugue: " + "Name- " + self.name + " " + "Subject- " + self.subject.name
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

def main():
    
    #main function where everything happens.
    """
    if input("Play ? (y/n)").lower() == "y":

        print("Playing.....\n")

        print("Done playing.")
    """
    test_song = Song("test", 60, 12)
    test_song.add_notes(40, 60)

    test_fugue = Fugue("test_fugue", 4)
    #test_fugue.create()    

    #Run GUI
    GUI()

    input("Press enter to exit.")

#Run main
main()
