import copy

class attack:
    def weak_attack(self):
        return 10

    def normal_attack(self):
        return 20
        
    def strong_attack(self):
        return 30
        
class enemy:
    def __init__(self):
        self.enemies = []
        
    def list_enemies(self):
        self.enemies = [
            ["Mimic",
            100, #point-life
            40 #gold
            ], 
            ["Slime",
            100,
            10
            ]
        ]
        return self.enemies
        
    def clone(self):   
        tempory_enemy = copy.deepcopy(self.enemies)
        return tempory_enemy





