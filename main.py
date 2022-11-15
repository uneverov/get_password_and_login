
from Objects.Gpals import Gpals

from Objects.MenuButton import MenuBar
from Objects.Window import MainWindow, place_buttons

window = MainWindow()
window.config(bg='#141414')
gpals = Gpals()
menu_bar = MenuBar(window, gpals.gpals)
place_buttons(gpals=gpals.gpals, window=window)

window.mainloop()
