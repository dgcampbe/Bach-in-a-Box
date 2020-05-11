#!/usr/bin/env python
#main module
import music21
import composition
#from composition import composition
from user_interface import interface

def main():

    test_voice = composition.Voice("test", music21.scale.MajorScale("D"), 12, "tenor")
    test_voice.compose()
    print(str(test_voice))
    #test_fugue = composition.Fugue("test_fugue", 4)
    #test_fugue.create()    

    #Run interface
    #interface.main()

    input("Press enter to exit.")

#Run main
main()
