import matplotlib.animation as anim
import matplotlib.pyplot as plt
import serial
from matplotlib import style
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data='0'

window = Tk()
window.title("Window 1")
window.geometry('640x480')

style.use('ggplot')
xar = []
yar = []

fig = plt.figure(figsize=(5,4), dpi=100)
a = fig.add_subplot(1,1,1)
a.set_ylim(0,1023)
line, = a.plot(xar,yar,'r')
plt.xlabel("Seconds")
plt.ylabel("Variable")

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)
ser.isOpen()

def animate(i):
	xar.append(i)
	#yar.append(99-i)
	data = ser.readline()
	data = str(data)
	b= data.find('log')
	c= data.find(' b')
	datum= data[b+4:c]
	print(data)
	print(datum)
	yar.append(int(datum))
	#Teoricamente guarda el dato enviado por el arduino en yar,'Teoricamente' :v
	line.set_data(xar,yar)
	a.set_xlim(0, i+1)

plotcanvas = FigureCanvasTkAgg(fig,window)
plotcanvas.get_tk_widget().grid(column=1,row=1)
ani = anim.FuncAnimation(fig, animate, interval=1000, blit=False)

window.mainloop()


