import threading
import tkinter

import pystray
import requests
import settings
from Objects.Button import place_buttons
from Objects.Gpals import write_json
from PIL import Image
from pystray import MenuItem as item
from requests.exceptions import ConnectionError

from db import get_logins, add_login_password
from server import host_name, server_port

image=Image.open("favicon.png")

CHAT_CONTENT = '' # all messages from server
LOGIN = None
is_update_chat = None # do we need to update text.widget
connection = None

def get_chat_content():
    while True:
        global CHAT_CONTENT, connection, is_update_chat
        try:
            connection = requests.get(f'http://{host_name}:{server_port}/')
        except ConnectionError:
            tkinter.messagebox.showwarning("ConnectionError",
                                           "Server is unavailable")
        if connection and len(connection.content.decode()) > len(CHAT_CONTENT):
            CHAT_CONTENT = connection.content.decode()
            is_update_chat = True


get_chat_content = threading.Thread(target=get_chat_content)
get_chat_content.start()

class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.password = None
        self.login = None
        self.txt = None
        self.scrollbar = None
        self.entry_chat = None
        self.title("GPAL")
        self.screenwidth = self.winfo_screenwidth()
        self.screenwidth = self.winfo_screenheight()
        self.geometry('%dx%d+%d+%d' % (
            240, 300, self.screenwidth//4,
            self.screenwidth - 700))
        self.bind()
        self.config(bg=settings.COLORS['BLACK'])
        self.resizable(False, True)
        self.attributes('-topmost', True)
        self.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.chat_frame = tkinter.Frame(background=settings.COLORS['BLACK'],
                                        height=120, width=240)
        self.chat_widget()
        self.update_chat()

    def update_chat(self):
        #global LOGIN
        #LOGIN = self.login
        global is_update_chat
        self.after(5000, self.update_chat)
        if self.login and self.password and is_update_chat:
            self.txt.configure(foreground='green')
            self.txt.configure(state="normal")
            self.txt.delete('1.0', tkinter.END)
            self.txt.insert(tkinter.END, f'{CHAT_CONTENT}')
            self.txt.configure(state="disable")
            self.txt.see(tkinter.END)
            is_update_chat = False

    def chat_widget(self):
        self.chat_frame = tkinter.Frame(background=settings.COLORS['BLACK'],
                                        height=120, width=240)
        self.chat_frame.grid(columnspan=4, row=0)
        self.entry_chat = tkinter.Entry(self.chat_frame, foreground='green',
                                        font=('Hack-Bold', 10),
                                        insertbackground='green',
                                        insertwidth=2,
                                        background=settings.COLORS['BLACK'],
                                        borderwidth=0)
        self.entry_chat.focus_set()
        self.entry_chat.place(x=5, y=95)
        self.scrollbar = tkinter.Scrollbar(self.chat_frame)
        self.scrollbar.place(x=223, relheight=0.97)
        self.txt = tkinter.Text(self.chat_frame, height=5, width=27,
                           background=settings.COLORS['BLACK'],
                           font=('Hack-Bold', 10), borderwidth=0,
                           foreground='green', state='disabled',
                           yscrollcommand=self.scrollbar.set)
        self.txt.place(x=0, y=0)
        self.txt.see(tkinter.END)
        self.scrollbar.config(command=self.txt.yview)
        self.entry_chat.bind("<Return>", lambda event: self.add_message())

    def add_message(self, message=None):
        if not message:
            message = self.entry_chat.get()
        if message.startswith('login: '):
            self.txt.configure(state="normal")
            self.login = message.replace('login: ', '')
            print(get_logins())
            if self.login and self.login not in get_logins():
                self.entry_chat.delete(0, tkinter.END)
                self.txt.tag_config("red", foreground="red")
                self.txt.tag_add("red", f"{self.txt.index('end')}", "end")
                self.txt.insert(tkinter.END,
                                '> ' + 'Please set your password' +
                                '\n' + 'send password: your_password\n')
                self.txt.configure(state="disable")
                self.txt.see(tkinter.END)
            if self.login and self.login in get_logins():
                self.entry_chat.delete(0, tkinter.END)
                self.txt.tag_config("red", foreground="red")
                self.txt.tag_add("red", f"{self.txt.index('end')}", "end")
                self.txt.insert(tkinter.END,
                                '> ' + 'send password: your_password\n')
                self.txt.configure(state="disable")
                self.txt.see(tkinter.END)
        if message.startswith('password: ') and self.login not in get_logins():
            self.txt.configure(state="normal")
            self.password = message.replace('password: ', '')
            add_login_password(self.login, self.password)
        if message.startswith('password: ') and self.login not in get_logins():
            self.txt.configure(state="normal")
            self.password = message.replace('password: ', '')
        if not self.login and not self.password:
            self.txt.configure(foreground='red')
            self.txt.configure(state="normal")
            self.entry_chat.delete(0, tkinter.END)
            self.txt.tag_config("red", foreground="red")
            self.txt.insert(tkinter.END, '> ' + 'You should login first' + '\n' + 'send login: your_login\n')
            self.txt.configure(state="disable")
            self.txt.see(tkinter.END)
        if self.login and not self.password:
            self.txt.configure(foreground='red')
            self.txt.configure(state="normal")
            self.entry_chat.delete(0, tkinter.END)
            self.txt.tag_config("red", foreground="red")
            self.txt.insert(tkinter.END,
                            '> ' + 'Please set your password' +
                            '\n' + 'send password: your_password\n')
            self.txt.configure(state="disable")
            self.txt.see(tkinter.END)
        if self.login and self.password:
            if not message.startswith('login: '):
                self.txt.configure(state="normal")
                self.txt.tag_config("green", foreground="green")
                self.txt.tag_add("green", f"{self.txt.index('end-2c')}", "end")
                params = {'login': {self.login}, 'message': message}
                requests.post(f'http://{host_name}:{server_port}/',
                              params=params)
                self.entry_chat.delete(0, tkinter.END)
                self.txt.configure(state="normal")
                self.txt.insert(tkinter.END, f'> {self.login}: ' + message + '\n')
                self.txt.configure(state="disable")
                self.txt.see(tkinter.END)


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
