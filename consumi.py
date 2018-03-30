#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import pigpio

INPUT_PIN = 11 #numero fisico sulla board
timeStarted = False


#callback chiamata dal lampeggio del led
def manageTime():
	global timeStarted
	
	if timeStarted == False:
		start = time.time()
		timeStarted = True
	else:
		timeBetweenTwoflash = time.time() - start #
		consumoWatt = 3600 / timeBetweenTwoflash
		return consumoWatt




#Risponde in tempo reale attivando il GPIO al lampeggio
def realTime():
	try:
		#setup callback GPIO
		GPIO.add_event_detect(INPUT_PIN, GPIO.RISING)
		GPIO.add_event_callback(4, manageTime)

		#avvia il monitoraggi in tempo reale contando i secondi che passano tra due lampeggi
		manageTime()
	except Exception, e:
		print('Exception in realTime method: ',e)


def consumoMedio():




try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	realTime()



except Exception, e:
	print('Exception in main: ',e)