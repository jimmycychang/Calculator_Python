from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.iconbitmap("icon.ico")
root.geometry("340x500")

font = ("Ink Free", 25)

def button_press(key):
    global equation_text
    equation_text = equation_text + str(key)
    equation_label.set(equation_text)
def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Value Error")
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""
def reciprocal():
    global equation_text
    try:
        equation_text = str(1/float(equation_text))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")
def delete():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)
def negative():
    global equation_text
    equation_text = str(float(equation_text)*(-1))
    equation_label.set(equation_text)
def sin():
    global equation_text
    try:
        equation_text = str(str(math.sin(math.radians(float(equation_text)))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")
def cos():
    global equation_text
    try:
        equation_text = str(str(math.cos(math.radians(float(equation_text)))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")
def tan():
    global equation_text
    try:
        equation_text = str(str(math.tan(math.radians(float(equation_text)))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")
def factorial():
    global equation_text
    try:
        equation_text = str(str(math.factorial(int(equation_text))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")        
def log():
    global equation_text
    try:
        equation_text = str(str(math.log10(float(equation_text))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")     
def ln():
    global equation_text
    try:
        equation_text = str(str(math.log(float(equation_text))))
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Value Error")

equation_text = ""
equation_label = StringVar()

label = Label(root, textvariable=equation_label, font=("Ink Free", 25), bg="lightgrey",height=1)
label.pack(fill="both")

frame = Frame(root)
frame.pack(pady=(10,0))

button_0 = Button(frame, text=0, height=1, width=3, font=font, command=lambda: button_press(0))
button_1 = Button(frame, text=1, height=1, width=3, font=font, command=lambda: button_press(1))
button_2 = Button(frame, text=2, height=1, width=3, font=font, command=lambda: button_press(2))
button_3 = Button(frame, text=3, height=1, width=3, font=font, command=lambda: button_press(3))
button_4 = Button(frame, text=4, height=1, width=3, font=font, command=lambda: button_press(4))
button_5 = Button(frame, text=5, height=1, width=3, font=font, command=lambda: button_press(5))
button_6 = Button(frame, text=6, height=1, width=3, font=font, command=lambda: button_press(6))
button_7 = Button(frame, text=7, height=1, width=3, font=font, command=lambda: button_press(7))
button_8 = Button(frame, text=8, height=1, width=3, font=font, command=lambda: button_press(8))
button_9 = Button(frame, text=9, height=1, width=3, font=font, command=lambda: button_press(9))

button_dec = Button(frame, text=".", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("."))
button_div = Button(frame, text="÷", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("/"))
button_mul = Button(frame, text="×", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("*"))
button_sub = Button(frame, text="−", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("-"))
button_add = Button(frame, text="+", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("+"))
button_mod = Button(frame, text="%", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("%"))
button_x_2 = Button(frame, text="x²", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("**2"))
button_x_3 = Button(frame, text="x³", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press("**3"))
button_pi = Button(frame, text="π", height=1, width=3, bg="lightgray", font=font, command=lambda: button_press(str(round(math.pi,4))))

button_equ = Button(frame, text="=", height=1, width=3, bg="lightgray", font=font, command=equal)
button_clr = Button(frame, text="AC", height=1, width=3, bg="lightgray", font=font, command=clear)
button_del = Button(frame, text="←", height=1, width=3, bg="lightgray", font=font, command=delete)
button_rec = Button(frame, text="1/x", height=1, width=3, bg="lightgray", font=font, command=reciprocal)
button_neg = Button(frame, text="+/−", height=1, width=3, bg="lightgray", font=font, command=negative)
button_sin = Button(frame, text="sin", height=1, width=3, bg="lightgray", font=font, command=sin)
button_cos = Button(frame, text="cos", height=1, width=3, bg="lightgray", font=font, command=cos)
button_tan = Button(frame, text="tan", height=1, width=3, bg="lightgray", font=font, command=tan)
button_fact = Button(frame, text="n!", height=1, width=3, bg="lightgray", font=font, command=factorial)
button_log = Button(frame, text="log", height=1, width=3, bg="lightgray", font=font, command=log)
button_ln = Button(frame, text="ln", height=1, width=3, bg="lightgray", font=font, command=ln)


button_neg.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dec.grid(row=5, column=2)
button_rec.grid(row=5, column=3)
button_equ.grid(row=5, column=4)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_div.grid(row=4, column=3)
button_pi.grid(row=4, column=4)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_mul.grid(row=3, column=3)
button_mod.grid(row=3, column=4)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_sub.grid(row=2, column=3)
button_clr.grid(row=2, column=4)

button_x_2.grid(row=1, column=0)
button_x_3.grid(row=1, column=1)
button_fact.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_del.grid(row=1, column=4)

button_sin.grid(row=0, column=0)
button_cos.grid(row=0, column=1)
button_tan.grid(row=0, column=2)
button_log.grid(row=0, column=3)
button_ln.grid(row=0, column=4)


root.mainloop()