import random

class monster:
    def __init__(self, name, armor_class, hitdice_amount, hit_dice, hp_mod):
        self.name = name
        self.armor_class = armor_class
        self.hitdice_amount = hitdice_amount
        self.hit_dice = hit_dice
        self.hp_mod = hp_mod


class attack():
    def __init__(self, to_hit, dmg_dice_amount, dmg_dice, dmg_mod, \
                dmg_type, dmg_dice2_amount=0, dmg_dice2=0, dmg_type2="",\
                dmg_mod2=0, recharge1 = False, recharge2 = False):

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
        roll_to_hit = random.randrange(1, 20) + self.to_hit
        rolleddamage = random.randrange(1, self.dmg_dice) + self.dmg_mod


        if self.dmg_dice2 > 0:
            rolleddamage2 = random.randrange(1, self.dmg_dice2) + self.dmg_mod2
            total_rolleddamage = rolleddamage2 + rolleddamage
            print("{} : {} damage | {} {} and {} {}".format(roll_to_hit, 
                total_rolleddamage, rolleddamage, self.dmg_type, 
                rolleddamage2, self.dmg_type2))    
        else:
            print("{} : {} {}".format(roll_to_hit, rolleddamage, self.dmg_type))


def main():
    hellhound = monster('Hell Hound', 15, 7, 8, 14)
    newattack = attack(5, 1, 8, 3, 'piercing', 2, 6, 'fire')
    attack.total_damage(newattack)
    

if __name__=="__main__":
    main()