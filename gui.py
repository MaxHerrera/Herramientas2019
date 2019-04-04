from tkinter import *


window = Tk()
window.title("Window 1")
window.geometry('640x480')
lbl = Label(window, text="Welcome little grasshopper")
lbl.grid(column=2,row=1)
def clicked():
	lbl.grid(column=0, row=0)
	lbl2=Label(window,text=txt.get())
	lbl2.grid(column=1, row=3)
	print("Hola")
btn = Button(window, text='Push me!', command=clicked)
btn.grid(column=1,row=1)
txt = Entry(window, width=10)
txt.grid(column=0,row=3)




window.mainloop()

