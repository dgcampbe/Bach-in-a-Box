#!/usr/bin/env python
#main module

import composition
#from composition import composition
from user_interface import interface

def main():
    
    test_voice = composition.Voice("test", 60, 12, "tenor")
    test_voice.add_notes()
    print(str(test_voice))
    test_fugue = composition.Fugue("test_fugue", 4)
    #test_fugue.create()    

    #Run interface
    interface.main()

    input("Press enter to exit.")

#Run main
main()
