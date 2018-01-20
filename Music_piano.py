#!/usr/bin/python

"By Andre Akue"

import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pygame.mixer.init()

while 1: #choosing volume
	try:
		global vol
		vol = int(input("Choose volume between 0 and 100\n>"))*0.01
		time.sleep(1)
		print ("Volume set")
		break
	except:
		time.sleep(0.5)
		print ("Sorry. The input was not recognized. Try again.\n")

class keys:

	def __init__(self, button, led, sound):
		self.key = button
		self.led = led
		self.note = pygame.mixer.Sound(sound)
		self.note.set_volume(vol)
		GPIO.setup(self.key, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(self.led, GPIO.OUT, initial = 0)

	def press(self,key):
		self.note.play(maxtime = 300)
		GPIO.output(self.led, 1)
		time.sleep(0.3)
		GPIO.output(self.led, 0)
		time.sleep(0.3)

K1 = keys(20,21, "piano_effects/do.wav")
K2 = keys(19,16, "piano_effects/re.wav")
K3 = keys(6,12, "piano_effects/mi.wav")
K4 = keys(5,(21,13), "piano_effects/fa.wav")
K5 = keys(23,(21,16,12,25,24,13), "piano_effects/sol.wav")
K6 = keys(22,25, "piano_effects/la.wav")
K7 = keys(27,24, "piano_effects/si.wav")
K8 = keys(17,13, "piano_effects/do-octave.wav")

time.sleep(1)
print("\n!!!Piano Ready!!!\n\nExit with 'Enter(Return)'")

try:
	for i in [K1,K2,K3,K4,K5,K6,K7,K8]:
		GPIO.add_event_detect(i.key, GPIO.FALLING, callback = i.press, bouncetime = 500)
	raw_input()
	GPIO.cleanup()
	print ("Clean Exit. Have a nice day!")
	exit()

except KeyboardInterrupt:
	print ("\nCode stopped by 'keyboard interrupt'. Have a nice day.")
	GPIO.cleanup()
	exit()
