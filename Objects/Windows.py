import tkinter

import pystray
import settings
from Objects.Button import place_buttons
from Objects.Gpals import write_json
from PIL import Image
from pystray import MenuItem as item

image=Image.open("favicon.png")

def add_message(entry_chat, txt):
    message = entry_chat.widget.get()
    entry_chat.widget.delete(0, tkinter.END)
    txt.configure(state="normal")
    txt.insert(tkinter.END, '> ' + message + '\n')
    txt.see(tkinter.END)
    txt.configure(state="disable")

class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPAL")
        self.screenwidth = self.winfo_screenwidth()
        self.screenwidth = self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d' % (
            240, 300, self.screenwidth//4,
            self.screenwidth - 700))
        self.bind()
        self.config(bg=settings.COLORS['BLACK'])
        #self.resizable(False, True)
        self.attributes('-topmost', True)
        self.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.chat_frame = tkinter.Frame(background=settings.COLORS['BLACK'], height=120, width=240)
        self.chat_frame.grid(columnspan=4, row=0)
        self.entry_chat = tkinter.Entry(self.chat_frame, foreground='green', font=('Hack-Bold', 10), insertbackground='green', insertwidth=2, background=settings.COLORS['BLACK'], borderwidth=0)
        self.entry_chat.focus_set()
        self.entry_chat.place(x=5, y=95)
        scrollbar = tkinter.Scrollbar(self.chat_frame)
        scrollbar.place(x=223, relheight=0.97)
        txt = tkinter.Text(self.chat_frame, height=5, width=27,
                           background=settings.COLORS['BLACK'],
                           font=('Hack-Bold', 10), borderwidth=0,
                           foreground='green', state='disabled', yscrollcommand=scrollbar.set)
        txt.place(x=0, y=0)
        scrollbar.config(command=txt.yview)
        self.entry_chat.bind("<Return>", lambda event: add_message(event, txt))

    def quit_window(self, icon, item):
       icon.stop()
       self.destroy()

    def show_window(self, icon, item):
       icon.stop()
       self.after(0,self.deiconify())

    def hide_window(self):
       self.withdraw()
       menu=(item('Quit', self.quit_window), item('Show', self.show_window, default=True))
       icon=pystray.Icon("name", image, "GPAL", menu)
       icon.run()

class SaveCredentialWindow(tkinter.Tk):
    def __init__(self, gpals, window):
        super().__init__()
        self.messages = {'too_long_name': tkinter.Label(),
                         'not_all_fields_filled': tkinter.Label(),
                         'not_unique_name': tkinter.Label(),
                         'succes_message': tkinter.Label()}
        self.config(bg=settings.COLORS['BLACK'])
        self.main_window = window
        self.credential_dicts = []
        self.gpals = gpals
        self.title("Add new gpals")
        self.geometry('400x200')

        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.name_lbl = tkinter.Label(self, text='Name',
                                      background=settings.COLORS['BLACK'],
                                      foreground=settings.COLORS['WHITE'])
        self.name_lbl.grid(column=0, row=1, padx=5, pady=5)
        self.login_lbl = tkinter.Label(self, text='Login',
                                       background=settings.COLORS['BLACK'],
                                       foreground=settings.COLORS['WHITE'])
        self.login_lbl.grid(column=1, row=1, padx=5, pady=5)
        self.password_lbl = tkinter.Label(self, text='Password',
                                          background=settings.COLORS['BLACK'],
                                          foreground=settings.COLORS['WHITE'])
        self.password_lbl.grid(column=2, row=1, padx=5, pady=5)
        self.name_field = tkinter.Entry(self)
        self.name_field.grid(column=0, row=1, padx=4, pady=5)
        self.login_field = tkinter.Entry(self)
        self.login_field.grid(column=1, row=1, padx=4, pady=5)
        self.password_field = tkinter.Entry(self)
        self.password_field.grid(column=2, row=1, padx=4, pady=5)
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
        names = [gpal['name'] for gpal in self.credential_dicts]
        self.delete_messages()
        if len(credential_dict['name']) > 10:
            self.messages['too_long_name'] = tkinter.Label(self,
                                                           text='Your gpal name\n cannot exceed\n 10 characters',
                                                           fg=settings.COLORS['RED'],
                                                           background=settings.COLORS['BLACK'])
            self.messages['too_long_name'].grid(column=1, row=4,
                                                pady=10)
        if not all(credential_dict.values()):
            self.messages['not_all_fields_filled'] = tkinter.Label(self,
                                                                   text='All fields must be filled',
                                                                   fg=settings.COLORS['RED'],
                                                                   background=settings.COLORS['BLACK'])
            self.messages['not_all_fields_filled'].grid(column=1, row=4,
                                                        pady=10)
        if (credential_dict['name'] in names
                or credential_dict['name'] in self.gpals):
            self.messages['not_unique_name'] = tkinter.Label(
                self,
                text=f'Gpal with name\n {credential_dict["name"]}\n already exist',
                fg=settings.COLORS['RED'],
                background=settings.COLORS['BLACK'])
            self.messages['not_unique_name'].grid(column=1,
                                                  row=4,
                                                  pady=10)
        if (all(credential_dict.values()) and credential_dict[
            'name'] not in names
                and credential_dict['name'] not in self.gpals and len(
                    credential_dict['name']) <= 10):
            self.messages['succes_message'] = tkinter.Label(self,
                                                            text=f'You saved {len(self.credential_dicts) + 1} gpals',
                                                            fg='green',
                                                            background=settings.COLORS['BLACK'])
            self.messages['succes_message'].grid(column=1, row=4, pady=10)
            if credential_dict['name'] not in names:
                self.credential_dicts.append(credential_dict)

    def create_gpals_button(self):
        for i in self.credential_dicts:
            self.gpals.update(
                {i['name']: ';gpal;'.join([(i['login']), (i['password'])])})
        write_json(self.gpals)
        place_buttons(self.gpals, self.main_window)
        self.destroy()

    def delete_messages(self):
        for message in self.messages.values():
            if message:
                message.destroy()
