import tkinter
from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(400,400)
#functions
def Calculate():
    weight =int(w_entry.get())
    height =int(h_entry.get()) / 100
    BMI = weight / (height*height)
    if BMI < 18.5:
        a_label.config(text=f"Your BMI is : {BMI} , You are Underweight")
    elif BMI > 18.5 and BMI < 24.9:
        a_label.config(text=f"Your BMI is : {BMI} , You are Normal weight")
    elif BMI > 25 and BMI < 29.9:
        a_label.config(text=f"Your BMI is : {BMI} , You are Over weight")
    elif BMI > 30 and BMI < 34.9:
        a_label.config(text=f"Your BMI is : {BMI} , You are Obesity (Class 1)")
    elif BMI > 35 and BMI < 39.9:
        a_label.config(text=f"Your BMI is : {BMI} , You are Obesity (Class 2)")
    elif BMI > 40:
        a_label.config(text=f"Your BMI is : {BMI} , You are Extreme Obesity")


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

button1=Button(text="Calculate" , command=Calculate)
button1.place(x=160,y=200)

#button

#answer_label

a_label=Label()
a_label.place(x=50,y=250)

#answer_label


window.mainloop()