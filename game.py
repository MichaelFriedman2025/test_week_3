import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin

class Game:
    __bamboo = []

    @staticmethod
    def show_manu():
        answer = input("If you want to exit the game, enter the word 'exit'\n"
                       "else enter what do you want:\n")
        if answer == "exit":
            return False
        return True

    @staticmethod
    def create_player():
        return Player()

    @staticmethod
    def choose_random_monster():
        choosing = random.randint(1,2)
        if choosing == 1:
            monster =  Goblin()
        else:
            monster =  Orc()
        return monster

    @staticmethod
    def battle(player,monster,attack):
        dice_6 = Game.roll_dice(6)
        dice_20 = Game.roll_dice(20)
        if attack:
            res_attack = player.attack(monster, dice_6, dice_20)
        else:
            res_attack = monster.attack(player, dice_6, dice_20)
        return res_attack


    @staticmethod
    def roll_dice(sides):
        return random.randint(1,sides)


    def start(self):
        player = self.create_player()

        for cm in range(8):
            Game.__bamboo.append(self.choose_random_monster())

        monster = Game.__bamboo[-1]

        print(f"monster: {monster.name} ,type: {monster.type}, hp: {monster.hp}\n"
              f"player: {player.name}, hp: {player.hp}\n")

        player_rolling = self.roll_dice(6)
        monster_rolling = self.roll_dice(6)

        if player.speed + player_rolling >= monster.speed + monster_rolling:
            attack = True
            print(f"the {player.name} attacking\n")
        else:
            attack = False
            print(f"the {monster.name} attacking\n")

        while True:
            answer = self.show_manu()
            if not answer:
                break

            res_attack = self.battle(player,monster,attack)

            if res_attack:
                print(f"monster: {monster.name} ,type: {monster.type}, hp: {monster.hp}")
                print(f"player: {player.name}, hp: {player.hp}\n")
                print("The attacking completed\n")
                if attack:
                    if monster.hp <= 0:
                        if not Game.__bamboo:
                            print("you won all monster you finish the game, well don.")
                            break
                        else:
                            Game.__bamboo.pop()
                            monster = Game.__bamboo[-1]
                            print(f"the monster dead,"
                                  f" You have killed {8 - len(Game.__bamboo)} monsters so far. :)\n"
                                  f"You move to the next room.\n"
                                  f"monster: {monster.name} ,type: {monster.type}, hp: {monster.hp}\n"
                                  f"player: {player.name}, hp: {player.hp}\n")

                else:
                    if player.hp <= 0:
                        print("you dont have a life, you are dead :(")
                        break
            else:
                print("the attack missed\n")

            if attack:
                attack = False
                print(f"now torn {monster.name} to attacking")
                print(player.speak(),"\n")
            else:
                attack = True
                print(f"now torn {player.name} to attacking")
                print(monster.speak(),"\n")

