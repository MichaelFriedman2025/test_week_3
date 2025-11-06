import random

class Goblin:

    def __init__(self):
        self.name = "jo"
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        self.weapon = random.randint(1, 3)

        if self.weapon == 1:
            self.weapon = "knife"
        elif self.weapon == 2:
            self.weapon = "sword"
        else:
            self.weapon = "ax"

    def speak(self):
        return f"The goblin {self.name} angry."

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

