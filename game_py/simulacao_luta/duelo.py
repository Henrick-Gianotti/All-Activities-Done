from simulacao import *
import os
import time
import random

call_enemy = enemy()
call_attack = attack()

class duel:
    def __init__(self):
        self.t_enemy = []
        #self.select_enemy = None

    def start(self):
        self.t_enemy = copy.deepcopy(call_enemy.list_enemies())
        #self.choose_enemy = copy.deepcopy(call_enemy.list_enemies())
        #self.t_enemy = random.randint(0, len(self.choose_enemy) - 1)
        os.system('cls')
        print("You see your enemy appearing in your front...\n")
        time.sleep(2)
        
        action=int(0)
        action=int(input("Choice your action\n\n1-Weak-attack\n2-Medium-attack\n3-Strong-attack\n4-Do nothing\n5-Give up\n"))
        while True:
            if (action == 1):
                self.t_enemy[0][1] -= call_attack.weak_attack()
                if (self.t_enemy[0][1] < 1):
                    os.system('cls')
                    print(f"The {self.t_enemy[0]} has been defeated\n")
                    time.sleep(3)
                    os.system('cls')
                    break
                os.system('cls')
                print(f"The {self.t_enemy[0][0]} received 30 damage and have {self.t_enemy[0][1]} points\n")
                
            elif (action == 2):
                self.t_enemy[0][1] = self.t_enemy[0][1] - call_attack.normal_attack()
                if (self.t_enemy[0][1] < 1):
                    os.system('cls')
                    print(f"The {self.t_enemy[0][0]} has been defeated\n")
                    time.sleep(3)
                    os.system('cls')
                    break
                os.system('cls')
                print(f"The {self.t_enemy[0][0]} received 30 damage and have {self.t_enemy[0][1]} points\n")
                
            elif (action == 3):
                self.t_enemy[0][1] = self.t_enemy[0][1] - call_attack.strong_attack()
                if (self.t_enemy[0][1] < 1):
                    os.system('cls')
                    print(f"The {self.t_enemy[0][0]} has been defeated\n")
                    time.sleep(3)
                    os.system('cls')
                    break
                os.system('cls')
                print(f"The {self.t_enemy[0][0]} received 30 damage and have {self.t_enemy[0][1]} points\n")
                
            elif (action == 4):
                os.system('cls')
                print("You do nothing")
                time.sleep(3)
                os.system('cls')
            elif (action == 5):
                os.system('cls')
                print("Ending the simulation...")
                time.sleep(3)
                os.system('cls')
                break
            else:
                print("You insert a wrong value!\n\n")

            action=int(input("Choice your next action\n\n1-Weak-attack\n2-Medium-attack\n3-Strong-attack\n4-Do nothing\n5-Give up\n"))

