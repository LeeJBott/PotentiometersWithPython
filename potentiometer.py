import machine
from time import sleep
p1 = 28 #Potentiometer middle pin
potent = machine.ADC(p1) #class potent, machine, Analogue to Digital Converter

while True:
    potVal = potent.read_u16() #read_u16 = reading 16 bit number (2 x^y raised to power of 16 = 65535)
    print(potVal)
    sleep(1)
    potVal = potent.read_u16()
    voltage=(3.3/65106)*potVal-(400*3.3/65106) #determining the equation of a line(slope)
    print(voltage)
    sleep(1)
