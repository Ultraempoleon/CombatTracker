from classes import *
from monsters import choosemonster
#Options Functions

#adds a new amount of monsters
def addmonsters(monsters):
    monsteramount = int(input("Number of mons: "))
    x = [True]
    while (x[0] == True):
        monstername = input('Monster Name: ')
        choosemonster(monstername, monsteramount, monsters, x)
        if x == False:
            break
        else:
            print("Your monsters was not found!")

    
    #sorts the current initiative count
    sortIntiative_count(monsters)    

#Adds new non monsters to the list (presumed players)
def addplayers(monsters):
    morePlayers = True
    print("Enter 0 to stop adding players")


    while morePlayers:
        name = input('Enter Player Name: ')
        if name == '0':
            break

        initiative = input("Initiative Roll: ")
        if initiative == '0':
            break
        
        monsters.append(customInput(name, int(initiative)))
        
        #sorts the current intiative count
        sortIntiative_count(monsters)

#Damage a monster
def damagemonster(monsters):
    
    try:
        monster_selected = int(input("Pick a monster on the initiative count: "))
        damage_dealt = int(input("Enter damage dealth: "))
    except ValueError:
        print("Error! Has to be a number\n")
    monsters[monster_selected].take_damage(damage_dealt)

#Run the turn
def runturn(monsters):
    
    for m in monsters:
        if (type(m) == monster) or (issubclass(type(m), monster)):
            m.turn()
        else:
            print("Nothing happened")
    pass

#Ends the menu loop
def endmenu(menu_running):
    menu_running[0] = False
    

#Option subfunctions

#Sorts the functions
def sortIntiative_count(monsters):
    monsters.sort(key=lambda x:x.intiative)



#Main functions

#asks user to pick an option then passes that input
def option_input(monsters, options, menu_running):
    try:
        option_picked = int(input('\nSelect Input: '))
        option_functions(monsters, option_picked, options, menu_running)
    except ValueError:
        print("Error! Has to be a number\n")

#prints the current intiative order
def display_initiative(monsters):
    print("\n\n\n")
    for i in monsters:
        if (type(i) == monster) or (issubclass(type(i), monster)):
            print("{} {} Ini: {} HP: {}".format(i.name, i.number, i.intiative, i.hp))
        elif type(i) == customInput:
            print("{} Ini: {}".format(i.name, i.intiative))
        else:
            print("Has no type")

#calls the function associated with what the user picked
def option_functions(monsters, user_choice, options, menu_running):
    if user_choice == 0:
        addmonsters(monsters)
    elif user_choice == 1:
        addplayers(monsters)
    elif user_choice == 2:
        damagemonster(monsters)
    elif user_choice == 8:
        runturn(monsters)
    elif user_choice == 9:
        endmenu(menu_running)
    else:
        Default

#passes if another number is chosen
def Default():
    print('Nothing Happened')