import time
import os
from playsound import playsound

def spooky_message():
    print("You feel a chill down your spine...")
    time.sleep(2)
    print("A ghostly whisper says, 'Vampires are real and they can code...'")
    time.sleep(2)
    print("Suddenly, you hear a creepy sound...")

def play_spooky_sound():
    # Make sure you have a spooky sound file in the same directory as this script
    playsound('spooky_sound.mp3')

if __name__ == "__main__":
    spooky_message()
    play_spooky_sound()
