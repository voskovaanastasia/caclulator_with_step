import tkinter
from tkinter import *
from tkinter import messagebox as mb
val = ""
A = 0
operator = ""
def button_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
def button_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
def button_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
def button_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
def button_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
def button_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
def button_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
def button_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
def button_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
def button_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)
def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)
def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)
def button_step_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "^"
    val = val + "^"
    data.set(val)
def C_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            mb.showerror("Помилка", "На 0 ділити не можна")
            A == ""
            val = ""
            data.set(val)
        else:
            c = int(A / x)
            data.set(c)
            val = str(c)
    elif operator == '^':
        x = int((val2.split("^")[1]))
        c = A**x
        data.set(c)
        val = str(c)
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("Калькулятор")
data = StringVar()
lbl = Label(root, text="Label", anchor=SE, font=20, textvariable=data, background="#ffffff", fg="#000000")
lbl.pack(expand=True, fill="both")
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill="both")
row2 = Frame(root)
row2.pack(expand=True, fill="both")
row3 = Frame(root)
row3.pack(expand=True, fill="both")
row4 = Frame(root)
row4.pack(expand=True, fill="both")

button1 = Button(row1, text="1", font=22, border=0, command=button_1_isclicked)
button1.pack(side=LEFT, expand=True, fill="both")
button2 = Button(row1, text="2", font=22, border=0, command=button_2_isclicked)
button2.pack(side=LEFT, expand=True, fill="both")
button3 = Button(row1, text="3", font=22, border=0, command=button_3_isclicked)
button3.pack(side=LEFT, expand=True, fill="both")
button_add = Button(row1, text="+", font=22, border=0, command=btn_add_clicked)
button_add.pack(side=LEFT, expand=True, fill="both")

button4 = Button(row2, text="4", font=22, border=0, command=button_4_isclicked)
button4.pack(side=LEFT, expand=True, fill="both")
button5 = Button(row2, text="5", font=22, border=0, command=button_5_isclicked)
button5.pack(side=LEFT, expand=True, fill="both")
button6 = Button(row2, text="6", font=22, border=0, command=button_6_isclicked)
button6.pack(side=LEFT, expand=True, fill="both")
button_sub = Button(row2, text="-", font=22, border=0, command=btn_sub_clicked)
button_sub.pack(side=LEFT, expand=True, fill="both")

button7 = Button(row3, text="7", font=22, border=0, command=button_7_isclicked)
button7.pack(side=LEFT, expand=True, fill="both")
button8 = Button(row3, text="8", font=22, border=0, command=button_8_isclicked)
button8.pack(side=LEFT, expand=True, fill="both")
button9 = Button(row3, text="9", font=22, border=0, command=button_9_isclicked)
button9.pack(side=LEFT, expand=True, fill="both")
buttonmul = Button(row3, text="*", font=22, border=0, command=btn_mul_clicked)
buttonmul.pack(side=LEFT, expand=True, fill="both")

buttonC = Button(row4, text="C", font=22, border=0, command=C_pressed)
buttonC.pack(side=LEFT, expand=True, fill="both")
button0 = Button(row4, text="0", font=22, border=0, command=button_0_isclicked)
button0.pack(side=LEFT, expand=True, fill="both")
buttonequal = Button(row4, text="=", font=22, border=0, command=result)
buttonequal.pack(side=LEFT, expand=True, fill="both")
buttondiv = Button(row4, text="/", font=22, border=0, command=btn_div_clicked)
buttondiv.pack(side=LEFT, expand=True, fill="both")
buttonstep = Button(row4, text="^", font=22, border=0, command=button_step_clicked)
buttonstep.pack(side=LEFT, expand=True, fill="both")

root.mainloop()