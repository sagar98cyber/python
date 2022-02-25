# import everything from tkinter module
import math
from tkinter import *

expression = ""
buttonBG="#361500"
buttonFG = "#CC9544"

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)


def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

def sqRoot():
	global expression
	expression = math.sqrt(int(expression))
	equation.set(expression)



if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="#1C0A00")
	gui.title("Manav's Calculator")
	gui.geometry("235x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation,bg=buttonFG,fg=buttonBG,width=12)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg=buttonFG, bg=buttonBG,command=lambda: press(1), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button1.grid(row=3, column=0)
	button2 = Button(gui, text=' 2 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(2), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button2.grid(row=3, column=1)
	button3 = Button(gui, text=' 3 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(3), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button3.grid(row=3, column=2)
	button4 = Button(gui, text=' 4 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(4), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button4.grid(row=4, column=0)
	button5 = Button(gui, text=' 5 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(5), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button5.grid(row=4, column=1)
	button6 = Button(gui, text=' 6 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(6), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button6.grid(row=4, column=2)
	button7 = Button(gui, text=' 7 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(7), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button7.grid(row=5, column=0)
	button8 = Button(gui, text=' 8 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(8), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button8.grid(row=5, column=1)
	button9 = Button(gui, text=' 9 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(9), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button9.grid(row=5, column=2)
	button0 = Button(gui, text=' 0 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(0), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button0.grid(row=6, column=1)
	plus = Button(gui, text=' + ', fg=buttonFG, bg=buttonBG,
				command=lambda: press("+"), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	plus.grid(row=7, column=3)
	minus = Button(gui, text=' - ', fg=buttonFG, bg=buttonBG,
				command=lambda: press("-"), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	minus.grid(row=4, column=3)
	multiply = Button(gui, text=' * ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("*"), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	multiply.grid(row=5, column=3)
	divide = Button(gui, text=' / ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("/"), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	divide.grid(row=6, column=3)
	equal = Button(gui, text=' = ', fg=buttonFG, bg=buttonBG,
				command=equalpress, height=1, width=7,activeforeground="Orange", activebackground="blue",)
	equal.grid(row=6, column=2)
	clear = Button(gui, text='Clear', fg=buttonFG, bg=buttonBG, command=clear, height=1, width=7,activeforeground="Orange", activebackground="blue",)
	clear.grid(row=3, column=3)
	Decimal= Button(gui, text='.', fg=buttonFG, bg=buttonBG,
					command=lambda: press('.'), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	Decimal.grid(row=7, column=0) 
	button00 = Button(gui, text=' 00 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press('00'), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button00.grid(row=6, column=0)
	sqrt = Button(gui, text=' sqrt ', fg=buttonFG, bg=buttonBG,
					command=lambda: sqRoot(), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	sqrt.grid(row=7, column=1)
	perc = Button(gui, text=' % ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("/100*"), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	perc.grid(row=7, column=2)
	# start the GUI
	gui.mainloop()