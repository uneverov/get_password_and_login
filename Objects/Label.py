import tkinter
import random

import settings


class Label:
    def __init__(self, window, text, grid):
        self.window = window
        self.text = text
        self.lbl = tkinter.Label(window,
                                 text=text,
                                 background=settings.BLACK,
                                 foreground=settings.WHITE,
                                 width=9)
        self.lbl.grid(column=grid[0], row=grid[1], padx=(6, 0))
        self.lbl.bind('<Enter>', self.on_enter)
        self.lbl.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.lbl['background'] = random.choice(settings.COLORS)
        self.lbl['foreground'] = settings.BLACK

    def on_leave(self, event):
        self.lbl['background'] = settings.BLACK
        self.lbl['foreground'] = settings.WHITE
