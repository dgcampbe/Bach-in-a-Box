#!/usr/bin/env python
"""Composition."""

import random
# file writing
import os
# import time
# import numpy
# import scipy
import music21
# from backend import playback

# Default Global Variables
Pitch_Ranges = {"soprano": ("C4", "A5"),
                "mezzo-soprano": ("A3", "F5"),
                "alto": ("F3", "D5"),
                "tenor": ("B2", "G4"),
                "baritone": ("G2", "E4"),
                "bass": ("E2", "C4")}

for i in Pitch_Ranges:
    Pitch_Ranges[i] = tuple([music21.note.Note(x) for x in Pitch_Ranges[i]])


class Voice(music21.stream.Voice):
    """Create a Music21 Voice of random notes from a selected scale."""

    def __init__(self, name="", scale=music21.scale.MajorScale("C"), length=12, pitch="tenor"):

        print("Voice created.")
        super().__init__()
        self.name = name
        self.scale = scale
        self.length = length
        self.default_save_directory = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir), "data", "generated", self.name)

        if pitch in Pitch_Ranges:

            self.pitch = pitch
            self.range = Pitch_Ranges[self.pitch]

        else:
            raise

    def __str__(self):
        """String."""
        rep = ""

        for thisNote in self:

            rep += str(thisNote.fullName) + "\n"

        return rep

    def compose(self):
        """Compose."""
        self.append(music21.note.Note(self.scale.getTonic()))
        self.intervals = []
        notes = [music21.note.Note(str(x)) for x in self.scale.getPitches(self.range[0].pitch.name, self.range[1].pitch.name)]

        while not len(self) == self.length:

            self.append(music21.note.Note(random.choice(notes).pitch.name))

        self.save_midi()

    def save_midi(self):
        """Save to midi."""
        # self.show("midi")
        mf = music21.midi.translate.streamToMidiFile(self)

        if not os.path.exists(self.default_save_directory):

            os.makedirs(self.default_save_directory)

        mf.open(os.path.join(self.default_save_directory,
                             self.name + ".midi"), 'wb')
        mf.write()
        mf.close()


class Counterpoint_Voice(Voice):
    """Counterpoint voice."""

    def __init__(self):

        print("Counterpoint Voice created.")
        super().__init__()


class Counterpoint(object):
    """Counterpoint."""

    def __init__(self, species, voice_count):

        self.voice_count = voice_count
        self.voices = []

    def compose(self):
        """Compose."""
        for count in self.voice_count:

            self.voices.append(Counterpoint_Voice().addnotes())


class Fugue_Voice(Counterpoint):
    """Fugue voice."""

    def __init__(self, subject=None):

        print("Fugue Voice created.")
        super().__init__()
        if isinstance(subject, Counterpoint_Voice):

            self.subject = subject

        else:

            self.subject = None


class Fugue(Fugue_Voice):
    """Fugue."""

    def __init__(self, name, voices, subject=None):

        print("Fugue created.")
        super().__init__()
        self.name = name
        self.voice_list = [subject] + [[None] for x in range(voices)]

    def __str__(self):
        """String."""
        return self.voice_list

    def counterpoint(self):
        """Counterpoint."""
        print("Counterpoint is hard.")

    def create_answer(self, semitones):
        """Create answer."""
        print("Answer created.")

    def createcountersubject(self):
        """Create countersubject."""
        print("This program can't create a countersubject yet :(")


class Canon_Voice(Counterpoint_Voice):
    """Canon voice."""

    def __init__(self):

        print("Canon Voice created.")
        super().__init__()


class Canon(Canon_Voice):
    """Canon."""

    def __init__(self, lead_chords, voice_count):

        self.lead_chords = lead_chords
        self.voice_count = voice_count
        print("Canon created.")
        super().__init__()

    def gen_rand_chords(self):
        """Generate random chords."""
        print("Generating random chords")


class Crab_Canon(Canon):
    """Crab canon from Bach's musical offering."""

    def __init__(self):

        print("Crab Canon created.")
