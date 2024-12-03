from tkinter import *
from random import shuffle
import time
gui=Tk(className="python window color")
gui.geometry("400x200")
colors=['red','yellow','blue','orange','pink','purple']
for i in range(0,len(colors)):
    gui.configure(background=colors[i])
    gui.update()
    time.sleep(1)
gui.mainloop()