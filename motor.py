import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
motorInputA1 = 16    # Input Pin
motorInputA2 = 18    # Input Pin
motorInputB1 = 39   # Input Pin
motorInputB2 = 40    # Input Pin
#Motor3 = 22    # Enable Pin
 
GPIO.setup(motorInputA1,GPIO.OUT)
GPIO.setup(motorInputA2,GPIO.OUT)
GPIO.setup(motorInputB1,GPIO.OUT)
GPIO.setup(motorInputB2,GPIO.OUT)

print "FORWARD MOTION"
GPIO.output(motorInputA1,GPIO.HIGH)
GPIO.output(motorInputA2,GPIO.LOW)
GPIO.output(motorInputB1,GPIO.HIGH)
GPIO.output(motorInputB2,GPIO.LOW)
 
sleep(2)
 
print "BACKWARD MOTION"
GPIO.output(motorInputA1,GPIO.LOW)
GPIO.output(motorInputA2,GPIO.HIGH)
GPIO.output(motorInputB1,GPIO.LOW)
GPIO.output(motorInputB2,GPIO.HIGH)

sleep(2)
 
print "STOP"
GPIO.output(motorInputA1,GPIO.LOW)
GPIO.output(motorInputA2,GPIO.LOW)
GPIO.output(motorInputB1,GPIO.LOW)
GPIO.output(motorInputB2,GPIO.LOW)

GPIO.cleanup()