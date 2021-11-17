from classes import *
from functions import *
import collections


def main():
    monsters = []
    options = ['[0]: Add Monsters', '[1] Add Player', '[8] Run Count', '[9] End the game']
    menu_running = [True] #has to be in the form of a list to be modified by the function

    while (menu_running[0]):
        for i in options:
            print("{} ".format(i), end="")
    
        #grabs user input and then calls the function associated with what was picked
        option_input(monsters, options, menu_running)
        
        for i in monsters:
            if type(i) == monster:
                print("{} {} Ini: {}".format(i.name, i.number, i.intiative))
            if type(i) == customInput:
                print("{} Ini: {}".format(i.name, i.intiative))

if __name__=="__main__":
    main()