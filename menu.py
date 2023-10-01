import tkinter
from tkinter import *
from main import *
from situp import *
from pushup import *
from PIL import Image,ImageTk



def start(root):
    root.title("Menu")
    root.geometry("750x300+0+0")

    btn1 = tkinter.Button(root,text="Bicep Curl",width=20,command=lambda : bcc(root))
    btn1.place(x=250,y=550)

    btn2 = tkinter.Button(root, text="Push Ups", width=20, command=lambda: pushup(root))
    btn2.place(x=730, y=550)

    btn3 = tkinter.Button(root, text="Sit Up", width=20, command=lambda: situp(root))
    btn3.place(x=1160, y=550)



def bcc(root):
    root.destroy()
    exercise()

def situp(root):
    root.destroy()
    situps()

def pushup(root):
    root.destroy()
    pushups()

def call():
    root=Tk()
    canvas = Canvas(root, width=2000, height=800)
    photo = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Downloads\\background.jpeg"))

    canvas.create_image(0,0, anchor=NW, image=photo)
    canvas.pack()
    start(root)
    root.mainloop()

call()
