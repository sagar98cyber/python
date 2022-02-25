# import everything from tkinter module
import math
from tkinter import *

expression = ""
buttonBG="#3E497A"
buttonFG = "#F1D00A"
aForeground = '#21325E'
aBackGround = '#F0F0F0'
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
	gui.configure(background="#21325E")
	gui.title("Sagar's Calculator")
	gui.geometry("235x150")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation,bg=buttonFG,fg=buttonBG,width=12)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg=buttonFG, bg=buttonBG,command=lambda: press(1), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button1.grid(row=4, column=0)
	button2 = Button(gui, text=' 2 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(2), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button2.grid(row=4, column=1)
	button3 = Button(gui, text=' 3 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(3), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button3.grid(row=4, column=2)
	clear = Button(gui, text='Clear', fg=buttonFG, bg=buttonBG, command=clear, height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	clear.grid(row=3, column=3)
	button4 = Button(gui, text=' 4 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(4), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button4.grid(row=5, column=0)
	button5 = Button(gui, text=' 5 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(5), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button5.grid(row=5, column=1)
	button6 = Button(gui, text=' 6 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(6), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button6.grid(row=5, column=2)
	button7 = Button(gui, text=' 7 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(7), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	minus = Button(gui, text=' - ', fg=buttonFG, bg=buttonBG,
				command=lambda: press("-"), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	minus.grid(row=5, column=3)
	button7.grid(row=6, column=0)
	button8 = Button(gui, text=' 8 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(8), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button8.grid(row=6, column=1)
	button9 = Button(gui, text=' 9 ',fg=buttonFG, bg=buttonBG,
					command=lambda: press(9), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button9.grid(row=6, column=2)

	multiply = Button(gui, text=' * ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("*"), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	multiply.grid(row=6, column=3)
	button0 = Button(gui, text=' 0 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press(0), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button0.grid(row=7, column=1)
	
	divide = Button(gui, text=' / ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("/"), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	divide.grid(row=7, column=3)
	equal = Button(gui, text=' = ', fg=buttonFG, bg=buttonBG,
				command=equalpress, height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	equal.grid(row=7, column=2)
	button00 = Button(gui, text=' 00 ', fg=buttonFG, bg=buttonBG,
					command=lambda: press('00'), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	button00.grid(row=7, column=0)
	
	Decimal= Button(gui, text='.', fg=buttonFG, bg=buttonBG,
					command=lambda: press('.'), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	Decimal.grid(row=3, column=0) 
	
	sqrt = Button(gui, text=' sqrt ', fg=buttonFG, bg=buttonBG,
					command=lambda: sqRoot(), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	sqrt.grid(row=3, column=1)
	perc = Button(gui, text=' % ', fg=buttonFG, bg=buttonBG,
					command=lambda: press("/100*"), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	perc.grid(row=3, column=2)
	plus = Button(gui, text=' + ', fg=buttonFG, bg=buttonBG,
				command=lambda: press("+"), height=1, width=7,activeforeground=aForeground, activebackground=aBackGround,)
	plus.grid(row=4, column=3)
	# start the GUI
	gui.mainloop()