from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
window = ThemedTk(theme='equilux')
window.configure(bg="gray27")


result = ""
equation = StringVar()

def press(x):
    global result
    result = result + str(x)
    equation.set(result)
    txt.delete(0, END)
    txt.insert(0, result)

def equalpress():
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result = ""
        txt.delete(0, END)
        txt.insert(0, total)

    except:
        equation.set("error")
        result = ""

def clear():
    txt.delete(0, END)

txt = ttk.Entry(window)
txt.grid(column = 0, row = 0, columnspan = 3)
seven = ttk.Button(window, text = "7", command = lambda: press(7))
seven.grid(column = 0, row = 1)
eight = ttk.Button(window, text = "8", command = lambda: press(8))
eight.grid(column = 1, row = 1)
nine = ttk.Button(window, text = "9", command = lambda: press(9))
nine.grid(column = 2, row = 1)
four = ttk.Button(window, text = "4", command = lambda: press(4))
four.grid(column = 0, row = 3)
five = ttk.Button(window, text = "5", command = lambda: press(5))
five.grid(column = 1, row = 3)
six = ttk.Button(window, text = "6", command = lambda: press(6))
six.grid(column = 2, row = 3)
one = ttk.Button(window, text = "1", command = lambda: press(1))
one.grid(column = 0, row = 5)
two = ttk.Button(window, text = "2", command = lambda: press(2))
two.grid(column = 1, row = 5)
three = ttk.Button(window, text = "3", command = lambda: press(3))
three.grid(column = 2, row = 5)
plus = ttk.Button(window, text = "+", command = lambda: press("+"))
plus.grid(column = 4, row = 1)
minus = ttk.Button(window, text = "-", command = lambda: press("-"))
minus.grid(column = 4, row = 3)
c = ttk.Button(window, text = "C", command = clear)
c.grid(column = 4, row = 0)
mult = ttk.Button(window, text = "X", command = lambda: press("*"))
mult.grid(column = 0, row = 6)
div = ttk.Button(window, text = "/", command = lambda: press("/"))
div.grid(column = 1, row = 6)
equals = ttk.Button(window, text = "=", command = equalpress)
equals.grid(column = 2, row = 6)
ep = ttk.Button(window, text = ")", command = lambda: press(")"))
ep.grid(column = 4, row = 5)
lp = ttk.Button(window, text = "(", command = lambda: press("("))
lp.grid(column = 4, row = 6)
power = ttk.Button(window, text = "^", command = lambda: press("**"))
power.grid(column = 1, row = 7)
root = ttk.Button(window, text = "√", command = lambda: press("math.sqrt("))
root.grid(column = 2, row = 7)
window.mainloop()