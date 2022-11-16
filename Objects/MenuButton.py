from tkinter import Menu
from Objects.Windows import SaveCredentialWindow


class MenuBar:
    def __init__(self, window, gpals):
        self.gpals = gpals
        self.window = window
        self.mainmenu = Menu(window)
        self.window.config(menu=self.mainmenu)
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Add gpal", command=self.add)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",
                                  command=self.exit)
        self.mainmenu.add_cascade(label="Menu",
                                  menu=self.filemenu)

    def add(self):
        SaveCredentialWindow(self.gpals, self.window)

    def exit(self):
        self.window.destroy()
