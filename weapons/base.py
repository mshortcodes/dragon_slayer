class Base:
    def __init__(self, name):
        self.level = 1
        self.health = 100
        self.mana = 100
        self.potions = 0
        self._name = name
        self._xp = 0

    def attack(self, target):
        dmg = 5
        target.health -= 5
        print(f"The {target.name} takes {dmg} damage has {target.health} health remaining.")