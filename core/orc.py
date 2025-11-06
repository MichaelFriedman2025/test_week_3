import random

class Orc:

    def __init__(self):
        self.name = "bob"
        self.hp = 50
        self.type = "orc"
        self.speed  = random.randint(0,5)
        self.power = random.randint(10,15)
        self.armor_rating = random.randint(2,8)
        self.weapon = random.randint(1,3)

        if self.weapon == 1:
            self.weapon = "knife"
        elif self.weapon == 2:
            self.weapon = "sword"
        else:
            self.weapon = "ax"

    def speak(self):
        return f"The orc {self.name} angry."

    def attack(self, player, dice_6, dice_20):
        checking_attack = self.speed + dice_20
        if checking_attack > player.armor_rating:
            damage = dice_6 + self.power
            if self.weapon == "knife":
                damage *= 0.5
            elif self.weapon == "ax":
                damage *= 1.5

            player.hp -= damage
            return player
        else:
            return False
