import tkinter


class Button:
    def __init__(self, window, text, grid, textvariable=None, padx=None):
        self.window = window
        self.text = text
        self.textvariable = textvariable
        self.btn = tkinter.Button(window,
                                  text=text,
                                  textvariable=textvariable,
                                  command=self.clicked)
        self.btn.grid(column=grid[0], row=grid[1], padx=padx)

    def clicked(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(str(self.textvariable))
