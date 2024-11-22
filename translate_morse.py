import RPi.GPIO as GPIO 
import time

from pygame import mixer 

light = 20


def set_up_GPIO():
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    GPIO.setup(light, GPIO.OUT) #set up light (#19) as output 
def set_up_music():
    mixer.init()
    mixer.music.set_volume(1.0) 

def main():
    set_up_GPIO()
    set_up_music()
    
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': ' '}
    message = input("Enter Message: ")
    message = message.upper()
    for ch in message:
        if ch in MORSE_CODE:
            code = MORSE_CODE[ch]
            for dot_dash in code:
                GPIO.output(light, GPIO.HIGH) #turn on light
                if dot_dash == '.':
                    mixer.music.load("morseshort.mp3")
                    mixer.music.play()
                    print("dot")
                elif dot_dash == '-':
                    mixer.music.load("morselong.mp3")
                    mixer.music.play()
                    print("dash")
                time.sleep(0.2) #delay between sounds
            time.sleep(0.5) #delay between letters
        elif ch == " ":
            time.sleep(1) #delay between a space and the next letter, to signfy the start of a new word
    GPIO.output(light, GPIO.LOW)  # keeps/turns light off if button is not pressed
    GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
