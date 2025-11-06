import random

class Player:

    def __init__(self):
        self.name = "michael"
        self.hp = 50
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.armor_rating = random.randint(5,15)
        self.profession = random.randint(1,2)

        if self.profession == 1:
            self.profession = "fighter"
            self.power += 2
        else:
            self.profession = "cure"
            self.hp += 10

    def speak(self):
        return f"{self.name} Afraid?"

    def attack(self,monster,dice_6,dice_20):
        checking_attack = self.speed + dice_20
        if checking_attack > monster.armor_rating:
            monster.hp -= dice_6 + self.power
            return monster
        else:
            return False




