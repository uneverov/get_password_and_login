import json
from os import getcwd
from tkinter import Label, Entry
from tkinter.messagebox import askquestion
from tkinter import Button

from Objects.Window import SecondWindow


class Gpals:
    def __init__(self):
        self.name_field = None
        self.window2 = None
        self.btn = None
        self.lbl = None
        self.json_data = f'{getcwd()}/gpals.json'

    def get_data(self):
        try:
            json_source = open(self.json_data)
            print(json_source)
            file_content = json_source.read()
            gpals = json.loads(file_content)
        except FileNotFoundError:
            answer = askquestion('Error', 'File with credentials not found. '
                                          'Do you want to create file?')
            if answer == 'yes':
                self.window2 = SecondWindow()
                self.lbl = Label(self.window2,
                                 text="Now we'll create a storage\n for our "
                                      "credentials.\n Add your "
                                      "login/password\n and "
                                      "name of credentials.",
                                 font=("Courier", 12))
                self.lbl.pack(side='top')
                self.btn = Button(master=self.window2,
                                  bd=5,
                                  text="Let's go",
                                  command=self.clicked)
                self.btn.pack(side='top')

    def clicked(self):
        self.lbl.destroy()
        self.btn.destroy()
        self.name_field = Entry(self.window2)
        self.name_field.place(x='25', y='25')

