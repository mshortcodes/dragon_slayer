from .enemy import Enemy

class Training_Dummy(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 9999
        self.element = None
    
    def invincible(self):
        self.health = 9999
        print(f"The {self.name} uses {self.invincible.__name__.capitalize()} and heals to {self.health} health.")