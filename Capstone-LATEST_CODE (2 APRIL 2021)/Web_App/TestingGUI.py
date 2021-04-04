from tkinter import *
from PIL import ImageTk, Image
import os


def whenClicked():
    "Here we call another function say runTests which handles the main testing"
    pass
def runTests():
    ""
def mainGUI():
    global root
    global e
    global e1
    root = Tk()
    root.title("Testing Environment")
    root.geometry("500x500")
    label1 = Label(root, text='').pack()
    label1 = Label(root, text='').pack()
    label = Label(root, text='Testing Environment ').pack()
    label1 = Label(root, text='').pack()

   



    TK_SILENCE_DEPRECATION = 1
    label1 = Label(root, text='').pack()
    submit_button = Button(root, text="Run Tests", command=whenClicked)
    submit_button.pack()

    root.mainloop()



mainGUI()