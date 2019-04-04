import serial
from tkinter import *


window = Tk()
window.title("Window 1")
window.geometry('640x480')
lbl = Label(window, text="Welcome little grasshopper")
lbl.grid(column=0,row=0)


port = serial.Serial(port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)
port.isOpen()

lbl2 = Label(window, text=port.readline())
lbl2.grid(column=0,row=2)
lbl2.config(text=port.readline())
lbl2.after(1000)

def clicked():
	port.write(int(txt.get()))
	lbl2.config(text="Send: "+ txt.get())

btn = Button(window, text='Send', command=clicked)
btn.grid(column=1,row=1)
txt = Entry(window, width=10)
txt.grid(column=0,row=1)


window.mainloop()
