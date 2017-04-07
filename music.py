#This program should be able to write music. Quality is not assured. Now on Github :)
#I might try integrating this with Alda
#I am very sure this violates every rule of programming best practices

#import random module for some randomness in the music
import random
#import tkinter for GUI
from tkinter import *
#for writing some files to a specified folder
import os.path

#some variables that need to be defined
savepath = "C:/PythonMusic/textfiles/"

guisong = 0
#lists that will be used eventually
Note_list = ["A","B","C","D","E","F","G"]
Octaves = [1,2,3,4,5,6]


#Getting all the GUI related stuff out of the way for later
#I need to have it defined before I call it in main(), because no forward declaration in python :(

class Application(Frame):
    #Application class, where the GUI magic happens

    def __init__(self, master):

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
        self.musicbutton1.grid(row = 5, column = 0, columnspan = 1, sticky = E)
        self.musicbutton1.configure(text = "Test button")
        

        self.musicbutton2 = Button(self)
        self.musicbutton2.grid(row = 1, column = 4, sticky = W)
        self.musicbutton2.configure(text = "Submit")

        self.musicbutton3 = Button(self)
        self.musicbutton3.grid(row = 6, column = 0, columnspan = 1, sticky = E)
        self.musicbutton3.configure(text = "Usefull button.")
              
        #remember to change this value as needed

        self.musicbutton2.configure(command = self.submit)
        self.musicbutton1.configure(command = self.update)
        global guisong
        guisong = Song("guisong", "4", "3", "2")
        #self.musicbutton3.configure(command = self.puttextinbox(str(guisong), "False"))
        self.musicbutton3.configure(command = self.specialputinbox)
        
    def create_text(self):

        self.firstentry = Entry(self)
        self.firstentry.grid(row = 1, column = 2, columnspan = 2, sticky = W)


        self.display = Text(self, width = 20, height = 5, wrap = WORD)
        self.display.grid(row = 2, column = 0, columnspan = 5, sticky = S)
        #self.puttextinbox("kat", "False")

        
    def specialputinbox(self):

        #stupid, but it works :P
        #stupid and under construction
        #self.puttextinbox(str(guisong), "False")
        guisong.add_notes()
        self.puttextinbox(str(guisong.notedictionary), "False")
    
    def create_checks(self):
        
        self.bool1 = BooleanVar()
        self.bool2 = BooleanVar()
        self.bool3 = BooleanVar()
        
        self.check1 = Checkbutton(self)
        self.check1.configure(variable = self.bool1)
        self.check1.configure(command = self.submit)
        self.check1.grid(row = 3, column = 0, sticky = S)
        #might want to not use a variable to save space idk.

        
        
    def update(self):

        self.buttonclick += 1
        self.musicbutton1.configure(text = "Total Clicks: " + str(self.buttonclick))
        print(str(self.buttonclick))

    def submit(self):

        global guisong
        textboxstuff = self.firstentry.get()

        if textboxstuff:

            print("The Number of Notes is: " + textboxstuff)
            numberofnotes = textboxstuff
            guisong = Song("guisong", "5", "4", textboxstuff)
            print(guisong)

        else:

            print("No Number provided.")


    def puttextinbox(self, putinbox, append):

        if append == "False":

            self.display.delete(0.0, END)
            self.display.insert(0.0, putinbox)

        else:

            self.display.insert(0.0, putinbox) 


#going to use pack and pack-forget to make an ever changing ui
#I am going to rewrite the program to work with tkinter

#Creates GUI from the Application class
def GUI():

    root = Tk()
    root.title("Python Music Program")
    root.geometry("600x400")
    app = Application(root)

    
    #Run mainloop
    root.mainloop()



# some classes defined below

class Note(object):

#    This is used to create a note that will being strung together to form music

    def __init__(self, name, letter, octave, sharp):

        #will add ability to determine if part of song or something idk
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

#still need to connect note and song classes

class Song(object):

#    This is used to makes a groups of notes to create a song (or maybe just a single "voice" of a song)

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

        songlist = []
        self.notedictionary = {}

        for i in range(int(self.length)):

            #Might want to work on making less random :P
            randomnote = random.choice(Note_list)
            randomoctave = random.choice(Octaves)
            randomsharp = random.randint(0,6)

            if randomsharp == 1:

                issharp = " sharp "

            else:

                issharp = " not sharp "

            self.notedictionary["note" + str(i)] = Note(str("note" + str(i)),str(randomnote),str(randomoctave), str(issharp))

            randomnoteandoctave = str(randomnote) + str(randomoctave) + str(issharp)
            songlist.append(str(randomnoteandoctave))

        print("Notes added to song. Check text file for results.")
        self.songlist = songlist

        #write to file
        text_file_name = os.path.join(savepath, "testmusic.txt")
        text_file = open(text_file_name, "w")
        #text_file = open("testmusic.txt", "w")
        text_file.write("song: " + str(songlist))
        text_file.close()

    def print_songlist(self):

        print("song: " + str(self.songlist))
        write = input("Write music above to file? y or n ")

        if write == "y":

            filename = input("What should the text file be called? Do NOT include the .txt file extension")

            text_file_name = os.path.join(savepath, str(filename) + ".txt")
            text_file = open(text_file_name, "w")
            #text_file = open( str(filename) + ".txt", "w")
            #text_file.write("song: " + str(self.songlist))
            text_file.close()

            print("Song written to " + filename + ".txt")

        else:

            print("Song not written.")

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

#   Not even close to done
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
#    main function where everything happens

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
    song1.print_songlist()
    print(song1)
    song1.append_notes(3)
    print(song1)

    #testing with the fugue song that is being worked on
    fuguesong1 = Song("fuguesong1",3,4,8)
    testfugue1 = fugue("testfugue1", song1)
    print(testfugue1)

    #Run GUI
    print("GUI started.")
    GUI()
    
    input("Press enter to exit.")

#Run main
main()

#This is the end for now
