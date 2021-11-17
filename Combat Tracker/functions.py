from classes import *

#Options Functions

#adds a new amount of monsters
def addmonsters(monsters):
    monsteramount = int(input("Number of mons: "))
    x = 0
    while (x < monsteramount):
        HellHound_Bite = attack('Bite', 5, 1, 8, 3, 'piercing', 2, 6, 'fire', 0)
        Fire_Breath = rechargeAttack('Fire Breath', 12, 'Dex', 6, 6, 'fire', '15ft', 'cone')
        monsters.append(monster('Hell Hound', 15, 7, 8, 14, 3, HellHound_Bite, Fire_Breath, x+1))
        x += 1
    
    #sorts the current initiative count
    sortIntiative_count(monsters)    

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

def endmenu(menu_running):
    menu_running[0] = False
    

#Option subfunctions
def sortIntiative_count(monsters):
    monsters.sort(key=lambda x:x.intiative)



#Main functions

#asks user to pick an option then passes that input
def option_input(monsters, options, menu_running):
    option_picked = int(input('\nSelect Input: '))
    option_functions(monsters, option_picked, options, menu_running)

#calls the function associated with what the user picked
def option_functions(monsters, user_choice, options, menu_running):
    if user_choice == 0:
        addmonsters(monsters)
    elif user_choice == 1:
        addplayers(monsters)
    elif user_choice == 9:
        endmenu(menu_running)
    else:
        Default

def Default():
    print('Nothing Happened')