import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')
def run():
    os.system('easy_facial_recognition.py --i known_faces')

text = Text(window)
text.insert(INSERT, "Press Q to quit the video.")
btn = Button(window, text="Start facial recognition", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)
text.grid(column=0, row=1)

window.mainloop()
