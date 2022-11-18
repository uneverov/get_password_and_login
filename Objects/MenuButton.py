
from tkinter import Menu

from Objects.Gpals import get_info_from_json
from Objects.Windows import SaveCredentialWindow


class MenuBar:
    def __init__(self, window, gpals):
        self.gpals_content = None
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
        self.gpals_content = get_info_from_json(self.gpals.json_data)
        SaveCredentialWindow(self.gpals_content, self.window)

    def exit(self):
        self.window.destroy()
