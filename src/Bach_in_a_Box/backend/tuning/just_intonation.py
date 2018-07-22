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

    def __init__(self, ratio, direction):

        print("Interval created.")

        if ratio in ratios and direction in ("+", "-"):

            self.ratio = ratio
            self.direction = direction

        else:

            raise Exception("Interval not properly defined. Something is probably programmed wrong.")

class IntervalStream(object):

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

            if interval.ratio.title() in ratios and interval.direction  == "+":

                frequency = frequency * ratios[interval.ratio.title()]
                print("Playing up a " + interval.ratio.title() + " to: " + str(frequency) + " hz.")

            elif interval.ratio.title() in ratios and interval.direction == "-":

                frequency = frequency / ratios[interval.ratio.title()]
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
    interval_list = [("Perfect Fifth", "+"), ("Perfect Fourth", "-"), ("Perfect Fifth", "+"), ("Perfect Fourth", "-"),  ("Major Third", "-")]
    Intervals = []

    for i in interval_list:

        Intervals.append(Interval(i[0], i[1]))

    proof_stream = IntervalStream()
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

ratios = {"Perfect Unison": 1/1, "Minor Second": 16/15, "Major Second": 9/8, "Minor Third": 6/5, "Major Third": 5/4, "Perfect Fourth": 4/3,
          "Augmented Fourth": 45/32, "Diminished Fifth": 64/45, "Perfect Fifth": 3/2, "Minor Sixth": 8/5, "Major Sixth": 5/3, "Minor Seventh": 16/9,
          "Major Seventh": 15/8, "Perfect Octave": 2/1}
syntonic_comma = 1.0125

if __name__ == "__main__":
    
    main()
