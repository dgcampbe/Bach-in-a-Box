#!/usr/bin/env python
#main module

import composition
import user_interface.user_interface

def main():
    
    """
    if input("Play ? (y/n)").lower() == "y":

        print("Playing.....\n")

        print("Done playing.")
    """
    test_song = composition.Song("test", 60, 12)
    test_song.add_notes(40, 60)

    test_fugue = composition.Fugue("test_fugue", 4)
    #test_fugue.create()    

    #Run interface
    user_interface.user_interface.main()

    input("Press enter to exit.")

#Run main
main()
