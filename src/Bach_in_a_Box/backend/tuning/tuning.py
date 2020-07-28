#!/usr/bin/env python
"""A library for dealing with many tuning systems including just intonation."""
# import time
# import math
import sys
import os
# import numpy as np
# import music21
# import sympy
# import pandas as pd
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
from playback import playback


class Equal_Tempermant(object):
    """Process any equal temperment, not just 12TET."""

    def __init__(self, step_size):

        print("Equal tempermant system initialized.")
        self.step_size = step_size

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class Just_Intonation(object):
    """Process just intonation of any limit."""

    def __init__(self, limit):

        print("Just intonation system initialized.")
        self.limit = limit

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class Arbitrary_Tuning(object):
    """Process arbitrary tuning given ratios."""

    def __init__(self):

        print("Arbitrary tuning system initialized.")

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class Stream(object):
    """Output audio."""

    def __init__(self):

        print("Stream created.")
        self.intervals = []
        self.frequency = None

    def set_intervals(self, intervals):
        """Set intervals."""
        self.intervals = intervals

    def play(self):
        """Play."""
        # below line will be removed.
        self.frequency = 220.0
        print("Playing starting frequency: " + str(self.frequency) + " hz.")
        playback.sine_tone(self.frequency, 1)
        frequencies = [self.frequency]

        for interval in self.intervals:

            self.frequency *= interval
            print("Playing a " + str(interval)
                  + " to: " + str(self.frequency) + " hz.")
            playback.sine_tone(self.frequency, 1)
            frequencies.append(self.frequency)

        return frequencies


def comma_pump(frequency):
    """Comma pump."""
    print("Demonstrating the syntonic comma. Starting at "
          + str(frequency) + " hz.")
    intervals = [3/2, 3/4, 3/2, 3/4, 4/5]
    stream = Stream()
    stream.set_intervals(intervals)
    notes = stream.play()
    print("Playing starting note: " + str(frequency)
          + " hz, again for comparison.")
    playback.sine_tone(frequency, 1)
    print("Hear the difference?")
    return notes


def main():
    """Main."""
    # just_intonation = pd.read_csv("just_intonation.csv")
    # alpha_scale = pd.read_csv("alpha_scale.csv")
    # beta_scale = pd.read_csv("beta_scale.csv")
    # gamma_scale = pd.read_csv("gamma_scale.csv")
    # syntonic_comma = 1.0125
    comma_pump(220.0)


if __name__ == "__main__":

    main()
