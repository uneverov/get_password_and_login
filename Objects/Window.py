import tkinter


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPAL")
        self.geometry('400x250')
        self.bind()
        self.attributes('-topmost', True)
