import RPi.GPIO as GPIO 
import time
import os
import sys

from pygame import mixer 


button_pin = 19 #save 19 (GPIO pin) as button_pin
light = 20 #save20 (GPIO pin)as light 
 #save the audio segment as song 

def set_up_GPIO():
    mixer.init()
    mixer.music.load("MK & Dom Dolla - Rhyme Dust.mp3")
    mixer.music.set_volume(1.0) 
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(light, GPIO.OUT) #set up light (#19) as output 
    GPIO.setup (button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Configure as input with pull-up resistor

def play_audio():
    mixer.music.play()
    
def main():       
    set_up_GPIO() #call function that sets up pins
    try:
        while True:
        # Check if the button is pressed
            if GPIO.input(button_pin) == GPIO.LOW: 
                GPIO.output(light, GPIO.HIGH) #turn on light
                print("audio playing") #print statement through terminal 
                play_audio() #call play audio function and use it on vairiabe audio_file
                time.sleep(1)  # Debounce delay
                while True:
                    if GPIO.input(button_pin) == GPIO.LOW:
                        print("play audio")
                        GPIO.output(light, GPIO.LOW)  # keeps/turns light off if button is not pressed
                        mixer.music.stop()
                        time.sleep(1)  # Debounce delay
                        break
 
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit() #when this error is cuaght exit the program
    finally:
        GPIO.output(light, GPIO.LOW) #turn off light when while loop is ended 
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__": #call and run main function 
    main()



