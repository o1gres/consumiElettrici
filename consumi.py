#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import pigpio
import threading

INPUT_PIN = 11 #numero fisico sulla board
timeStarted = False
numeroLampeggi = 0


#callback chiamata dal lampeggio del led
def manageTime():
	try:
		global timeStarted
		global numeroLampeggi

		numeroLampeggi += 1
		
		if timeStarted == False:
			start = time.time()
			timeStarted = True
		else:
			timeBetweenTwoflash = time.time() - start #
			consumoWatt = 3600 / timeBetweenTwoflash
			return consumoWatt

	except Exception, e:
		print('Exception in manageTime method: ',e)




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
		global numeroLampeggi

		threading.Timer(3600.0, timer).start()

	except Exception,e:
		print('Errore nel conteggio del numero dei lampeggi: ', e)




#MAIN
try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	realTime() #controllo consumi real time

	consumoMedio() #controllo dei consumi medi (E' un thread asincrono)



except Exception, e:
	print('Exception in main: ',e)