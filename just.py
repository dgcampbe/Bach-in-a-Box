#Project Sebastian
#A program for dealing with Just Intonation tuning as opposed to Equal Temperment
import time
import math
import music21
import playmodule

def scale(start):

    print("Playing scale using invervals based on a single frequency...")
    frequencies_list = {}
    i = 0
    suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16
    time.sleep(1)

    for ratio in ratios:

        temp = start * ratios[ratio]
        place = str(i + 1) + suffixes[(i + 1) % 100]
        print("Playing the " + place + " frequency, a " + str(ratio) + " : " + str(temp) + " hz.")
        playmodule.sine_tone(temp, 1)
        frequencies_list[i] = temp
        i += 1

def comma_proof(starting_frequency):

    print("Proving the need for a syntonic comma. Starting at " + str(starting_frequency) + " hz.")
    time.sleep(2)
    proof = ["Start:" + str(starting_frequency), "Fifth+ ~ Fourth- ~ Fifth+ ~ Fourth- ~ Third-"]
    interprete(proof)
    print("Playing starting note: " + str(starting_frequency) + " hz, again for comparison.")
    playmodule.sine_tone(starting_frequency, 1)
    print("Hear the difference?")
    time.sleep(1)
    
def comma_sequence(frequency, up, iterations):

    for i in range(iterations):

        print(str(frequency))
        playmodule.sine_tone(frequency, 1)

        if up:

            frequency *= syntonic_comma

        elif not up:

            frequency /= syntonic_comma        

def interpret(interpret_this):

    note = float(interpret_this[0][6:])
    string = ""
    print("Playing starting frequency: " + str(note) + " hz.")
    playmodule.sine_tone(note, 1)
    intervals = interpret_this[1].split(" ~ ")

    for interval in intervals:

        if interval.title()[:-1] in ratios:

            if interval[-1] == "+":

                note = note * ratios[interval[:-1]]
                print("Playing up a " + interval.title()[:-1] + " to: " + str(note) + " hz.")
                playmodule.sine_tone(note, 1)

            elif interval[-1] == "-":

                note = note / ratios[interval[:-1]]
                print("Playing down a " + interval.title()[:-1] + " to: " + str(note) + " hz.")
                playmodule.sine_tone(note, 1)

            else:

                print("Syntax is not parsable.")
            
        else:

            print("Syntax is not parsable.")
       
def main():

    comma_proof(220.0)
    scale(440.0)

ratios = {"Unison": 1/1, "Semitone": 16/15, "Second": 9/8, "Minor third": 6/5, "Third": 5/4, "Fourth": 4/3,
          "Tritone": 45/32, "Tritone 2": 25/18, "Fifth": 3/2, "Minor sixth": 8/5, "Sixth": 5/3, "Minor seventh": 16/9,
          "Seventh": 15/8, "Octave": 2/1}
otherratios= { }
syntonic_comma = 1.0125
main()
