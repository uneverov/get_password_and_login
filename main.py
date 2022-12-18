import keyboard
from Objects.Button import place_buttons, onkeypress
from Objects.Gpals import Gpals
from Objects.MenuButton import MenuBar
from Objects.Windows import MainWindow


window = MainWindow()
gpals = Gpals()
menu_bar = MenuBar(window, gpals)
place_buttons(gpals=gpals.gpals, window=window, labels=True)
keyboard.on_press(onkeypress)
window.mainloop()
