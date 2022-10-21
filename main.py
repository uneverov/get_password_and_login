from Objects.Button import Button
from Objects.Gpals import Gpals
from Objects.Label import Label
from Objects.Window import MainWindow

window = MainWindow()
gpals = Gpals().get_data()

# for i, (label, gpal) in enumerate(gpals.items()):
#     gl, gp = str(gpal).split(';gpal;')
#     Label(window=window,
#           text=label,
#           grid=(0, i + 1))
#     Button(window=window,
#            text='login',
#            textvariable=gl,
#            grid=(1, i + 1))
#     Button(window=window,
#            text='password',
#            textvariable=gp,
#            grid=(2, i + 1))

window.mainloop()
