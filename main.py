import keyboard
from Objects.Button import onkeypress, place_buttons
from Objects.Gpals import Gpals
from Objects.MenuButton import MenuBar
from Objects.Windows import MainWindow

window = MainWindow()

gpals = Gpals()
menu_bar = MenuBar(window, gpals)
place_buttons(gpals=gpals.gpals, window=window)
keyboard.on_press(onkeypress)
window.mainloop()
