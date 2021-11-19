import random

#Basic monsters with 1 or 2 attacks
class monster:
    def __init__(self, name, armor_class, hitdice_amount, hit_dice, hp_mod, dex_mod, attack1, attack2 = None, number = 1):
        self.name = name
        self.armor_class = armor_class
        self.hitdice_amount = hitdice_amount
        self.hit_dice = hit_dice
        self.hp_mod = hp_mod
        self.dex_mod = dex_mod
        self.attack1 = attack1
        self.attack2 = attack2
        self.number = number #number exists for multiple monsters with the same name, differntiates them
        self.intiative = random.randrange(1, 20) + dex_mod
        self.hp = ((random.randrange(1, hit_dice) * hitdice_amount) + hp_mod)


    def newnumber(self, newnumber):
        self.number = newnumber

    def display_info(self):
        self.getName()
        #self.attack1.total_damage()

    def get_initiative_roll(self):
        print(self.intiative)

    def take_damage(self, damage_taken):
        self.hp -= damage_taken

#Monsters with a recharge weapon
class rechargeMonster(monster):
    def __init__(self, name, armor_class, hitdice_amount, hit_dice, hp_mod, dex_mod, attack1, attack2=None, number=1):
        super().__init__(name, armor_class, hitdice_amount, hit_dice, hp_mod, dex_mod, attack1, attack2, number=number)

    def turn(self):
        if type(self.attack2) == rechargeAttack:
            if self.attack2.recharge == True:
                self.attack2.attack()
            else:
                self.attack2.rechargeCheck()
                self.attack1.attack()

#Presumed a new player but it can be anything
class customInput():
    def __init__(self, name, intiative):
        self.name = name
        self.intiative = intiative

    def change_roll(self):
        self.intiative = input('New Roll: ')

    def getName(self):
        print('Attack Name: {}'.format(self.name))
            
#Normal Attack
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
    def attack(self):
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
            print("Uses {} - {} : {} damage | {} {} and {} {}".format(self.name, roll_to_hit, #this print message is just long, weird formatting
                total_rolleddamage, rolleddamage, self.dmg_type, 
                rolleddamage2, self.dmg_type2))
                
        else:
            print("Uses {} - {} : {} {}".format(self.name, roll_to_hit, rolleddamage, self.dmg_type))

    def getName(self):
        print('Attack Name: {}'.format(self.name))

#Rechargable Attack
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

    #uses recharge attack
    def attack(self):
        rolleddice = 0
        rolleddamage = 0
        while (rolleddice < self.dmg_dice_amount):
            rolleddamage += random.randrange(1, self.dmg_dice)
            half = int(rolleddamage/2)
            rolleddice += 1

        print("Fail: {} {} Damage | Pass: {} {}".format(rolleddamage, self.dmg_type, half, self.dmg_type))

        self.recharge = False

    #1/3 chance of recharging weapon
    def rechargeCheck(self):
        check = random.randrange(3)
        if check == 2:
            self.recharge = True
