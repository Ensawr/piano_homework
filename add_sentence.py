import tkinter as tk
import tkinter.messagebox
from tkinter import*
import os
import subprocess
import sys
os.system('cls')

currDir = os.getcwd()
file = open('poems.txt', 'a')

def addSentence():
    text = txt.get(1.0,"end-1c")
    if(len(text)<1):
        tkinter.messagebox.showinfo("Error","Textbox boş olamaz!")
    else:
        file.write("\n")
        file.write(text)
        file.close()
        window.destroy()
        app = currDir+"/app.py"
        subprocess.run([sys.executable, app], check=True)


window = tk.Tk()
window.title('Add Sentence')
window.geometry('700x150')

txt = tk.Text(window, height = 1, width = 80)
txt.place(relx=0.5, rely=0.2, anchor=CENTER)

addButton = Button(window, width=10, text="Add sentence", command=lambda: addSentence())
addButton.configure(bg="#7d7d7d", fg="#ffffff")
addButton.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()