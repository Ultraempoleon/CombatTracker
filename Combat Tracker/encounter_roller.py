import random

class monster:
    def __init__(self, name, armor_class, hitdice_amount, hit_dice, hp_mod, attack1, attack2 = None):
        self.name = name
        self.armor_class = armor_class
        self.hitdice_amount = hitdice_amount
        self.hit_dice = hit_dice
        self.hp_mod = hp_mod
        self.attack1 = attack1
        self.attack2 = attack2

    def getName(self):
        print('Name: {}'.format(self.name))

    def display_info(self):
        self.getName()
        self.attack1.total_damage()
        self.attack2.total_damage()


class attack():
    def __init__(self, name,  to_hit, dmg_dice_amount, dmg_dice, dmg_mod, \
                dmg_type, dmg_dice2_amount=0, dmg_dice2=0, dmg_type2="",\
                dmg_mod2=0, recharge1 = False, recharge2 = False):
        self.name = name
        self.to_hit = to_hit
        self.dmg_dice_amount = dmg_dice_amount
        self.dmg_dice = dmg_dice
        self.dmg_mod = dmg_mod
        self.dmg_type = dmg_type
        self.dmg_dice2_amount = dmg_dice2_amount
        self.dmg_dice2 = dmg_dice2
        self.dmg_type2 = dmg_dice2
        self.dmg_type2 = dmg_type2
        self.dmg_mod2 = dmg_mod2


    #Calcs roll and damage dealt
    def total_damage(self):
        rolleddice = 0
        rolleddamage = 0

        roll_to_hit = random.randrange(1, 20) + self.to_hit
        while (rolleddice < self.dmg_dice_amount):
            rolleddamage += random.randrange(1, self.dmg_dice) + self.dmg_mod
            rolleddice += 1
        
        #if damage has 2 types
        if self.dmg_dice2 > 0:
            rolleddice = 0
            total_rolleddamage = rolleddamage
            while(rolleddice < self.dmg_dice2_amount):
                rolleddamage2 = random.randrange(1, self.dmg_dice2) + self.dmg_mod2
                total_rolleddamage += rolleddamage2
                rolleddice += 1
            
            #output if damage has 2 types
            print("{} : {} damage | {} {} and {} {}".format(roll_to_hit, #this print message is just long, weird formatting
                total_rolleddamage, rolleddamage, self.dmg_type, 
                rolleddamage2, self.dmg_type2))
                
        else:
            print("{} : {} {}".format(roll_to_hit, rolleddamage, self.dmg_type))

    def getName(self):
        print('Attack Name: {}'.format(self.name))

 


class rechargeAttack:
    def __init__(self, name, DC, DC_check, dmg_dice_amount, dmg_dice, dmg_type, range, shape, recharge = True):
        self.name = name
        self.DC = DC
        self.DC_check = DC_check
        self.dmg_dice_amount = dmg_dice_amount
        self.dmg_dice = dmg_dice
        self.dmg_type = dmg_type
        self.range = range
        self.shape = shape
        self.recharge = recharge


    def total_damage(self):
        rolleddice = 0
        rolleddamage = 0
        while (rolleddice < self.dmg_dice_amount):
            rolleddamage += random.randrange(1, self.dmg_dice)
            half = int(rolleddamage/2)
            rolleddice += 1

        print("Fail: {} {} Damage | Pass: {} {}".format(rolleddamage, self.dmg_type, half, self.dmg_type))

        self.recharge = False

    #1/3 change or recharging weapon
    def rechargeCheck(self):
        x = random.randrange(1, 3)
        if x == 3:
            self.recharge = True
        else:
            pass

    def getName(self):
        print('Attack Name: {}'.format(self.name))
            



def main():
    # HellHound_Bite = attack('Bite', 5, 1, 8, 3, 'piercing', 2, 6, 'fire', 0)
    # Fire_Breath = rechargeAttack('Fire Breath', 12, 'Dex', 6, 6, 'fire', '15ft', 'cone')
    # HellHound = monster('Hell Hound', 15, 7, 8, 14, HellHound_Bite, Fire_Breath)
    # HellHound.display_info()
    monsters = []
    monsteramount = int(input("Number of mons: "))
    x = 0
    while (x < monsteramount):
        HellHound_Bite = attack('Bite', 5, 1, 8, 3, 'piercing', 2, 6, 'fire', 0)
        Fire_Breath = rechargeAttack('Fire Breath', 12, 'Dex', 6, 6, 'fire', '15ft', 'cone')
        monsters.append(monster('Hell Hound', 15, 7, 8, 14, HellHound_Bite, Fire_Breath))
        x += 1
    
    for i in monsters:
        i.display_info()
    


if __name__=="__main__":
    main()