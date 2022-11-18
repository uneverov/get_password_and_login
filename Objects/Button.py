import tkinter
from tkinter.messagebox import askquestion, showwarning

from Objects.Cryptocode import decrypt

import settings
from Objects.Gpals import Gpals, write_json
from Objects.Label import Label


def place_buttons(gpals, window, lables=False):
    if lables:
        login_lbl = tkinter.Label(text='l o g i n',
                                  background=settings.BLACK,
                                  foreground=settings.WHITE)
        login_lbl.grid(column=1, row=0, padx=0, pady=5)
        password_lbl = tkinter.Label(text='p a s s w o r d',
                                     background=settings.BLACK,
                                     foreground=settings.WHITE)
        password_lbl.grid(column=2, row=0, padx=0, pady=5)

    for i, (label, gpal) in enumerate(gpals.items()):
        gl, gp = str(gpal).split(';gpal;')
        Label(window=window,
              text=label,
              grid=(0, i + 1))
        Button(window=window,
               text='get',
               textvariable=decrypt(gl, 'login'),
               grid=(1, i + 1))
        Button(window=window,
               text='get',
               textvariable=decrypt(gp, 'password'),
               grid=(2, i + 1))
        DeleteButton(window=window,
                     text='X',
                     label=label,
                     grid=(3, i + 1))


class Button:
    def __init__(self, window, text, grid, textvariable=None, padx=None,
                 fg=settings.ORANGE, width=9):
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
        self.window.clipboard_clear()
        self.window.clipboard_append(str(self.textvariable))


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
                place_buttons(self.gpals.gpals, self.window, lables=True)
        else:
            showwarning("Noup", "You can't delete last gpal")
