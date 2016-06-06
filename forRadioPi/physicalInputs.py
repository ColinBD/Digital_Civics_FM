# physicalInputs script written by Colin, Stuart and Helen for the purpose of out Technologies for Digital Civics module

import RPi.GPIO as GPIO
import subprocess
import pygame #used for audio playback
from time import sleep

#variables to hold current states
playing = False
stopped = False
ejectState = False
selected = 'none'

pygame.mixer.init() #initialise the audio player

try:
	#set-up Pi physical connectors
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(13, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(12, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)
	
	#create an infinite loop which looks for acticvity on the Pi's physical connectors
	while True:
		#print 'testing ' + str(GPIO.input(12)) + ' ' + str(GPIO.input(16)) + ' ' + str(GPIO.input(18)) + ' ' + str(GPIO.input(22))
		
		#check rotary switch position
		if GPIO.input(12) == 0: #knob position 1 so twitter selected
			if selected != 'twitter':
				print 'twitter selected'
				selected = 'twitter'
				pygame.mixer.music.stop() #ensure no other audio is playing
				# play audio file stating which input is selected 
				return_code = subprocess.call(["aplay", 'TwitterSelected.wav'])
				# if the screen is out put it back because we don't need it
				if ejectState == True:
					ejectState = False
					subprocess.call(['eject', '-t'])
		elif GPIO.input(16) == 0: #knob position 2 so special interest selected
			if selected != 'specialInterest':
				selected = 'specialInterest'
				print 'special interest selected'
				pygame.mixer.music.stop() #ensure no other audio is playing
				# play audio file stating which input is selected 
				return_code = subprocess.call(["aplay", 'SpecialInterestSelected.wav'])
				# if the screen is out put it back because we don't need it
				if ejectState == True:
					ejectState = False
					subprocess.call(['eject', '-t'])
		elif GPIO.input(18) == 0: #knob position 3 so facebook selected
			if selected != 'facebook':
				selected = 'facebook'
				print 'facebook selected'
				pygame.mixer.music.stop() #ensure no other audio is playing
				# play audio file stating which input is selected 
				return_code = subprocess.call(["aplay", 'FacebookSelected.wav'])
				# if the screen is out put it back because we don't need it
				if ejectState == True:
					ejectState = False
					subprocess.call(['eject', '-t'])
		else: #knob position 4 so instagram selected
			if selected != 'instagram':
				selected = 'instagram'
				pygame.mixer.music.stop() #ensure no other audio is playing
				print 'instagram selected'
				# play audio file stating which input is selected 
				return_code = subprocess.call(["aplay", 'InstagramSelected.wav'])
				# if the screen is retracted then eject it because we will need it
				if ejectState == False:
					ejectState = True
					subprocess.call(['eject'])
		
		#look for play button being pressed (on pin 7)
		if GPIO.input(7) == 0:
			#then play button was pressed
			if playing == False: # avoids multiple presses
				playing = True
				stopped = False
				print 'play button pressed'
				if selected == 'twitter':
					#play the latest tweets audio file
					pygame.mixer.music.load('tweets.wav')
					pygame.mixer.music.play()
				elif selected == 'specialInterest':
					#run the 'playSpecialInterest' script
					return_code = subprocess.call(["python", "playSpecialInterest.py"])
					pygame.mixer.music.load('special_interest_tweets.wav')
					pygame.mixer.music.play()
				elif selected == 'facebook':
					#run the 'playFacebook' script
					return_code = subprocess.call(["python", "playFacebook.py"])
				else:
					#run the 'playInstagram' script
					return_code = subprocess.call(["python", "playInstagram.py"])
				#once the audio output has completed change play and stop state variables to reflect this
				playing = False
				stopped = True
		
		#look for stop button being pressed (on pin 11)
		if GPIO.input(11) == 0:
			#then stop button was pressed
			print 'stop button pressed'
			#stop the audio
			pygame.mixer.music.stop()
		
		#look for eject screen button being pressed (on pin 13)
		if GPIO.input(13) == 0:
			#toggle eject variable state
			if ejectState == False:
				ejectState = True
				print 'screen will move out'
				subprocess.call(['eject'])
				sleep(0.5)
			else: 
				ejectState = False
				print 'screen will retract'
				subprocess.call(['eject', '-t'])
				sleep(0.5)
		
		sleep(0.05)

finally:
	GPIO.cleanup()
