import tkinter


class Label:
    def __init__(self, window, text, grid):
        self.window = window
        self.text = text
        self.lbl = tkinter.Label(window, text=text)
        self.lbl.grid(column=grid[0], row=grid[1], padx=10)

