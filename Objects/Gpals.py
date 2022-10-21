import json
from os import getcwd
from tkinter import Button, Entry, Label
from tkinter.messagebox import askquestion

from Pages.SaveGpalsPages import IntroPage


class Gpals:
    def __init__(self):
        self.save_btn = None
        self.go_btn = None
        self.save_credential_lbl = None
        self.name_field = None
        self.save_credential_window = None
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
                intro_page = IntroPage()
