import tkinter as tk
from tkinter import*
from turtle import width
from playsound import playsound
import os
import random
import subprocess
import sys

currDir = os.getcwd()
file = open('poems.txt',encoding="utf-8")
content = file.readlines()
is_on = True
count = 0

# Functions

def newWindow():
    window.destroy()
    add_sentence = currDir+"/add_sentence.py"
    subprocess.run([sys.executable, add_sentence], check=True)

def rand_sentence():
    with open("poems.txt", 'r') as fp:
        c = len(fp.readlines())

    rand_numb = random.randrange(0,c,1)
    sentence = content[rand_numb].strip()
    txtPlace = Label(window, text=sentence, font='Verdana 12', height=3, width=100)
    txtPlace.place(relx=0.5, rely=0.25, anchor=CENTER)

def ordered_sentence():
    global count
    with open("poems.txt", 'r') as fp:
        c = len(fp.readlines())

    if(count<c):
        sentence = content[count].strip()
        txtPlace = Label(window, text=sentence, font='Verdana 12', height=3, width=100)
        txtPlace.place(relx=0.5, rely=0.25, anchor=CENTER)
        count = count + 1
    else:
        count = 0
        sentence = content[count].strip()
        txtPlace = Label(window, text=sentence, font='Verdana 12', height=3, width=100)
        txtPlace.place(relx=0.5, rely=0.25, anchor=CENTER)
        count = count + 1


def do(event=None):
    b1.config(relief=tk.SUNKEN)
    playsound('notes/nota-do.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b1.after(50,lambda:b1.config(relief=tk.RAISED))

def re(event=None):
    b2.config(relief=tk.SUNKEN)
    playsound('notes/nota-re.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b2.after(50,lambda:b2.config(relief=tk.RAISED))

def mi(event=None):
    b3.config(relief=tk.SUNKEN)
    playsound('notes/nota-mi.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b3.after(50,lambda:b3.config(relief=tk.RAISED))

def fa(event=None):
    b4.config(relief=tk.SUNKEN)
    playsound('notes/nota-fa.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b4.after(50,lambda:b4.config(relief=tk.RAISED))

def sol(event=None):
    b5.config(relief=tk.SUNKEN)
    playsound('notes/nota-sol.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b5.after(50,lambda:b5.config(relief=tk.RAISED))

def la(event=None):
    b6.config(relief=tk.SUNKEN)
    playsound('notes/nota-la.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b6.after(50,lambda:b6.config(relief=tk.RAISED))

def si(event=None):
    b7.config(relief=tk.SUNKEN)
    playsound('notes/nota-si.wav', False)
    if(is_on==True):
        ordered_sentence()
    else:
        rand_sentence()
    b7.after(50,lambda:b7.config(relief=tk.RAISED))

def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        toggle.config(text = "Randomly", fg = "grey")
        is_on = False
    else:
        on_button.config(image = on)
        toggle.config(text = "Ordered", fg = "green")
        is_on = True

# Views

window = tk.Tk()
window.title('Piano')
window.geometry('560x420')

# Toggle

toggle = Label(window, text ="Ordered" ,fg = "green",font = ("Helvetica", 12))
toggle.pack(pady = 5)

on = PhotoImage(file = "./images/on.png")
off = PhotoImage(file = "./images/off.png")

on_button = Button(window, image = on, bd = 0, command = switch)
on_button.pack(pady = 0)

addButton = Button(window, width=10, text="Add sentence", command=lambda: newWindow())
addButton.configure(bg="#7d7d7d", fg="#ffffff")
addButton.place(x=430, y=0)

b1 = tk.Button(window, text="Do\n(A)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=do)
b1.place(x=50, y=150)

b2 = tk.Button(window, text="Re\n(S)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=re)
b2.place(x=115, y=150)

bx = tk.Button(window, bg='black', borderwidth=3, height=10,width=2 )
bx.place(x=100, y=150)

b3 = tk.Button(window, text="Mi\n(D)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=mi)
b3.place(x=180, y=150)

bx2 = tk.Button(window, bg='black', borderwidth=3, height=10,width=2 )
bx2.place(x=165, y=150)

b4 = tk.Button(window, text="Fa\n(F)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=fa)
b4.place(x=245, y=150)

b5 = tk.Button(window, text="Sol\n(G)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=sol)
b5.place(x=310, y=150)

b6 = tk.Button(window, text="La\n(H)", font='Verdana 14 bold', bg='white', borderwidth=3,fg='black', height=10,width=4,command=la)
b6.place(x=375, y=150)

bx3 = tk.Button(window, bg='black', borderwidth=3, height=10,width=2 )
bx3.place(x=360, y=150)

b7 = tk.Button(window, text="Si\n(J)", font='Verdana 14 bold', bg='white', borderwidth=3, fg='black', height=10,width=4,command=si)
b7.place(x=440, y=150)

bx4 = tk.Button(window, bg='black', borderwidth=3, height=10,width=2 )
bx4.place(x=425, y=150)

window.bind('<a>',do)
window.bind('<s>',re)
window.bind('<d>',mi)
window.bind('<f>',fa)
window.bind('<g>',sol)
window.bind('<h>',la)
window.bind('<j>',si)

window.mainloop()