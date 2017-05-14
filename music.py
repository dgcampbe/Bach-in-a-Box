#Main music program

#import random module for some randomness in the music
import random
#import tkinter for GUI (need to change this so that it doesn't import all)
from tkinter import *
#for file and folder dialogs
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
#for writing some files to a specified folder
import os.path
#Pygame is here!!!
import pygame
from pygame import midi
#import livewires
import time
#Music21 module from MIT (absolutely amazing)
import music21
#A module I made for testing using pygame for playing MIDIs(included)
import bach_aof
import playmodule

#some variables that need to be defined
defaultsavepath = "C:/PythonMusic/textfiles/"
savepath = defaultsavepath
guisong = 0
guisongdict = {}
Note_list = ["A","B","C","D","E","F","G"]
Octaves = [1,2,3,4,5,6]

class Application(Frame):

    #Application class, where the GUI magic happens
    def __init__(self, master):

        self.guisongnum = 1
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
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

        self.musiclabel3 = Label(self, text = "Save location:")
        self.musiclabel3.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        self.musiclabel4 = Label(self, text = ".txt")
        self.musiclabel4.grid(row = 6, column = 2, columnspan = 1, sticky = W)

    def create_buttons(self):
                
        self.musicbutton1 = Button(self)
        self.musicbutton1.grid(row = 6, column = 3, columnspan = 1, sticky = W)
        self.musicbutton1.configure(text = "Save to file.")
        
        self.musicbutton2 = Button(self)
        self.musicbutton2.grid(row = 1, column = 4, sticky = W)
        self.musicbutton2.configure(text = "Submit")

        self.musicbutton3 = Button(self)
        self.musicbutton3.grid(row = 5, column = 0, columnspan = 1, sticky = W)
        self.musicbutton3.configure(text = "Display new song in textbox.")

        self.musicbutton4 = Button(self)
        self.musicbutton4.grid(row = 6, column = 5, columnspan = 1, sticky = W)
        self.musicbutton4.configure(text = "Play song.")
              
        #remember to change this value as needed (headache avoided)
        self.musicbutton2.configure(command = self.submit)
        self.musicbutton1.configure(command = self.savetofile1)
        self.musicbutton3.configure(command = self.specialputinbox)
        self.musicbutton4.configure(command = self.playguisong)
        
    def create_text(self):

        self.firstentry = Entry(self)
        self.firstentry.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        self.savetofile = Entry(self)
        self.savetofile.grid(row = 6, column = 1, columnspan = 1, sticky = W)

        self.display = Text(self, width = 50, height = 10, wrap = WORD)
        self.display.grid(row = 2, column = 0, columnspan = 5, sticky = W)
        self.puttextinbox("This is where results will go. The console is more verbose for debugging.", "False")

    def specialputinbox(self):

        #this is so tkinter button config is happy

        try:

            self.puttextinbox(str(guisongdict[self.guisongnum - 1].print_songlist()), "False")

        except:

            self.puttextinbox("An issue occured where there was no guisong created first.", "False")
        
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
        
    def submit(self):

        global guisong
        textboxstuff = self.firstentry.get()

        if textboxstuff:

            numberofnotes = textboxstuff
            guisongname = "guisong" + str(self.guisongnum)
            guisongdict[self.guisongnum]  = Song("guisong" + str(self.guisongnum), "5", "4", textboxstuff)
            guisongdict[self.guisongnum].add_notes()

            print(guisongdict[self.guisongnum])            
            self.guisongnum += 1
            self.puttextinbox("Song of length " + str(textboxstuff) + " has been created. Press the display results button to see the results here.", "False")
            
        else:

            print("No Number provided.")
            self.puttextinbox("No Number provided.", "False")

    def puttextinbox(self, putinbox, append):

        if append == "False":

            self.display.delete(0.0, END)
            self.display.insert(0.0, putinbox)

        else:

            self.display.insert(0.0, putinbox)

    def savetofile1(self):

        print("Save direcotry prompt:")
        inputpath = askdirectory()
        filename = self.savetofile.get()
        
        if not inputpath == "":

            global savepath
            savepath = inputpath

        guisongdict[self.guisongnum - 1].savesonglist(filename)

    def playguisong(self):

        playsong(guisongdict[self.guisongnum - 1].songlist, 1)

#I am going to rewrite the program to work with tkinter with pack and pack-forget to hide elements (maybe a complete rewrite in node.js :P)

def GUI():

    #now enter can used to submit stuff
    def entersubmit(event = None):

        app.submit()

    #Creates GUI from the Application class.
    print("GUI started.")
    root = Tk()
    root.title("Python Music Program")
    root.geometry("600x400")
    app = Application(root)
    #bind enter to submit, will later make it so that it knows where the cursor is and uses that to determine which button it should be
    root.bind('<Return>', entersubmit)
    
    #Run mainloop
    root.mainloop()

#some normal classes defined below

