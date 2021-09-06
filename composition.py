#!/usr/bin/env python
"""Composition."""
import random
import os
import math
import music21
import mido

# Default Global Variables
ranges = open("ranges.json")
ranges = eval(ranges.read())


class Voice(music21.stream.Voice):
    """Create a Music21 Voice of random notes from a selected scale."""

    def __init__(self,
                 name="",
                 scale=music21.scale.MajorScale("C"),
                 length=12,
                 pitch="tenor"):

        print("Voice created.")
        super().__init__()
        self.name = name
        self.scale = scale
        self.length = length
        self.intervals = []
        self.save_dir = os.path.join("generated", self.name)
        self.pitch = pitch
        self.range = ranges[self.pitch]

    def __str__(self):
        """String."""
        return "".join(str(note.fullName) + "\n" for note in self)

    def compose(self):
        """Compose."""
        self.append(music21.note.Note(self.scale.getTonic()))
        notes = [
            music21.note.Note(str(note))
            for note in self.scale.getPitches(
                self.range[0].pitch.name, self.range[1].pitch.name
            )
        ]
        while len(self) != self.length:
            self.append(music21.note.Note(random.choice(notes).pitch.name))
        self.save_midi()

    def save_midi(self):
        """Save to midi."""
        # self.show("midi")
        midi_file = music21.midi.translate.streamToMidiFile(self)
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        midi_file.open(os.path.join(self.save_dir,
                                    self.name + ".mid"), 'wb')
        midi_file.write()
        midi_file.close()


class Fugue:
    """Fugue."""

    def __init__(self, name, voices, subject=None):

        print("Fugue created.")
        super().__init__()
        self.name = name
        self.voice_list = [subject] + [[None], * len(voices)]

    def __str__(self):
        """String."""
        return self.voice_list

    def generate_answer(self):
        """Generate answer."""
        print("Answer created.")

    def generate_countersubject(self):
        """Generate countersubject."""
        print("This program can't create a countersubject yet :(")


class Canon:
    """Canon."""

    def __init__(self, lead_chords, voice_count):

        self.lead_chords = lead_chords
        self.voice_count = voice_count
        print("Canon created.")
        super().__init__()

    def generate_random_chords(self):
        """Generate random chords."""
        print("Generating random chords")


class CrabCanon:
    """Crab canon from Bach's musical offering."""

    def __init__(self):

        print("Crab Canon created.")


def midi_to_dectalk(midi, mode="phone"):
    """Convert midi files with monophonic tracks to be sung in dectalk."""
    # dectalk notes range from C2 to C5 and are numbered 36 less than midi
    # this function is currently very buggy
    print("Converting to dectalk.")
    midi_file = mido.MidiFile(midi)
    words = ["uw", "ax", "ow", "ah"]
    song = []
    for track in midi_file.tracks:
        if mode == "phone":
            voice = "[:phone on]\n"
        elif mode == "sing":
            voice = "[:phoneme arpabet speak on]\n"
        for note in track:
            if note.type in ("note_on", "note_off") and note.time != 0:
                freq = math.floor(music21.pitch.Pitch(note.note).frequency)
                duration = math.floor(note.time)
                if mode == "phone":
                    voice += "[:tone " + str(freq) \
                             + "," + str(duration) + "]\n"
                elif mode == "sing":
                    voice += "[" + words[0] + "<" + str(freq) \
                             + "," + str(note.note - 36) + ">]\n"
        song.append(voice)
    for i, j in enumerate(song):
        with open(os.path.join(os.path.split(midi)[0], str(i) + ".txt"),
                  "w") as track:
            track.write(j)
    print("Dectalk conversion finished.")
    return song


def main():
    """Main."""
    midi = os.path.join("examples", "The_Art_of_Fugue_Contrapunctus_1.mid")
    midi_to_dectalk(midi)


if __name__ == "__main__":

    main()
