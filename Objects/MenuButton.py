from tkinter import Menu

from Objects.Window import SaveCredentialWindow


class MenuBar:
    def __init__(self, window, gpals):
        self.gpals = gpals
        self.window = window
        self.mainmenu = Menu(window)
        self.window.config(menu=self.mainmenu)
        filemenu = Menu(self.mainmenu, tearoff=0)
        filemenu.add_command(label="Add gpal", command=self.add)
        filemenu.add_command(label="Delete gpal")
        filemenu.add_command(label="Exit",
                             command=self.exit)
        self.mainmenu.add_cascade(label="---",
                                  menu=filemenu)

    def add(self):
        add_gpal_window = SaveCredentialWindow(self.gpals, self.window)

    def delete(self):
        self.window.destroy()

    def exit(self):
        self.window.destroy()
