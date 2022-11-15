import json
import tkinter

from Objects.Button import Button
from Objects.Label import Label


def place_buttons(gpals, window):
    for i, (label, gpal) in enumerate(gpals.items()):
        gl, gp = str(gpal).split(';gpal;')
        Label(window=window,
              text=label,
              grid=(0, i + 1))
        Button(window=window,
               text='get',
               textvariable=gl,
               grid=(1, i + 1))
        Button(window=window,
               text='get',
               textvariable=gp,
               grid=(2, i + 1))


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPALS")
        self.geometry('400x250')
        self.bind()
        self.attributes('-topmost', True)
        self.login_lbl = tkinter.Label(self, text='login',
                                       background='#141414', foreground='#fff')
        self.login_lbl.grid(column=1, row=0, padx=5, pady=5)
        self.password_lbl = tkinter.Label(self, text='password',
                                          background='#141414',
                                          foreground='#fff')
        self.password_lbl.grid(column=2, row=0, padx=5, pady=5)


class SaveCredentialWindow(tkinter.Tk):
    def __init__(self, gpals, window):
        super().__init__()
        self.main_window = window
        self.credential_dicts = []
        self.gpals = gpals
        self.succes_message = None
        self.save_error_message = None
        self.title("Add new credentials")
        self.geometry('400x200')
        self.bind()
        self.attributes('-topmost', True)
        self.name_lbl = tkinter.Label(self, text='Name')
        self.name_lbl.grid(column=0, row=0, padx=5, pady=5)
        self.login_lbl = tkinter.Label(self, text='Login')
        self.login_lbl.grid(column=1, row=0, padx=5, pady=5)
        self.password_lbl = tkinter.Label(self, text='Password')
        self.password_lbl.grid(column=2, row=0, padx=5, pady=5)
        self.name_field = tkinter.Entry(self)
        self.name_field.grid(column=0, row=1, padx=5, pady=5)
        self.login_field = tkinter.Entry(self)
        self.login_field.grid(column=1, row=1, padx=5, pady=5)
        self.password_field = tkinter.Entry(self)
        self.password_field.grid(column=2, row=1, padx=5, pady=5)
        self.save_btn = tkinter.Button(master=self,
                                       text="Save",
                                       command=self.save_gpal_button)
        self.save_btn.grid(column=0, row=2, pady=10)
        self.create_file_btn = tkinter.Button(master=self,
                                              text="Exit",
                                              command=self.create_gpals_button)
        self.create_file_btn.grid(column=2, row=2, pady=10)

    def save_gpal_button(self):
        credential_dict = {'name': self.name_field.get(),
                           'login': self.login_field.get(),
                           'password': self.password_field.get()}
        if self.save_error_message:
            self.save_error_message.destroy()
        if self.succes_message:
            self.succes_message.destroy()
        if not all(credential_dict.values()):
            self.save_error_message = tkinter.Label(self,
                                                    text='All fields must be filled',
                                                    fg='red')
            self.save_error_message.grid(column=1, row=4, pady=10)
        if all(credential_dict.values()):
            self.succes_message = tkinter.Label(self,
                                                text='Saved',
                                                fg='green')
            self.succes_message.grid(column=1, row=4, pady=10)
            names = [gpal['name'] for gpal in self.credential_dicts]
            if credential_dict['name'] not in names:
                self.credential_dicts.append(credential_dict)

    def create_gpals_button(self):
        for i in self.credential_dicts:
            self.gpals.update(
                {i['name']: ';gpal;'.join([i['login'], i['password']])})
        json_object = json.dumps(self.gpals)
        with open("gpals.json", "w") as outfile:
            outfile.write(json_object)
        place_buttons(self.gpals, self.main_window)
        self.destroy()
