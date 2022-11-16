from Objects.Button import place_buttons
from Objects.Gpals import Gpals
from Objects.MenuButton import MenuBar
from Objects.Windows import MainWindow

window = MainWindow()
gpals = Gpals()
menu_bar = MenuBar(window, gpals.gpals)
place_buttons(gpals=gpals.gpals, window=window)
window.mainloop()
