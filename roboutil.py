import RPi.GPIO as GPIO
from time import sleep

LOW = 30
MID = 60
HIGH = 80

class Motor():

	def __init__(self, inputA, inputB, enable):
		GPIO.setmode(GPIO.BOARD)
		self.inputA = inputA
		self.inputB = inputB
		self.enable = enable
		GPIO.setup(inputA,GPIO.OUT)
		GPIO.setup(inputB,GPIO.OUT)
		GPIO.setup(enable,GPIO.OUT)
		self.pwm = GPIO.PWM(enable,100) # port, frequency
		self.pwm.start(0)

	def forward(self, speed=90):
		GPIO.output(self.inputA,GPIO.LOW)
		GPIO.output(self.inputB,GPIO.HIGH)
		self.pwm.ChangeDutyCycle(speed)
		print("forward with motor speed. - " + str(speed))

	def backward(self):
		GPIO.output(self.inputA,GPIO.HIGH)
		GPIO.output(self.inputB,GPIO.LOW)
		self.pwm.ChangeDutyCycle(60)

	def stop(self):
		print("stopping PWM pin now...")
		self.pwm.ChangeDutyCycle(30)

	def kill(self):
		GPIO.output(self.enable,GPIO.LOW)

class Robo():

	def __init__(self, motorA, motorB):
		GPIO.setmode(GPIO.BOARD)
		self.motorA = motorA
		self.motorB = motorB

	def process(self, command):

		print("processing command - " + command)

		if command == 'L1':
			self.l1()
		if command == 'L2':
			self.l2()
		if command == 'R1':
			self.r1()
		if command == 'R2':
			self.r2()
		if command == 'FF':
			self.forward()
		if command == 'BB':
			self.backward()


		sleep(1)
		self.stop()
		print("now stopping motor.")

	def l1(self):
		self.motorA.forward(HIGH)
		self.motorB.forward(MID)

	def l2(self):
		self.motorA.forward(HIGH)
		self.motorB.forward(LOW)

	def r1(self):
		self.motorA.forward(MID)
		self.motorB.forward(HIGH)

	def r2(self):
		self.motorA.forward(LOW)
		self.motorB.forward(HIGH)

	def forward(self):
		self.motorA.forward()
		self.motorB.forward()

	def backward(self):
		self.motorA.backward()
		self.motorB.backward()

	def stop(self):
		self.motorA.stop()
		self.motorB.stop()

	def cleanup(self):
		GPIO.cleanup()
