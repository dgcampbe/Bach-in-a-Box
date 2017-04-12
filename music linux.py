#!/usr/bin/env python

#This program should be able to write music. Quality is not assured. Now on Github :). I will try integrating this with Alda. I am very sure this violates every rule of programming best practices

#import random module for some randomness in the music
import random
#import tkinter for GUI
from tkinter import *
#for writing some files to a specified folder
import os.path

#some variables that need to be defined
savepath = "C:/PythonMusic/textfiles/"
guisong = 0
Note_list = ["A","B","C","D","E","F","G"]
Octaves = [1,2,3,4,5,6]

#Getting all the GUI related stuff out of the way for later. I need to have it defined before I call it in main(), because no forward declaration in Python :(

class Application(Frame):

    #Application class, where the GUI magic happens
    def __init__(self, master):

        #maybe create a variable to keep track of different guisongs like:
        #self.guisongnum = 1
        #then increment it as guisongs are created
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.buttonclick = 0

    def create_widgets(self):

        self.create_text()
        self.create_checks()
        self.create_labels()
        self.create_buttons()

    def create_labels(self):

        self.musiclabel = Label(self, text = "This is a simple music program. Please Enjoy.")
        self.musiclabel.grid(row = 0, column = 0, columnspan = 6, sticky = W)

        self.musiclabel2 = Label(self, text = "Number of notes for the song: ")
        self.musiclabel2.grid(row = 1, column = 0, columnspan = 2, sticky = W)

    def create_buttons(self):
                
        self.musicbutton1 = Button(self)
        self.musicbutton1.grid(row = 5, column = 1, columnspan = 1, sticky = W)
        self.musicbutton1.configure(text = "Save to file.")
        
        self.musicbutton2 = Button(self)
        self.musicbutton2.grid(row = 1, column = 4, sticky = W)
        self.musicbutton2.configure(text = "Submit")

        self.musicbutton3 = Button(self)
        self.musicbutton3.grid(row = 5, column = 0, columnspan = 1, sticky = W)
        self.musicbutton3.configure(text = "Usefull button.")
              
        #remember to change this value as needed (headache avoided)
        self.musicbutton2.configure(command = self.submit)
        self.musicbutton1.configure(command = self.savetofile)
        #I think I need to create a global variable called guisong and then edit the global version here to people able to use this method's version elseware
        global guisong
        guisong = Song("guisong", "4", "3", "2")
        #idk why the following commented line doesn't work, so I made a work around
        #self.musicbutton3.configure(command = self.puttextinbox(str(guisong), "False"))
        self.musicbutton3.configure(command = self.specialputinbox)
        
    def create_text(self):

        self.firstentry = Entry(self)
        self.firstentry.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        self.display = Text(self, width = 50, height = 10, wrap = WORD)
        self.display.grid(row = 2, column = 0, columnspan = 5, sticky = W)
        self.puttextinbox("This is where results will go. The console is more verbose for debugging.", "False")

    def specialputinbox(self):

        #stupid, but it works :P
        #This is the work around for the issue in self.create_buttons()
        #self.puttextinbox(str(guisong), "False")
        guisong.add_notes()
        #I need to fix this so the dictionary string isn't all weird memory addresses
        #self.puttextinbox(str(guisong.notedictionary), "False")
        self.puttextinbox(str(guisong.print_songlist("False")), "False")
    
    def create_checks(self):
        
        self.bool1 = BooleanVar()
        self.bool2 = BooleanVar()
        self.bool3 = BooleanVar()
        """        
        self.check1 = Checkbutton(self)
        self.check1.configure(variable = self.bool1)
        self.check1.configure(command = self.submit)
        self.check1.grid(row = 4, column = 5, sticky = S)
        #might want to not use a variable to save space idk
        """
        
    def update(self):

        self.buttonclick += 1
        self.musicbutton1.configure(text = "Total Clicks: " + str(self.buttonclick))
        print(str(self.buttonclick))

    def submit(self):

        global guisong
        textboxstuff = self.firstentry.get()

        if textboxstuff:

            #moving this from the console to GUI would be good
            print("The Number of Notes is: " + textboxstuff)
            numberofnotes = textboxstuff
            guisong = Song("guisong", "5", "4", textboxstuff)
            print(guisong)
            self.puttextinbox("Song of length " + str(textboxstuff) + " has been created. Press the other button to see the results here.", "False")
            
        else:

            print("No Number provided.")

    def puttextinbox(self, putinbox, append):

        if append == "False":

            self.display.delete(0.0, END)
            self.display.insert(0.0, putinbox)

        else:

            self.display.insert(0.0, putinbox)

    def savetofile(self):

        #Going to work on this so that it can actually save to file
        guisong.print_songlist("True")

#I am going to rewrite the program to work with tkinter with pack and pack-forget to hide elements

def GUI():

    #Creates GUI from the Application class.
    print("GUI started.")
    root = Tk()
    root.title("Python Music Program")
    root.geometry("600x400")
    app = Application(root)
  
    #Run mainloop
    root.mainloop()

#some classes defined below

