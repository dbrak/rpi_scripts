from Tkinter import *

window = Tk()
window.title ("Polygon")


# Side number

Label(window, text = "Enter an iteger for the number of sides:") .grid (row = 0, column = 0, sticky = W)

side_num = IntVar()

scale_num = Scale(window, orient = HORIZONTAL, from_ = 3, to = 20,variable = side_num) .grid (row = 0, column = 1)

# Side Length

Label(window, text = "Enter an iteger for the lenth of the sides:") .grid(row = 4, column = 0, sticky = W)

side_len = IntVar()

scale_len = Scale(window, orient = HORIZONTAL, from_ = 3, to = 20,variable = side_len) .grid (row = 4, column = 1)



# submit button

def click() : 
	per_print.config(state = "normal")
	per_print.delete(0,END)
	per_print.insert(END, (side_num.get() * side_len.get()))
	per_print.config(state = "readonly")
	
	ang_print.config(state = "normal")
	ang_print.delete(0,END)
	ang_print.insert(END, 180 - (360/side_num.get()))
	ang_print.config(state = "readonly")

Button(window, text = "SUBMIT", width = 5, command = click) .grid (row = 5, column = 1, sticky = E) 

#Perimeter/Angle/Area

Label(window, text = "Perimeter").grid (row = 6, column = 0, sticky = W)

per_print = Entry(width = 10)
per_print.grid(row = 6, column = 1)
per_print.config(state = "readonly")

Label(window, text = "Angle").grid (row = 7, column = 0, sticky = W)

ang_print = Entry(width = 10)
ang_print.grid(row = 7, column = 1)
ang_print.config(state = "readonly")   


window.mainloop()

