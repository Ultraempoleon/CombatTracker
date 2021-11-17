from classes import *

def main():
    monsters = []
    monsteramount = int(input("Number of mons: "))
    x = 0
    while (x < monsteramount):
        HellHound_Bite = attack('Bite', 5, 1, 8, 3, 'piercing', 2, 6, 'fire', 0)
        Fire_Breath = rechargeAttack('Fire Breath', 12, 'Dex', 6, 6, 'fire', '15ft', 'cone')
        monsters.append(monster('Hell Hound', 15, 7, 8, 14, 3, HellHound_Bite, Fire_Breath))
        x += 1
    
    monsters.sort(key=lambda x:x.intiative)
    
    for i in monsters:
        i.display_info()
        print(i.intiative)




if __name__=="__main__":
    main()