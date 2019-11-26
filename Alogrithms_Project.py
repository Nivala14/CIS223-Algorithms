# Ultrasonic sensor and fan
import pyfirmata
import time

board = pyfirmata.Arduino('COM3') #Connect to the port the Arduino is connected to

board.digital[7].mode = pyfirmata.OUTPUT #Trig Pin
board.digital[8].mode = pyfirmata.INPUT #Echo Pin
board.digital[6].mode = pyfirmata.OUTPUT #Fan
board.digital[11].mode = pyfirmata.OUTPUT #Blue LED
board.digital[12].mode = pyfirmata.OUTPUT #Green LED
board.digital[13].mode = pyfirmata.OUTPUT #Red LED

while True:
    #Tells ultrasonic sensor to send a signal then it reads how long it took that signal to come back 
    board.digital[7].write(0) #Turn trig pin off
    time.sleep(0.02) #Adds delay for the time between sending the signal
    board.digital[7].write(1) #Turn trig pin on
    time.sleep(0.1) #Adds delay for the time between sending the signal
    board.digital[7].write(0) #Turn trig pin off
    data = board.digital[7].read()
    distance = data/58 #Takes the time it took the signal to come back and calculates the distance

while True:
    #Loop goes infinitely reading the distance and telling which led to turn on and when the fan should turn on
    if(distance < 10 and distance > 0):
            board.digital[6].write(1) #Fan on
            board.digital[11].write(0)
            board.digital[12].write(1)
            board.digital[13].write(0)
    elif(distance < 20 and distance > 10):
            board.digital[6].write(0)#Fan off
            board.digital[11].write(1)
            board.digital[12].write(0)
            board.digital[13].write(0)
    elif(distance < 30 and distance > 20):
            board.digital[6].write(1)#Fan on
            board.digital[11].write(0)
            board.digital[12].write(0)
            board.digital[13].write(1)
    else:
            board.digital[6].write(0)#Fan off
            board.digital[11].write(0)
            board.digital[12].write(0)
            board.digital[13].write(0)
time.sleep(100) #Adds a delay for the time between the LEDs turning on and off