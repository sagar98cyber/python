# import everything from tkinter module
import math
from tkinter import *

e = ""
butBG="#3E497A"
butFG = "#F1D00A"
aFore = '#21325E'
aBack = '#F0F0F0'
def press(num):
	global e
	e = e + str(num)
	equation.set(e)


def equalpress():
	try:
		global e
		total = str(eval(e))
		equation.set(total)
		e = ""
	except:
		equation.set(" error ")
		e = ""

def clear():
	global e
	e = ""
	equation.set("")

def sqRoot():
	global e
	e = math.sqrt(int(e))
	equation.set(e)



if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="#21325E")
	gui.title("Sagar's Calculator")
	gui.geometry("265x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation,bg=butFG,fg=butBG,width=12)
	expression_field.grid(columnspan=4, ipadx=95)
	button1 = Button(gui, text=' 1 ', fg=butFG, bg=butBG,command=lambda: press(1), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button2 = Button(gui, text=' 2 ',fg=butFG, bg=butBG,
					command=lambda: press(2), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button3 = Button(gui, text=' 3 ', fg=butFG, bg=butBG,
					command=lambda: press(3), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	clear = Button(gui, text='Clear', fg=butFG, bg=butBG, command=clear, height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button4 = Button(gui, text=' 4 ', fg=butFG, bg=butBG,
					command=lambda: press(4), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button5 = Button(gui, text=' 5 ', fg=butFG, bg=butBG,
					command=lambda: press(5), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button6 = Button(gui, text=' 6 ', fg=butFG, bg=butBG,
					command=lambda: press(6), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button7 = Button(gui, text=' 7 ', fg=butFG, bg=butBG,
					command=lambda: press(7), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	minus = Button(gui, text=' - ', fg=butFG, bg=butBG,
				command=lambda: press("-"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button8 = Button(gui, text=' 8 ',fg=butFG, bg=butBG,
					command=lambda: press(8), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button9 = Button(gui, text=' 9 ',fg=butFG, bg=butBG,
					command=lambda: press(9), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	multiply = Button(gui, text=' * ', fg=butFG, bg=butBG,
					command=lambda: press("*"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button0 = Button(gui, text=' 0 ', fg=butFG, bg=butBG,
					command=lambda: press(0), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	divide = Button(gui, text=' / ', fg=butFG, bg=butBG,
					command=lambda: press("/"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	equal = Button(gui, text=' = ', fg=butFG, bg=butBG,
				command=equalpress, height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button00 = Button(gui, text=' 00 ', fg=butFG, bg=butBG,
					command=lambda: press('00'), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	Decimal= Button(gui, text='.', fg=butFG, bg=butBG,
					command=lambda: press('.'), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	sqrt = Button(gui, text=' sqrt ', fg=butFG, bg=butBG,
					command=lambda: sqRoot(), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	perc = Button(gui, text=' % ', fg=butFG, bg=butBG,
					command=lambda: press("/100*"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	plus = Button(gui, text=' + ', fg=butFG, bg=butBG,
				command=lambda: press("+"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)

	Decimal.grid(row=3, column=0) 
	sqrt.grid(row=3, column=1)
	perc.grid(row=3, column=2)
	clear.grid(row=3, column=3)
	button1.grid(row=4, column=0)
	button2.grid(row=4, column=1)
	button3.grid(row=4, column=2)
	plus.grid(row=4, column=3)
	button4.grid(row=5, column=0)
	button5.grid(row=5, column=1)
	button6.grid(row=5, column=2)
	minus.grid(row=5, column=3)
	button7.grid(row=6, column=0)
	button8.grid(row=6, column=1)
	button9.grid(row=6, column=2)
	multiply.grid(row=6, column=3)
	button00.grid(row=7, column=0)
	button0.grid(row=7, column=1)
	equal.grid(row=7, column=2)
	divide.grid(row=7, column=3)
	
	# start the GUI
	gui.mainloop()