from tkinter import *
import tkinter.messagebox
root=tkinter.Tk()
root.title("When you press button the message will pop up")
root.geometry("500x300")
def onClick():
    tkinter.messagebox.showinfo("Welcome TYBBA(CA) student","Hi I am Aditi")
button=Button(root,text="click-me",command=onClick,height=5,width=10)
button.pack(side="bottom")
root.mainloop()