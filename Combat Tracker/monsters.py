from functions import *
def choosemonster(monstername, monsteramount, monsters, monsterfound):
    if monstername == "Hell Hound":
        HellHoundMaker(monsteramount, monsters, monsterfound)
    


def HellHoundMaker(monsteramount, monsters, monsterfound):
    x = 0
    while (x < monsteramount):
        HellHound_Bite = attack('Bite', 5, 1, 8, 3, 'piercing', 2, 6, 'fire', 0)
        Fire_Breath = rechargeAttack('Fire Breath', 12, 'Dex', 6, 6, 'fire', '15ft', 'cone')
        monsters.append(rechargeMonster('Hell Hound', 15, 7, 8, 14, 3, HellHound_Bite, Fire_Breath, x+1))
        x += 1
    monsterfound[0] = False