class Note(object):

    #This is used to create a note that will being strung together to form music
    def __init__(self, name, letter, octave, sharp):

        print("A new note has been created.")
        self.name = name
        self.letter = letter
        self.octave = octave
        self.sharp = sharp
        print(self)
        
    def __str__(self):

        rep = "note: "
        rep += self.name + " " + self.letter + self.octave

        if self.sharp == "True":
            rep += " sharp"

        else:

            rep += " not sharp"

        return rep

    def changeoctave(self,numofoct):

        try:

            self.octave = int(self.octave) + int(numofoct)
            self.octave = str(self.octave)

        except:

            input("Error type 5 occured: Please Debug")

    def changenote(self,newnote):

        if newnote in Note_list:

            self.letter = newnote

        else:

            input("An illegal note change was attempted and stopped. Notes can only be called something A-G.")

    def swapsharpstate(self):

        if self.sharp == "True":

            self.sharp = "False"

        elif self.sharp == "False":

            self.sharp = "True"

        else:

            input("A note sharp state swap was attempted but an issue occurred and as a preventive measure, was halted. You should debug this.")

class Song(object):

    #This is used to makes a groups of notes to create a song (or maybe just a single "voice" of a song)
    def __init__(self, name, speed, pitch, length):

        print("A new song has been created.")

        self.notedictionary = {}
        self.name = name
        self.speed = speed
        self.pitch = pitch
        self.length = length

    def __str__(self):

        rep = "song: "
        rep +=  "Name-" + str(self.name) + " " + "Speed-" + str(self.speed) + " " + "Pitch-" + str(self.pitch) + " " + "Length-" + str(self.length)

        if self.notedictionary:
            
            rep += " ------Note dictionary avalible."

        return rep

    def add_notes(self):

        #maybe integrate the append_notes function by using an input that tells whether the dictionary should be overwritten or added to
        self.songlist = []
        self.notedictionary = {}

        for i in range(int(self.length)):

            #Might want to work on making less random :P
            randomnote = random.choice(Note_list)
            randomoctave = random.choice(Octaves)
            randomsharp = random.randint(0,6)

            if randomsharp == 1:

                issharp = "+"
            #testing a small change here for compatibility with Alda, still has a long way to go before it actually works
            #This needs to be reworked to work more like most __str__ functions do by using the += thing and returning a value instead of creating a variable that is added onto other stuff
            
            else:

                issharp = ""

            self.notedictionary["note" + str(i)] = Note(str("note" + str(i)),str(randomnote),str(randomoctave), str(issharp))
            randomnoteandoctave = str(randomnote) + str(randomoctave) + str(issharp)
            self.songlist.append(str(randomnoteandoctave))

        print("Notes added to song. Check text file for results.")
        #write results to file
        text_file_name = os.path.join(savepath, "testmusic.txt")
        text_file = open(text_file_name, "w")
        text_file.write("song: " + str(self.songlist))
        text_file.close()

    def print_songlist(self, console):

        #work more like a __str__ should

        if console == "True":
            
            print("song: " + str(self.songlist))
            write = input("Write music above to file? y or n ")            

            if write == "y":

                filename = input("What should the text file be called? Do NOT include the .txt file extension")
                text_file_name = os.path.join(savepath, str(filename) + ".txt")
                text_file = open(text_file_name, "w")
                text_file.write("song: " + str(self.songlist))
                text_file.close()
                print("Song written to " + filename + ".txt")

            else:

                print("Song not written.")

        else:
            
            rep = "song: "
            rep += str(self.songlist)
            return rep
            
    def append_notes(self, numofnotestoappend):

        if self.notedictionary and numofnotestoappend > 0:
            
            newnotenum = len(self.notedictionary) + 1
            
            for i in range(numofnotestoappend):

                newnotename = "note" + str(newnotenum)
                
                self.notedictionary[newnotename] = Note(newnotename, "A", "1", "True")
                self.length += 1
                newnotenum += 1
                print("Note appended to song. This note has random nonsense for letter and octave. You should change that.")

        else:
            
            print("Error type 11: Appending note to song failed.")

class fugue(object):

    #Not even close to done
    def __init__(self, name, subjectsong):

        print("A new fugue has been created")
        self.name = name
        self.subjectsong = subjectsong

    def __str__(self):

        rep = "Fugue: "
        #might want to do a bit of work the string value of other objects to make this better
        rep += "Name- " + self.name + " " + "Subject- " + str(self.subjectsong)
        return rep

    def counterpoint(self):

        #idk what to do here so here is a print function that portrays my feelings :P
        print("Counterpoint is hard")


def main():

    #main function where everything happens
    #gather some input (this will be moved to tkinter eventually)
    print("This program should be able to write music. Quality is not assured (quanity might, though). Work in progress.")
    lengthofsong = input("What length do you want? Default is fifty.")
    style = input("Please input a style (speed, length, pitch) of music: (this prompt doesn't do anything yet, just looks pretty.)")

    #testing to see how much of this stuff doesn't work
    notetest = Note("notetest","C","4","False")
    notetest.changeoctave(1)
    notetest.changenote("A")
    notetest.swapsharpstate()
    print(notetest)

    if not lengthofsong == "":

        try:

            song1 = Song("song1",3,4,int(lengthofsong))

        except:

            input("That wasn't a number, idiot! :P Defaulting to fifty.")
            song1 = Song("song1",3,4,50)            

    else:

        song1 = Song("song1",3,4,50)        

    song1.add_notes()
    song1.print_songlist("True")
    print(song1)
    song1.append_notes(3)
    print(song1)

    #testing with the fugue function that is being worked on
    fuguesong1 = Song("fuguesong1",3,4,8)
    testfugue1 = fugue("testfugue1", song1)
    print(testfugue1)

    print(song1.print_songlist("False"))
    #Run GUI
    GUI()
    
    input("Press enter to exit.")

#Run main
main()

#This is the end for now
