#!/usr/bin/python
import RPi.GPIO as pin
pin.setmode(pin.BCM)
pin.setwarnings(True)

import pygame
import time

print ("Starting piano\n")

#SETTING UP BUTTONS
s1 = 20 #38
s2 = 19 #35
s3 = 6 #31
s4 = 5 #29
s5 = 23 #16
s6 = 22 #15
s7 = 27 #13
s8 = 17 #11
all_switches = (s1,s2,s3,s4,s5,s6,s7,s8)
pin.setup(all_switches,pin.IN,pull_up_down=pin.PUD_UP)
all_switches = [s1,s2,s3,s4,s5,s6,s7,s8]
time.sleep(0.3)
print("buttons ready\n")

#SETTING UP LEDS
left=21 #40
right=13 #33
white= (left, right)
yellow=16 #36
red=12 #32
blue=25 #22
green=24 #18
all = (left, right, yellow, red, blue, green) #all lights from one button
pin.setup(all,pin.OUT)
all_lights  = [left, yellow, red, white, all, blue, green, right] #list of all lights matching button order
time.sleep(0.3)
print ("Lights ready\n")
time.sleep(1)

#SETTING UP SOUNDS
print("Initiallizing mixer\n")
pygame.mixer.init()
time.sleep(0.3)
print ("Creating sound objects...\n")
effect1 = pygame.mixer.Sound("piano_effects/do.wav") #creating sound object
effect2 = pygame.mixer.Sound("piano_effects/re.wav")
effect3 = pygame.mixer.Sound("piano_effects/mi.wav")
effect4 = pygame.mixer.Sound("piano_effects/fa.wav")
effect5 = pygame.mixer.Sound("piano_effects/sol.wav")
effect6 = pygame.mixer.Sound("piano_effects/la.wav") 
effect7 = pygame.mixer.Sound("piano_effects/si.wav") #wrong sound
effect8 = pygame.mixer.Sound("piano_effects/do-octave.wav")
all_effects = [effect1, effect2, effect3, effect4, effect5, effect6, effect7, effect8] #list of all sound effects matching button order
time.sleep(1)
print ("Audio ready")

#SETTING UP VOLUME
try:
    vol = int(input("Choose volume between 0 and 100\n>"))*0.01
    time.sleep(1)
    print ("Volume set")
except:
    vol = 0.5
    time.sleep(0.5)
    print ("Sorry. The input was not recognized.\nDefault volume applied.\n")
time.sleep(0.5)

effect1.set_volume(vol)
effect2.set_volume(vol)
effect3.set_volume(vol)
effect4.set_volume(vol)
effect5.set_volume(vol)
effect6.set_volume(vol)
effect7.set_volume(vol)
effect8.set_volume(vol)

#SETTING UP CALLBACK FUNCTIONS
print ("Please wait while the piano is being set up...")
def event1(i):
	effect1.play(maxtime = 300)
	pin.output(left, pin.HIGH)
	time.sleep(0.3)
	pin.output(left, pin.LOW)
	time.sleep(0.3)
def event2(i):
	effect2.play(maxtime = 300)
	pin.output(yellow, pin.HIGH)
	time.sleep(0.3)
	pin.output(yellow, pin.LOW)
def event3(i):
	effect3.play(maxtime = 300)
	pin.output(red, pin.HIGH)
	time.sleep(0.3)
	pin.output(red, pin.LOW)
def event4(i):
	effect4.play(maxtime = 300)
	pin.output(white, pin.HIGH)
	time.sleep(0.3)
	pin.output(white, pin.LOW)
def event5(i):
	effect5.play(maxtime = 300)
	pin.output(all, pin.HIGH)
	time.sleep(0.3)
	pin.output(all, pin.LOW)
def event6(i):
	effect6.play(maxtime = 300)
	pin.output(blue, pin.HIGH)
	time.sleep(0.3)
	pin.output(blue, pin.LOW)
	time.sleep(0.3)
def event7(i):
	effect7.play(maxtime = 300)
	pin.output(green, pin.HIGH)
	time.sleep(0.3)
	pin.output(green, pin.LOW)
def event8(i):
	effect8.play(maxtime = 300)
	pin.output(right, pin.HIGH)
	time.sleep(0.3)
	pin.output(right, pin.LOW)

#SETTING UP INTERRUPT CALLS
pin.add_event_detect(s1, pin.FALLING, callback = event1, bouncetime = 500)
pin.add_event_detect(s2, pin.FALLING, callback = event2, bouncetime = 500)
pin.add_event_detect(s3, pin.FALLING, callback = event3, bouncetime = 500)
pin.add_event_detect(s4, pin.FALLING, callback = event4, bouncetime = 500)
pin.add_event_detect(s5, pin.FALLING, callback = event5, bouncetime = 500)
pin.add_event_detect(s6, pin.FALLING, callback = event6, bouncetime = 500)
pin.add_event_detect(s7, pin.FALLING, callback = event7, bouncetime = 500)
pin.add_event_detect(s8, pin.FALLING, callback = event8, bouncetime = 500)

time.sleep(1)
print("\n!!!Piano Ready!!!\n\n\n Exit with 'Enter(Return)' or Keyboard Interrupt.")

try:
    input()
    pin.cleanup()
    print ("Clean Exit. Have a nice day!")
except KeyboardInterrupt:
    print ("\nCode stopped by 'keyboard interrupt'. Have a nice day.")
    pin.cleanup()
