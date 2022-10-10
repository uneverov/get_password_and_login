import json
import tkinter
from os import getcwd


def clicked_login():
    gl = login_btn.cget('textvariable')
    window.clipboard_clear()
    window.clipboard_append(str(gl))


def clicked_password():
    gp = password_btn.cget('textvariable')
    window.clipboard_clear()
    window.clipboard_append(str(gp))


json_data = f'{getcwd()}/gpal.json'

with open(json_data) as json_source:
    file_content = json_source.read()
    gpals = json.loads(file_content)

window = tkinter.Tk()
window.title("GPAL")
window.geometry('400x250')
buttons_names = []
window.bind()
for button_name in range(len(gpals.items())):
    buttons_names.append(f'btn_{button_name}')
for i, (label, gpal) in enumerate(gpals.items()):
    gl, gp = str(gpal).split(';gpal;')
    for btn in buttons_names:
        ll = tkinter.Label(window, text=label)
        ll.grid(column=0, row=i + 1)
        login_btn = tkinter.Button(window,
                                   text='login',
                                   textvariable=gl,
                                   command=clicked_login)
        login_btn.grid(column=1, row=i + 1)
        password_btn = tkinter.Button(window,
                                      text='password',
                                      textvariable=gp,
                                      command=clicked_password)
        password_btn.grid(column=2, row=i + 1)

window.attributes('-topmost', True)
window.mainloop()
