import tkinter
from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(400,400)

#functions


#functions

#weight_label

w_label=Label(text="Enter Your Weight (kg)")
w_label.place(x=130,y=50)

#weight_label

#height_entry

w_entry=Entry()
w_entry.place(x=132,y=80)

#height_entry

#height_label

h_label=Label(text="Enter Your Height (cm)")
h_label.place(x=130,y=130)

#height_label

#height_entry

h_entry=Entry()
h_entry.place(x=132,y=160)

#height_entry

#button

button1=Button(text="Calculate")
button1.place(x=160,y=200)

#button

window.mainloop()