from tkinter import *
import time

root = Tk()
root.title("Clock by Sandesh")
root.geometry("359x150+0+0")
root.configure(background="black")


def start():
    text = time.strftime("%H:%M:%S ")
    label.config(text = text)
    label.after(200,start)
label = Label(root,font=("ds-digital",50,'bold'),bg="black",fg="blue",bd=50)
label.grid(row=0,column=1)
start()
root.mainloop()
