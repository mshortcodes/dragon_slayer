class Base:
    def __init__(self, name):
        self.level = 1
        self.health = 100
        self.mana = 100
        self.potions = 0
        self._name = name
        self._xp = 0

    def attack(self, target):
        target.health -= 5