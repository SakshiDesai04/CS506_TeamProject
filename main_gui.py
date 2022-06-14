# Import Module
from tkinter import *
from tkinter.ttk import *
import sunglass as sg
import beard as br
import dog as dg
import addMask as am
import anh as an
import hat as ht
import cat as ct

def sunglass():
    sunglass = sg.DetectFace('haarcascade_frontalface_default.xml')
    sunglass.camera()

def tophat():
    tophat = br.DetectFace('haarcascade_frontalface_default.xml')
    tophat.camera()


def dog():
    dog = dg.DetectFace('haarcascade_frontalface_default.xml')
    dog.camera()

def cat():
    cat = ct.DetectFace('haarcascade_frontalface_default.xml')
    cat.camera()


def mask():
    mask = am.mask()
    mask.camera()

def sepia():
    sep = an.anh()
    sep.sep()

def cartoon():
    car = an.anh()
    car.cartoon()

def hat():
    hat = ht.mask()
    hat.camera()


# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to Filters for 506")
# Set geometry (widthxheight)
root.geometry('350x350')

lbl = Label(root, text = "Enjoy our various filters below")
lbl.pack()

style = Style()
 
style.configure('TButton', font = ('calibri', 20, 'bold'),   borderwidth = '4')
 
# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'green')],background = [('active', 'black')])

 
# button widget with red color text
# inside
btn1 = Button(root, text = "tophat", command=tophat)
# set Button grid
btn1.pack()

btn2 = Button(root, text = "sunglasses", command=sunglass)
# set Button grid
btn2.pack()

btn3 = Button(root, text = "Mask" , command=mask)
# set Button grid
btn3.pack()

btn4 = Button(root, text = "Dog" , command=dog)
# set Button grid
btn4.pack()

btn5 = Button(root, text = "Sepia", command=sepia)
# set Button grid
btn5.pack()

btn6 = Button(root, text = "Cartoon" , command=cartoon)
# set Button grid
btn6.pack()

btn7 = Button(root, text = "witch", command=hat)
# set Button grid
btn7.pack()

btn8 = Button(root, text = "Cat" , command=cat)
# set Button grid
btn8.pack()

# Define a function to close the window
def close():
   #win.destroy()
   root.quit()

# Create a Button to call close()
Button(root, text= "Close the Window", command=close).pack(pady=20)


# all widgets will be here
# Execute Tkinter
root.mainloop()