import tkinter as tk
#for file and folder dialogs/management
from tkinter.filedialog import askdirectory, askopenfilename
import os.path
import time
import sys

#some variables that need to be defined
defaultsavepath = "C:/"
globalsavepath = defaultsavepath

##### Application Class #####
class Application(tk.Frame):
    
    def __init__(self, parent, UI_Elements, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.UI_Elements = UI_Elements
        self.parent = parent
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):

        self.labels, self.text, self.checks, self.buttons, self.bools, self.checks, self.menus, self.menuvars = ({},)*8
        self.create_menus()
        self.create_text()
        self.create_labels()
        self.create_buttons()
        self.create_checks()
        
    def create_labels(self):

        for i in self.UI_Elements[0]:

            temp = tk.Label(self, text = i[1])
            temp.grid(row = i[2], column = i[3], columnspan = i[4], sticky = i[5])
            self.labels[i[0]] = temp

    def create_buttons(self):

        for i in self.UI_Elements[1]:

            temp = tk.Button(self)
            temp.grid(row = i[2], column = i[3], columnspan = i[4], sticky = i[5])
            temp.configure(text = i[1])
            temp.configure(command = lambda: i[6](self))
            self.labels[i[0]] = temp
        
    def create_text(self):

        for i in self.UI_Elements[2]:

            if i[1].lower() == "entry":
                
                temp = tk.Entry(self)
                temp.grid(row = i[2], column = i[3], columnspan = i[4], sticky = i[5])
                self.text[i[0]] = temp

                if len(i) >= 7:

                    self.text[i[0]].insert(0, i[6])

            elif i[1].lower() == "text":

                temp = tk.Text(self, width = i[2], height = i[3], wrap = i[4])
                temp.grid(row = i[5], column = i[6], columnspan = i[7], sticky = i[8])
                self.text[i[0]] = temp

                if len(i) >= 10:

                    self.puttextinbox(i[9], i[10])

    def create_checks(self):

        for i in self.UI_Elements[3]:

            self.bools[i[0]] = tk.BooleanVar()
            self.checks[i[0]] = tk.Checkbutton(self)
            self.checks[i[0]].configure(variable = self.bools[i[0]], command = lambda: i[5](self))
            self.checks[i[0]].grid(row = i[2], column = i[3], sticky = i[4])
            
    def create_menus(self):

        for i in self.UI_Elements[4]:

            self.menuvars[i[0]] = tk.StringVar()
            self.menuvars[i[0]].set(i[6])
            self.menus[i[0]] = tk.OptionMenu(self, self.menuvars[i[0]], *i[2])
            self.menus[i[0]].grid(row = i[3], column = i[4], sticky = i[5])

    def puttextinbox(self, putinbox, append = True):

        if not append:

            self.text["display"].delete(0.0, tk.END)

        self.text["display"].insert(0.0, putinbox)

def GUI(UI_Elements):
  
    #Creates GUI from the Application class.
    print("GUI started.")
    root = tk.Tk()
    root.title("Python Music Program")
    root.geometry("600x400")
    #bind enter to submit
    root.bind('<Return>', lambda event: app.doeverything())
    #global app; app = Application(root, UI_Elements)
    global app; app = Music_Application(root, UI_Elements)
    #Run mainloop
    root.mainloop()

class Music_Application(Application):

    def __init__(self, parent, UI_Elements, *args, **kwargs):

        self.guisonglist = []
        Application.__init__(self, parent, UI_Elements, *args, **kwargs)

    def submit(self):

        textboxstuff = self.text["firstentry"].get()
        menustuff = self.menuvars["musicmenu"].get()
        speed = self.text["guisongspeed"].get()

        if textboxstuff and speed:

            self.guisonglist.append(Song("guisong" + str(len(self.guisonglist)), speed, menustuff, textboxstuff))
            self.guisonglist[-1].add_notes()
            self.puttextinbox( "length: " + textboxstuff + "\n" + str(self.guisonglist[-1]), False)
            
        else:

            print("No Numbers provided.")
            self.puttextinbox("No Numbers provided.", False)

    def puttextinbox(self, putinbox, append = True):

        if not append:

            self.text["display"].delete(0.0, tk.END)

        self.text["display"].insert(0.0, putinbox)

    def savetofile1(self):

        savepath = askdirectory()
        filename = self.text["savetofile"].get()
        self.guisonglist[-1].savesonglist(filename, savepath)

    def playguisong(self):
   
        playmodule.playsong(self.guisonglist[-1])

    def doeverything(self):

        self.submit()
        self.savetofile1()
        self.playguisong()    

if __name__ == "__main__":

    ### Labels ###
    musiclabel1 = ["musiclabel1", "This is a simple music program. Please Enjoy.", 0, 0, 6, tk.W]
    musiclabel2 = ["musiclabel2", "Number of notes for the song: ", 1, 0, 2, tk.W]
    musiclabel3 = ["musiclabel3", "Save location:", 6, 0, 2, tk.W]
    musiclabel4 = ["musiclabel4", ".txt", 6, 2, 1, tk.W]
    labels = [musiclabel1, musiclabel2, musiclabel3, musiclabel4]
    ### Buttons ###
    musicbutton1 = ["musicbutton1", "Save to file.", 7, 0, 1, tk.W, lambda app: app.savetofile1()]
    musicbutton2 = ["musicbutton2", "Submit", 1, 6, 1, tk.W, lambda app: Music_Application.submit()]
    musicbutton3 = ["musicbutton3", "Play song.", 7, 1, 1, tk.W, lambda app: app.playguisong()]
    musicbutton4 = ["musicbutton4", "Do everything.", 7, 2, 1, tk.W, lambda app: app.doeverything()]
    buttons = [musicbutton1, musicbutton2, musicbutton3, musicbutton4]
    ### Checks ###
    musiccheck = ["musiccheck", "meh", 15, 15, tk.W, lambda app: app.submit()]
    checks = [musiccheck]
    ### Text ###
    firstentry = ["firstentry", "Entry", 1, 2, 2, tk.W]
    savetofile = ["savetofile", "Entry", 6, 1, 1, tk.W]
    guisongspeed = ["guisongspeed", "Entry", 1, 5, 1, tk.W, "60"]
    display = ["display", "Text", 75, 15, tk.WORD, 2, 0, 7, tk.W, "This is where results will go. The console is more verbose for debugging.", False]
    text = [firstentry, savetofile, guisongspeed, display]
    ### Menu ### -- almost works
    musicmenu = ["musicmenu", "", ["Soprano", "Mezzo-Soprano", "Alto", "Tenor", "Baritone", "Bass"], 1, 4, tk.W, "Alto"]
    menus = [musicmenu]
    ############################################
    UI_Elements = [labels, buttons, text, checks, menus]
    GUI(UI_Elements)

def GUI():

    def entersubmit(event = None):
    
        app.doeverything()
        
    #Creates GUI from the Application class.
    print("GUI started.")
    root = tk.Tk()
    root.title("Python Music Program")
    root.geometry("600x400")
    app = Application(root)
    #bind enter to submit
    root.bind('<Return>', entersubmit)
    
    #Run mainloop
    root.mainloop()
