from PNZGUParser import PNZGUParser
from tkinter import *


def main():
    parser = PNZGUParser(login_input.get(), password_input.get())
    parser.start()


window = Tk()
window.title("PNZGU Parser")
window.geometry('300x250')

login_label = Label(window, text="Login")
login_label.grid(column=6, row=15)

login_input = Entry(window, width=10)
login_input.grid(column=7, row=15)

password_label = Label(window, text='Password')
password_label.grid(column=6, row=16)

password_input = Entry(window, width=10)
password_input.grid(column=7, row=16)

main_button = Button(window, text="Auth and start", command=main)
main_button.grid(column=2, row=10)

window.mainloop()
