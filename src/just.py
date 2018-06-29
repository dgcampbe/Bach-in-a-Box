#!/usr/bin/env python
#A library for dealing with Just Intonation
import time
import math
import music21
import playback

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
    time.sleep(2)
    proof = [starting_frequency, [("Perfect Fifth", "+"), ("Perfect Fourth", "-"), ("Perfect Fifth", "+"), ("Perfect Fourth", "-"),  ("Major Third", "-")]]
    interpret(proof)
    print("Playing starting note: " + str(starting_frequency) + " hz, again for comparison.")
    playback.sine_tone(starting_frequency, 1)
    print("Hear the difference?")
    time.sleep(1)
    
def comma_sequence(frequency, direction, iterations):

    for i in range(iterations):

        print(str(frequency))
        playback.sine_tone(frequency, 1)

        if direction == "up":

            frequency *= syntonic_comma

        elif direction == "down":

            frequency /= syntonic_comma        

def interpret(interpret_this):

    note = interpret_this[0]
    print("Playing starting frequency: " + str(note) + " hz.")
    playback.sine_tone(note, 1)
    notes = [note]

    for interval in interpret_this[1]:

        if interval[0].title() in ratios and interval[1]  == "+":

            note = note * ratios[interval[0]]
            print("Playing up a " + interval[0].title() + " to: " + str(note) + " hz.")

        elif interval[0].title() in ratios and interval[1] == "-":

            note = note / ratios[interval[0]]
            print("Playing down a " + interval[0].title() + " to: " + str(note) + " hz.")
 
        else:

            raise Exception("There was an issue parsing intervals.")

        playback.sine_tone(note, 1)
        notes.append(note)

    return notes
       
def main():

    comma_proof(220.0)
    scale(440.0)

ratios = {"Perfect Unison": 1/1, "Minor Second": 16/15, "Major Second": 9/8, "Minor Third": 6/5, "Major Third": 5/4, "Perfect Fourth": 4/3,
          "Augmented Fourth": 45/32, "Diminished Fifth": 64/45, "Perfect Fifth": 3/2, "Minor Sixth": 8/5, "Major Sixth": 5/3, "Minor Seventh": 16/9,
          "Major Seventh": 15/8, "Perfect Octave": 2/1}
syntonic_comma = 1.0125

if __name__ == "__main__":
    
    main()
