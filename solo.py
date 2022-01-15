
import time
from os import system

# Clear screen and setups up new level name
def loading_screen(chapter_name = ""):
    system('clear')
    print_withpause("Loading.....................", 3)
    system('clear')
    print_withpause(chapter_name)

# Prints out dialogue or storyline with an optional pause
def print_withpause(sentence, timing=2):
    print(sentence)
    time.sleep(timing)  

# Introduce the game upon startup
def welcome_screen():  
    print_withpause("Welcome to 'Solo' a text based adventure game!")
    print_withpause("Solo will take you on a wild solo canoe trip down the Widowmaker River!")
    print_withpause("Do you have what it takes to traverse these deadly waters?", 3)
    print_withpause("Will you survive?", 3)
    print_withpause("Let's get started!", 3)
    loading_screen()

# Setup new player    
def player_setup():
    player = input("What is your player name? \n ")
    happy_phrase = input(" What's a phrase that you say when you're happy? \n ")
    sad_phrase = input("What's a phrase you say when something goes wrong? \n ")
    loading_screen()

def story_setup():
    loading_screen("Highway 11: 6 hours since the start of the trip")  

welcome_screen()
player_setup()
story_setup()
