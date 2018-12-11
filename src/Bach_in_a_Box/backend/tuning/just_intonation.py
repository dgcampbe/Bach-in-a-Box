#!/usr/bin/env python
#A library for dealing with Just Intonation
import time
import math
import sys
import os
#allow for the other module to be found
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
from playback import playback

class Interval(object):

    def __init__(self, ratio, direction, length):

        print("Interval created.")
        #instead of using a + or - I will eventually just invert the ratio number
        if ratio in ratios and direction in ("+", "-") and isinstance(length, int):

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

        print("IntervalStream created.")
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

                frequency = frequency * ratios[interval.ratio]
                print("Playing up a " + interval.ratio.title() + " to: " + str(frequency) + " hz.")

            elif interval.direction == "-":

                frequency = frequency / ratios[interval.ratio]
                print("Playing down a " + interval.ratio.title() + " to: " + str(frequency) + " hz.")

            playback.sine_tone(frequency, 1)
            frequencies.append(frequency)

        return frequencies
                
def scale(start):

    print("Playing scale using invervals based on a single frequency...")
    frequencies_list = {}
    i = 0
    suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16
    time.sleep(1)

    for ratio in ratios:

        temp = start * ratios[ratio]
        place = str(i + 1) + suffixes[(i + 1) % 100]
        print("Playing the " + place + " frequency, a " + str(ratio) + " at " + str(temp) + " hz.")
        playback.sine_tone(temp, 1)
        frequencies_list[i] = temp
        i += 1

def comma_proof(starting_frequency):

    print("Proving the need for a syntonic comma. Starting at " + str(starting_frequency) + " hz.")
    interval_list = [("Perfect Fifth", "+", 1), ("Perfect Fourth", "-", 1), ("Perfect Fifth", "+", 1), ("Perfect Fourth", "-", 1),  ("Major Third", "-", 1)]
    Intervals = []

    for i in interval_list:

        Intervals.append(Interval(i[0], i[1], i[2]))

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

#this data is going to be moved into a pandas dataframe so that the full names and shorter names will both be avalible.
ratios = {"Perfect Unison": 1/1, "Minor Second": 16/15, "Major Second": 9/8, "Minor Third": 6/5, "Major Third": 5/4, "Perfect Fourth": 4/3,
          "Augmented Fourth": 45/32, "Diminished Fifth": 64/45, "Perfect Fifth": 3/2, "Minor Sixth": 8/5, "Major Sixth": 5/3, "Minor Seventh": 16/9,
          "Major Seventh": 15/8, "Perfect Octave": 2/1}
#ratios = {"P1": 1/1, "m2": 16/15, "M2": 9/8, "m3": 6/5, "M3": 5/4, "P4": 4/3,
#          "Augmented Fourth": 45/32, "Diminished Fifth": 64/45, "P5": 3/2, "m6": 8/5, "M6": 5/3, "m7": 16/9, "M7": 15/8, "P8": 2/1}

syntonic_comma = 1.0125

if __name__ == "__main__":
    
    main()
