import tkinter
import random

import settings


class Label:
    def __init__(self, window, text, grid):
        self.window = window
        self.text = text
        self.lbl = tkinter.Label(window,
                                 text=text,
                                 background=settings.COLORS['BLACK'],
                                 foreground=settings.COLORS['WHITE'],
                                 width=9)
        self.lbl.grid(column=grid[0], row=grid[1], padx=(6, 0))
        self.lbl.bind('<Enter>', self.on_enter)
        self.lbl.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.lbl['background'] = random.choice(
        [x for x in list(settings.COLORS.values()) if x not in
         [settings.COLORS['VIOLET'], settings.COLORS['BLACK'],
          settings.COLORS['RED'], settings.COLORS['GREEN']]])
        self.lbl['foreground'] = settings.COLORS['BLACK']

    def on_leave(self, event):
        self.lbl['background'] = settings.COLORS['BLACK']
        self.lbl['foreground'] = settings.COLORS['WHITE']

# class AnimateLabel:
#     def __init__(self, window, text, x, y):
#         self.txt = text
#         self.lbl = tkinter.Label(window, font='Bell 12 bold', width=len(self.txt))
#         self.lbl.place(x=x, y=y)
#         window.after(1000, self.animate_label, self.txt)
#
#     def animate_label(self, text, n=0):
#         if n < len(text) - 1:
#             self.lbl.after(500, self.animate_label, text, n+1)
#         self.lbl['text'] = text[:n+1]
