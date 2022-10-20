import json
from os import getcwd
from tkinter import Label
from tkinter.messagebox import askquestion
from tkinter import Button

from Objects.Window import SecondWindow


class Gpals:
    def __init__(self):
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
                window2 = SecondWindow()
                Label(window2,
                      text="Now we'll create a storage\n for our "
                           "credentials.\n Add your login/password\n and "
                           "name of credentials.",
                      font=("Courier", 12)).pack(side='top')
                Button(master=window2,
                       bd=5,
                       text="Let's go").pack(side='top')

        # return gpals
