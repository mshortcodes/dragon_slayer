class Base:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 100
        self.potions = 0

    def attack(self, target):
        target.health -= 5

class Mage(Base):
    def __init__(self, name):
        super().__init__(name)

    def fireball(self, target):
        if self.mana < 10:
            return "Not enough mana."
        self.mana -= 10
        target.health -= 10

    def freeze(self, target):
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15
    
    def tornado(self, target):
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15

    def flood(self, target):
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15

