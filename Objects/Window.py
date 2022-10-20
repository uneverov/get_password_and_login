import tkinter


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPAL")
        self.geometry('400x250')
        self.bind()
        self.attributes('-topmost', True)


class SecondWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add new credentials")
        self.geometry('400x400')
        self.bind()
        self.attributes('-topmost', True)
