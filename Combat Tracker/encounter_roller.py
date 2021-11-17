import random

class attack:
    def __init__(self, to_hit, dmg_dice_amount, dmg_dice, dmg_mod, \
                dmg_type, dmg_dice2_amount=0, dmg_dice2=0, dmg_type2="",\
                dmg_mod2=0):

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

    def total_damage(self):
        roll_to_hit = random.randrange(1, 20) + self.to_hit
        rolleddamage = random.randrange(1, self.dmg_dice) + self.dmg_mod
        if self.dmg_dice2 > 0:
            rolleddamage += random.randrange(1, self.dmg_dice2) + self.dmg_mod2
        
        return roll_to_hit, rolleddamage


def main():
    newattack = attack(5, 1, 8, 3, 'piercing')
    roll_to_hit, rolled_damage = attack.total_damage(newattack)
    print("{} : {} {}".format(roll_to_hit, rolled_damage, newattack.dmg_type))


if __name__=="__main__":
    main()