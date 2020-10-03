# use Tkinter to show a digital clock
# using python code base

import time
#because we need digital clock , so we are importing the time library.
from tkinter import *

root = Tk()

root.title("Digital Clock")
root.geometry("250x100+0+0")
root.resizable(0,0)

label = Label(root, font=("Arial", 30, 'bold'), bg="black", fg="white", bd =30)
label.grid(row =0, column=1)



#function to declare the tkniter clock
def dig_clock():
    
    text_input = time.strftime("%H : %M : %S") # get the current local time from the PC
    
    label.config(text=text_input)
    
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    
    label.after(200, dig_clock)

    
    
# calling the function
dig_clock()

root.mainloop()