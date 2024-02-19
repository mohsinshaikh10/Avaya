import serial  
import time  

def connect():
    print("Booting required Systems")  
    port="/dev/tty.HC-06-DevB" 
    bluetooth=serial.serial(port,9600)  
    print("Home Connected")

def process(inputstr):
    bluetooth.flushInput()
    bluetooth.write(inputstr)
    
process("bedON")