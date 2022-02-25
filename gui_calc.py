# import everything from tkinter module
import math
from tkinter import *

exp = ""
butBG="#3E497A"
butFG = "#F1D00A"
aFore = '#21325E'
aBack = '#F0F0F0'
def pressed(num):
	global exp
	exp = exp + str(num)
	eq.set(exp)


def equalPress():
	try:
		global exp
		sum = str(eval(exp))
		eq.set(sum)
		exp = ""
	except:
		eq.set(" error ")
		exp = ""

def clear():
	global exp
	exp = ""
	eq.set("")

def squareRoot():
	global exp
	exp = math.sqrt(int(exp))
	eq.set(exp)



if __name__ == "__main__":
	GUI = Tk()
	GUI.configure(background="#21325E")
	GUI.title("Sagar's Calculator")
	GUI.geometry("265x150")
	eq = StringVar()
	expression_field = Entry(GUI, textvariable=eq,bg=butFG,fg=butBG,width=12)
	expression_field.grid(columnspan=4, ipadx=95)
	button1 = Button(GUI, text=' 1 ', fg=butFG, bg=butBG,command=lambda: pressed(1), height=1, width=7,activeforeground="Orange", activebackground="blue",)
	button2 = Button(GUI, text=' 2 ',fg=butFG, bg=butBG,
					command=lambda: pressed(2), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button3 = Button(GUI, text=' 3 ', fg=butFG, bg=butBG,
					command=lambda: pressed(3), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	clear = Button(GUI, text='Clear', fg=butFG, bg=butBG, command=clear, height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button4 = Button(GUI, text=' 4 ', fg=butFG, bg=butBG,
					command=lambda: pressed(4), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button5 = Button(GUI, text=' 5 ', fg=butFG, bg=butBG,
					command=lambda: pressed(5), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button6 = Button(GUI, text=' 6 ', fg=butFG, bg=butBG,
					command=lambda: pressed(6), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button7 = Button(GUI, text=' 7 ', fg=butFG, bg=butBG,
					command=lambda: pressed(7), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	minus = Button(GUI, text=' - ', fg=butFG, bg=butBG,
				command=lambda: pressed("-"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button8 = Button(GUI, text=' 8 ',fg=butFG, bg=butBG,
					command=lambda: pressed(8), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button9 = Button(GUI, text=' 9 ',fg=butFG, bg=butBG,
					command=lambda: pressed(9), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	multiply = Button(GUI, text=' * ', fg=butFG, bg=butBG,
					command=lambda: pressed("*"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button0 = Button(GUI, text=' 0 ', fg=butFG, bg=butBG,
					command=lambda: pressed(0), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	divide = Button(GUI, text=' / ', fg=butFG, bg=butBG,
					command=lambda: pressed("/"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	equal = Button(GUI, text=' = ', fg=butFG, bg=butBG,
				command=equalPress, height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	button00 = Button(GUI, text=' 00 ', fg=butFG, bg=butBG,
					command=lambda: pressed('00'), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	Decimal= Button(GUI, text='.', fg=butFG, bg=butBG,
					command=lambda: pressed('.'), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	sqrt = Button(GUI, text=' sqrt ', fg=butFG, bg=butBG,
					command=lambda: squareRoot(), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	perc = Button(GUI, text=' % ', fg=butFG, bg=butBG,
					command=lambda: pressed("/100*"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)
	plus = Button(GUI, text=' + ', fg=butFG, bg=butBG,
				command=lambda: pressed("+"), height=1, width=7,activeforeground=aFore, activebackground=aBack,)

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
	GUI.mainloop()