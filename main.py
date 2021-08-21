import time
from playsound import playsound
import random
from tkinter import *
from PyDictionary import PyDictionary
timer = 0.1*60
time.sleep(timer)
dictionary=PyDictionary()
file = open("dict.txt")
words = file.read().split("\n")
index = random.randint(0,3368)
word = words[index]
defs = meaning = dictionary.meaning(word)

playsound('song.mp3')
root = Tk()
root.title(Special Word of the Day)
root.geometry("600x100")
var = StringVar()
vari = StringVar()
label1= Label( root, textvariable=var, relief=RAISED,font = "Times 32")
label2 = Label(root , textvariable=vari, relief=RAISED,font ="Times 18")
var.set(word)
vari.set(meaning)
label1.pack()
label2.pack()




root.mainloop()
