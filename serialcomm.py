import serial
#import matplotlib

a=0
array=[]
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)
while(1):
    ser.isOpen()
    var = str(ser.readline())
    var2 = var[var.find('logica')+7:var.find('\r')]
    print(var2)