class Note(object):

    #This is used to create a note that will being strung together to form music
    def __init__(self, name, letter, octave, sharp):

        self.name = name
        self.letter = letter
        self.octave = octave
        self.sharp = sharp
        print("A new note has been created. " + str(self))

        self.name2 = self.name + "music21"
        self.notenamething = self.letter + self.octave
        self.name2 = music21.pitch.Pitch(self.notenamething)
        print("music21 test...." + str(self.name2.midi))
        
    def __str__(self):

        rep = str(self.letter)

        if self.sharp == "True":
            
            rep += "#" + str(self.octave)

        else:
            
            rep += str(self.octave)
            
        return rep
    
    def printstring(self):

        rep = "note: "
        rep += self.name + " " + self.letter + self.octave

        if self.sharp == "True":
            rep += " sharp"

        else:

            rep += " not sharp"

        return rep

    def changeoctave(self, numofoct):

        try:

            self.octave = int(self.octave) + int(numofoct)
            self.octave = str(self.octave)

        except:

            input("Error type 5 occured: Please Debug")

    def changenote(self, newnote):

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

    #This is used to makes a groups of notes to create a song (or maybe just a single "voice" of a fugue)
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

        self.songlist = []
        self.notedictionary = {}
        

        for i in range(int(self.length)):

            #Might want to work on making less random :P
            randomnote = random.choice(Note_list)
            randomoctave = random.choice(Octaves)
            randomsharp = random.randint(0,6)

            if randomsharp == 1:

                issharp = "#"
            
            else:

                issharp = ""

            self.notedictionary["note" + str(i)] = Note(str("note" + str(i)),str(randomnote),str(randomoctave), str(issharp))
            randomnoteandoctave = str(randomnote) + str(randomoctave) + str(issharp)
            self.songlist.append(str(randomnoteandoctave))
            
        print("Notes added to song. Check testmusic.txt file for results.")
        self.savesonglist("testmusic")

    def print_songlist(self):
            
            rep = "song: "
            rep += str(self.songlist)
            return rep

    def savesonglist(self, filename):

        text_file_name = os.path.join(savepath, str(filename) + ".txt")
        text_file = open(text_file_name, "w")
        text_file.write("song: " + str(self.songlist))
        text_file.close()
        print("Song written to " + filename + ".txt")
            
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

    def transpose(self, semitones):

        if self.notedictionary:

            #this needs to figure out sharps so E# is not considerred different from F
            print("Transpose function used on song " + self.name + ". Transposed " + str(semitones) + " semitones.")

            for note in self.notedictionary:
                
                #idk how this is going to work
                print("Note not transposed due to bad programming.")
                
        else:

            print("Transpose function used on song " + self.name + ". Transposed " + str(semitones) + " semitones.")            

    def changenotestolist(self, changelist):

        print("this should work")
    
class fugue(object):

    #Not even close to done
    def __init__(self, name, subjectsong, answers):

        print("A new fugue has been created.")
        self.name = name
        self.subjectsong = subjectsong
        self.answercount = 0

    def __str__(self):

        rep = "Fugue: "
        #might want to do a bit of work the string value of other objects to make this better
        rep += "Name- " + self.name + " " + "Subject- " + str(self.subjectsong)
        return rep

    def counterpoint(self):

        #idk what to do here so here is a print function that portrays my feelings :P
        print("Counterpoint is hard.")

    def createanswer(self, semitones):

        #this is horrendously bad but it works for the short term
        #I will change this so it works on for loops for each note in the song changing the corresponding notes in the answer
        #or I will change it so that the Song class has the ability to change its notes in one method call
        self.answer = Song("answer",self.subjectsong.speed, self.subjectsong.pitch, self.subjectsong.length)
        print(self.subjectsong.print_songlist())
        self.answer.add_notes()
        self.answer.notedictionary = self.subjectsong.notedictionary
        self.answer.songlist = self.subjectsong.songlist
        print(self.answer.print_songlist())
        self.answer.transpose(semitones)
        self.answercount += 1

    def createcountersubject(self):

        #self.subjectsong
        print("This program can't create a countersubject yet :(")
      
def playsong(songlistofsong, speed):

    for note in songlistofsong:

        music21note = music21.pitch.Pitch(note)
        playmodule.playmidinote(music21note.midi, speed)

def main():
    
    #main function where everything happens. I am testing with the fugue class that is being worked on and using pygame to play MIDIs.
    bach_test = input("Test bach_aof module (y/n)")
    
    if bach_test != "n":
        
        print("Tesitng.....\n")
        bach_aof.miditest()
        print("Test successful")
        time.sleep(1)
    
    fuguesong1 = Song("fuguesong1", 3, 4, 8)
    fuguesong1.add_notes()
    testfugue1 = fugue("testfugue1", fuguesong1, 1)
    testfugue1.createanswer(5)

    #playsong(fuguesong1.songlist, 1)
        
    #Run GUI
    GUI()

    input("Press enter to exit.")

#Run main
main()

#This is the end for now
