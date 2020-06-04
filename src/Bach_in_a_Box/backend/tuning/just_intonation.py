#!/usr/bin/env python
#A library for dealing with Just Intonation
import time
import math
import sys
import os
import pandas as pd
#allow for the other module to be found
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
from playback import playback

class Interval(object):

    def __init__(self, ratio, direction, length):

        print("Interval created.")
        if not ratios[ratios["Short Name"] == ratio].empty and direction in ("+", "-") and isinstance(length, int):

            self.ratio = ratio
            self.direction = direction
            self.length = length

        else:

            raise Exception("Interval not properly defined.")

    def invert(self):

        if self.direction == "+":
            self.direction = "-"
        else:
            self.direction = "+"

    @property
    def inversion(self):
       return Interval(self.ratio, self.direction, self.length).invert()

class Interval_Stream(object):

    def __init__(self):

        print("Interval Stream created.")
        self.intervals = []
        self.starting_frequency = None

    def add_intervals(self, interval_list):

        for i in interval_list:

            if isinstance(i, Interval):

                self.intervals.append(i)

    def play(self, frequency):

        print("Playing starting frequency: " + str(frequency) + " hz.")
        playback.sine_tone(frequency, 1)
        frequencies = [frequency]

        for interval in self.intervals:

            if interval.direction  == "+":

                frequency *= eval(ratios[ratios["Short Name"] == interval.ratio]["Ratio"].values[0])
                print("Playing up a " + interval.ratio + " to: " + str(frequency) + " hz.")

            elif interval.direction == "-":

                frequency /= eval(ratios[ratios["Short Name"] == interval.ratio]["Ratio"].values[0])
                print("Playing down a " + interval.ratio + " to: " + str(frequency) + " hz.")

            playback.sine_tone(frequency, 1)
            frequencies.append(frequency)

        return frequencies

def scale(start):

    print("Playing scale using invervals based on a single frequency...")
    frequencies_list = {}
    i = 0
    suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16
    time.sleep(1)

    for ratio in ratios["Short Name"]:

        temp = start * eval(ratios[ratios["Short Name"] == ratio]["Ratio"].values[0])
        place = str(i + 1) + suffixes[(i + 1) % 100]
        print("Playing the " + place + " frequency, a " + str(ratio) + " at " + str(temp) + " hz.")
        playback.sine_tone(temp, 1)
        frequencies_list[i] = temp
        i += 1

def comma_proof(starting_frequency):

    print("Proving the need for a syntonic comma. Starting at " + str(starting_frequency) + " hz.")
    proof = [("P5", "+", 1), ("P4", "-", 1), ("P5", "+", 1), ("P4", "-", 1), ("M3", "-", 1)]
    Intervals = []

    for i in proof:

        Intervals.append(Interval(*i))

    proof_stream = Interval_Stream()
    proof_stream.add_intervals(Intervals)
    notes = proof_stream.play(starting_frequency)
    print("Playing starting note: " + str(starting_frequency) + " hz, again for comparison.")
    playback.sine_tone(starting_frequency, 1)
    print("Hear the difference?")

    return notes

def comma_sequence(frequency, direction, iterations):

    for i in range(iterations):

        print(str(frequency))
        playback.sine_tone(frequency, 1)

        if direction == "up":

            frequency *= syntonic_comma

        elif direction == "down":

            frequency /= syntonic_comma

def main():

    comma_proof(220.0)
    scale(440.0)

ratios = pd.read_csv("just_intonation.csv")
syntonic_comma = 1.0125

if __name__ == "__main__":

    main()
