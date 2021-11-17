class Weapon:
    def __init__(self, weapon_name, weapon_damage):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage

    def display_weapon_name(self):
        print('Weapon Name: %s' %self.weapon_name)


class Person:

    def __init__(self, person_name, health, ranged_weapon):
        self.person_name = person_name
        self.health = health
        self.weapon = ranged_weapon

    def display_person_info(self):
        print('Name: %s' %self.person_name)
        self.weapon.display_weapon_name()
        #print('Ranged Weapon :%s' %Weapon.display_weapon_name)

def ranged_attack(self, ranged_weapon, target):
    target.health -=ranged_weapon.weapon_damage
    print("Weapon: %s" %ranged_weapon.weapon_name)
    print(target.person_name + "'s Health: "+str(target.health))

pistol = Weapon("Pistol", 40)
bob = Person("Bob", 100, pistol)

bob.display_person_info()