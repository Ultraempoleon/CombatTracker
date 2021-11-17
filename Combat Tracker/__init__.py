from classes import *
from functions import *


def main():
    monsters = []
    options = ['[0] Add Monsters', '[1] Add Player', '[8] Run the turn', '[9] End the game']
    menu_running = [True] #has to be in the form of a list to be modified by the function

    while (menu_running[0]):
        print('\n')
        for i in options:
            print("{} ".format(i), end="")
    
        #grabs user input and then calls the function associated with what was picked
        option_input(monsters, options, menu_running)
        display_initiative(monsters)

if __name__=="__main__":
    main()