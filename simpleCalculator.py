from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="white")

e = Entry(root, width=24, borderwidth=2, bg="white", fg="black", font=("Arial"))
e.grid(row=0, column=0, columnspan=4, padx=30, pady=30)

def button_click(num):
    e.insert(END, num)

def button_clear():
    e.delete(0,END)

def button_equal():
    second_num = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num+float(second_num))
    if math == "subtraction":
        e.insert(0, f_num-float(second_num))
    if math == "multiplication":
        e.insert(0, f_num*float(second_num))
    if math == "division":
        e.insert(0, f_num/float(second_num))

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    e.delete(0,END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    e.delete(0,END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    e.delete(0,END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    e.delete(0,END)

def button_decimal():
    e.insert(END, ".")

def button_delete():
    txt = e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)

def button_reciprocal():
    num = float(e.get())
    num = str(1/num)
    e.delete(0,END)
    e.insert(0,num)

def button_negative():
    num = float(e.get())
    num = str(num*(-1))
    e.delete(0,END)
    e.insert(0,num)
    
# numbers
button_1 = Button(root, text="1", padx=30, pady=10, bg="gray", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=10, bg="gray", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=10, bg="gray", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=10, bg="gray", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=10, bg="gray", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=10, bg="gray", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=10, bg="gray", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=10, bg="gray", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=10, bg="gray", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=10, bg="gray", command=lambda: button_click(0))
# functions
button_a = Button(root, text="+", padx=29, pady=10, bg="darkgray", command=button_add)
button_s = Button(root, text="-", padx=31, pady=10, bg="darkgray", command=button_subtract)
button_e = Button(root, text="=", padx=29, pady=10, bg="darkgray", command=button_equal)
button_c = Button(root, text="Clear", padx=17, pady=10, bg="dimgray", command=button_clear)
button_m = Button(root, text="*", padx=31, pady=10, bg="darkgray", command=button_multiply)
button_d = Button(root, text="/", padx=31, pady=10, bg="darkgray", command=button_divide)
button_dec = Button(root, text=".", padx=32, pady=10, bg="silver", command=button_decimal)
button_del = Button(root, text="Del", padx=23, pady=10, bg="dimgray", command=button_delete)
button_rec = Button(root, text="1/x", padx=24, pady=10, bg="dimgray", command=button_reciprocal)
button_neg = Button(root, text="+/-", padx=23, pady=10, bg="silver", command=button_negative)

button_neg.grid(row=7, column=0)
button_0.grid(row=7, column=1)
button_dec.grid(row=7, column=2)
button_e.grid(row=7, column=3)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_d.grid(row=6, column=3)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_m.grid(row=5, column=3)


button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_s.grid(row=4, column=3)

button_rec.grid(row=3, column=0)
button_c.grid(row=3, column=1)
button_del.grid(row=3, column=2)
button_a.grid(row=3, column=3)

root.mainloop()