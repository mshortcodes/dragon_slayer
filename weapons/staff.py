from weapons.base import Base

class Staff(Base):
    def __init__(self, name):
        super().__init__(name)
        self._weapon = "Staff"
        self._abilities = ["attack", "fireball", "freeze", "tornado", "flood"]

    def fireball(self, target):
        dmg = 10
        if self.mana < 10:
            return "Not enough mana."
        self.mana -= 10
        target.health -= 10
        print(f"The {target.name} takes {dmg} damage has {target.health} health remaining.")

    def freeze(self, target):
        dmg = 15
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15
        print(f"The {target.name} takes {dmg} damage and has {target.health} health remaining.")
    
    def tornado(self, target):
        dmg = 15
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15
        print(f"The {target.name} takes {dmg} damage has {target.health} health remaining.")


    def flood(self, target):
        dmg = 15
        if self.mana < 15:
            return "Not enough mana."
        self.mana -= 15
        target.health -= 15
        print(f"The {target.name} takes {dmg} damage has {target.health} health remaining.")

