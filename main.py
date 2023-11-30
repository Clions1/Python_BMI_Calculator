import tkinter as tk
from tkinter import messagebox

def Calculate():
    try:
        weight = int(w_entry.get())
        height = int(h_entry.get()) / 100
        BMI = weight / (height * height)
        if BMI < 18.5:
            a_label.config(text=f"Your BMI is : {BMI} , You are Underweight")
        elif 18.5 <= BMI < 24.9:
            a_label.config(text=f"Your BMI is : {BMI} , You are Normal weight")
        elif 25 <= BMI < 29.9:
            a_label.config(text=f"Your BMI is : {BMI} , You are Over weight")
        elif 30 <= BMI < 34.9:
            a_label.config(text=f"Your BMI is : {BMI} , You are Obesity (Class 1)")
        elif 35 <= BMI < 39.9:
            a_label.config(text=f"Your BMI is : {BMI} , You are Obesity (Class 2)")
        elif BMI >= 40:
            a_label.config(text=f"Your BMI is : {BMI} , You are Extreme Obesity")
    except ValueError:
        messagebox.showerror("Error", "Please Enter Correct Value")

window = tk.Tk()
window.title("BMI Calculator")
window.minsize(400, 400)

w_label = tk.Label(text="Enter Your Weight (kg)")
w_label.place(x=130, y=50)

w_entry = tk.Entry()
w_entry.place(x=132, y=80)

h_label = tk.Label(text="Enter Your Height (cm)")
h_label.place(x=130, y=130)

h_entry = tk.Entry()
h_entry.place(x=132, y=160)

button1 = tk.Button(text="Calculate", command=Calculate)
button1.place(x=160, y=200)

a_label = tk.Label()
a_label.place(x=50, y=250)

window.mainloop()
