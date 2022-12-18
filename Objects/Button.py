import random
import tkinter
from tkinter.messagebox import askquestion, showwarning

import keyboard
import settings
from Objects.Gpals import Gpals, write_json
from Objects.Label import Label

login_to_paste = []


def place_buttons(gpals, window, labels=False):
    if labels:
        login_lbl = tkinter.Label(text='press F2',
                                  background=settings.BLACK,
                                  foreground=settings.WHITE)
        login_lbl.grid(column=0, row=0, padx=0, pady=5)
        login_lbl_2 = tkinter.Label(text='to insert',
                                    background=settings.BLACK,
                                    foreground=settings.WHITE)
        login_lbl_2.grid(column=1, row=0, padx=0, pady=5)
        animate_label(login_lbl['text'], login_lbl)
    for i, (label, gpal) in enumerate(gpals.items()):
        gl, gp = str(gpal).split(';gpal;')
        print(gl, gp)
        Label(window=window,
              text=label,
              grid=(0, i + 1))
        Button(window=window,
               text='get',
               textvariable=gpal,
               grid=(1, i + 1))
        DeleteButton(window=window,
                     text='X',
                     label=label,
                     grid=(3, i + 1))


def animate_label(text, login_lbl):
    login_lbl.after(2000, animate_label, text, login_lbl)
    login_lbl['foreground'] = random.choice(
        [x for x in list(settings.COLORS.values()) if x not in
         [settings.VIOLET, settings.BLACK, settings.RED, settings.GREEN]])


class Button:
    def __init__(self, window, text, grid, textvariable=None, padx=None,
                 fg=settings.ORANGE, width=18):
        self.window = window
        self.text = text
        self.textvariable = textvariable
        self.btn = tkinter.Button(window,
                                  text=text,
                                  textvariable=textvariable,
                                  command=self.clicked,
                                  fg=fg,
                                  background=settings.BLACK,
                                  borderwidth=0, width=width)
        self.btn.grid(column=grid[0], row=grid[1], padx=padx)

    def clicked(self):
        login_to_paste.clear()
        login_to_paste.extend(str(self.textvariable).split(';gpal;'))
        print(login_to_paste)


def onkeypress(event):
    if event.name == 'f2':
        print(login_to_paste)
        try:
            keyboard.write(login_to_paste[0])
        except IndexError:
            pass
        try:
            del login_to_paste[0]
        except IndexError:
            pass


class DeleteButton:
    def __init__(self, window, text, label, grid):
        self.window = window
        self.gpals = Gpals()
        self.text = text
        self.label = label
        self.btn = tkinter.Button(window,
                                  text=text,
                                  command=self.delete,
                                  fg=settings.LILAC,
                                  background=settings.BLACK,
                                  borderwidth=0, width=3)
        self.btn.grid(column=grid[0], row=grid[1])

    def delete(self):
        if len(self.gpals.gpals) > 1:
            answer = askquestion('Delete gpal',
                                 'Do you really want to delete gpal?')
            if answer == 'yes':
                grid_objects = self.window.grid_slaves()
                for grid_object in grid_objects:
                    grid_object.destroy()
                del self.gpals.gpals[self.label]
                write_json(self.gpals.gpals)
                place_buttons(self.gpals.gpals, self.window, labels=True)
        else:
            showwarning("Noup", "You can't delete last gpal")
