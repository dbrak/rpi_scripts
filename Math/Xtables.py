
from Tkinter import *
from random import randint


bw = 8
bc = "turquoise"
window = Tk()
window.title("Xtable Game")
score = 0


# Layout

main = Frame(window)
main.grid (row = 1, column = 2, sticky = N)
space = Frame(window)
space.grid(row = 2, column = 1, sticky = N, columnspan = 2)
bottom = Frame(window)
bottom.grid (row = 3, column = 2, sticky = N)

#Main

Label(main, text = "What do you want your top times table to be? ").grid(row = 0, column = 0, sticky = W)

q1 = Entry(main, width = bw, bg = bc)
q1.grid(row = 0, column = 1, sticky = E)


Label(main, text = "What do you want your target number to be? ").grid(row = 1, column = 0, sticky = W)

q2 = Entry(main, width = bw, bg = bc)
q2.grid(row = 1, column = 1, sticky = E)

def click():
	max = q1.get()
	target = q2.get()
	
	for widget in main.winfo_children():
		widget.destroy()
	
	
	Label(main, text = "X").grid(row = 1, column = 1, sticky = W)
	l1 = Canvas(main,width = 110,height=5)
	l1.grid(row = 2, column = 1, sticky = W)
	l1.create_line(0,5,110,5)
	
	global box1
	box1 = Entry(main, width = bw, bg = bc)
	box1.grid(row = 0, column = 1, sticky = E)
	box1.insert(END, randint(0,int(max)))
	box1.config(state = 'readonly')
	
	global box2
	box2 = Entry(main, width = bw, bg = bc)
	box2.grid(row = 1, column = 1, sticky = E)
	box2.insert(END, randint(0,12))
	box2.config(state = 'readonly')

	global quAnswer
	quAnswer = Entry(main, width = bw, bg = bc)
	quAnswer.grid(row = 3, column = 1, sticky = E)
	
	targetbox.config(state = 'normal')
	targetbox.delete(0,END)
	targetbox.insert(END, target)
	targetbox.config(state = 'readonly')
	
	scorebox.config(state = 'normal')
	scorebox.delete(0,END)
	scorebox.insert(END, score)
	scorebox.config(state = 'readonly')
	
	maxbox.config(state = 'normal')
	maxbox.delete(0,END)
	maxbox.insert(END, max)
	maxbox.config(state = 'readonly')
	
	Button(main, text = "SUBMIT", width = bw, command = calc).grid(row = 3, column = 0, sticky = N)


Button(main, text = "SUBMIT", width = bw, command = click).grid(row = 3, column = 1, sticky = N)



#Space
l2 = Canvas(space,width = 110,height=5)
l2.grid(row = 0, column = 0, sticky = N)
l2.create_line(0,5,110,5, width = 3)


#Bottom

Label(bottom, text = "Score").grid(row = 0, column = 0, sticky = N)
Label(bottom, text = "Target").grid(row = 0, column = 1, sticky = N)
Label(bottom, text = "Top Table").grid(row = 0, column = 2, sticky = N)

scorebox = Entry(bottom, width = bw, bg = bc)
scorebox.grid(row = 1, column = 0, sticky = N)
scorebox.config(state = 'readonly')

targetbox = Entry(bottom, width = bw, bg = bc)
targetbox.grid(row = 1, column = 1, sticky = N)
targetbox.config(state = 'readonly')

maxbox = Entry(bottom, width = bw, bg = bc)
maxbox.grid(row = 1, column = 2, sticky = N)
maxbox.config(state = 'readonly')
#Submit Button

def calc():
	answer = int(quAnswer.get())
	s = int(scorebox.get())
	n1 = int(box1.get())
	n2 = int(box2.get())
	
	if (answer == n1 * n2):
		s = s + 3
	else:
		s = s - 5
	
	scorebox.config(state = 'normal')
	scorebox.delete(0, END)	
	scorebox.insert(END, s)
	scorebox.config(state = 'readonly')
	
	if int(targetbox.get()) <= s:
		Label(space, text = "Congratulations -  You Won!",bg="blue").grid(row = 1, column = 0, sticky = N)
	else:
			
		box1.config(state = 'normal')
		box1.delete(0,END)
		box1.insert(END, randint(0,int(maxbox.get())))
		box1.config(state = 'readonly')

		box2.config(state = 'normal')
		box2.delete(0,END)
		box2.insert(END, randint(0,12))
		box2.config(state = 'readonly')
		
		quAnswer.delete(0,END)
		
		Button(main, text = "SUBMIT", width = bw, command = calc).grid(row = 3, column = 0, sticky = N)
		
	







window.mainloop()


