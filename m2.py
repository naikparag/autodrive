from gpiozero import Motor
from time import sleep
from picamera import PiCamera
from datetime import datetime

motorA1 = 23
motorA2 = 24

motorB1 = 20
motorB2 = 21

camera = PiCamera()
camera.resolution = (64, 48)
currentTime = 0

def capture():
    currentTime = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % currentTime)

motorA = Motor(motorA1, motorA2)
motorB = Motor(motorB1, motorB2)

motorA.forward(0.5)
motorB.forward(0.5)

capture()

sleep(1)

motorA.forward(0.9)
motorB.forward(0)

sleep(2)

motorA.forward(0)
motorB.forward(0.9)

sleep(2)

capture()

motorA.backward(0.4)
motorB.backward(0.4)

sleep(3)

motorA.stop()