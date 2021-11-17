import random
        
class attack:
    def __init__(self, damage):
        self.damage = damage
    
    def dealdamage(self):
        newdamage = self.damage + 5
        return newdamage

def main():
    newattack = attack(5)
    newdamage = newattack.dealdamage()
    print(newdamage)

if __name__=="__main__":
    main()