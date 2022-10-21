from tkinter import Entry, Label, Button, Text

from Objects.Window import SaveCredentialWindow


class IntroPage:
    def __init__(self):
        self.save_btn = None
        self.name_field = None
        self.save_credential_window = SaveCredentialWindow()
        self.about_lbl = Label(
            self.save_credential_window,
            text="Now we'll create a storage\n for our "
                 "credentials.\n Add your login/password\n and name of "
                 "credentials.",
            font=("Courier", 12))
        self.about_lbl.pack(side='top')
        self.go_btn = Button(master=self.save_credential_window,
                             text="Let's go",
                             command=self.go_to_save_credentials_page)
        self.go_btn.pack(side='top')

    def go_to_save_credentials_page(self):
        SaveCredentialsPage(self.save_credential_window,
                            self.about_lbl,
                            self.go_btn)


class SaveCredentialsPage:
    credentials_dict = {}

    def __init__(self, save_credential_window, about_lbl, go_btn):
        self.save_credential_window = save_credential_window
        self.error_message = None
        about_lbl.destroy()
        go_btn.destroy()
        self.name_lbl = Label(self.save_credential_window, text='Name')
        self.name_lbl.grid(column=0, row=0, padx=5, pady=5)
        self.login_lbl = Label(self.save_credential_window, text='Login')
        self.login_lbl.grid(column=1, row=0, padx=5, pady=5)
        self.password_lbl = Label(self.save_credential_window, text='Password')
        self.password_lbl.grid(column=2, row=0, padx=5, pady=5)
        self.name_field = Entry(self.save_credential_window)
        self.name_field.grid(column=0, row=1, padx=5, pady=5)
        self.login_field = Entry(self.save_credential_window)
        self.login_field.grid(column=1, row=1, padx=5, pady=5)
        self.password_field = Entry(self.save_credential_window)
        self.password_field.grid(column=2, row=1, padx=5, pady=5)
        self.save_btn = Button(master=self.save_credential_window,
                               text="Save",
                               command=self.save_gpal_button)
        self.save_btn.grid(column=1, row=2, pady=10)

    def save_gpal_button(self):
        credential_dict = {}

        credential_dict['name'] = self.name_field.get()
        credential_dict['login'] = self.login_field.get()
        credential_dict['password'] = self.password_field.get()
        if not all(credential_dict.values()):
            self.error_message = Label(self.save_credential_window,
                                       text='All fields must be filled',
                                       fg='red')
            self.error_message.grid(column=1, row=4, pady=10)
        if all(credential_dict.values()) and self.error_message:
            self.error_message.destroy()
        print(credential_dict)
