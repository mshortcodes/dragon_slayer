from base import Base

class Staff(Base):
    def __init__(self, name):
        super().__init__(name)
        self._weapon = "Staff"

    def fireball(self, target):
        dmg = 10
        if self.mana < 10:
            return "Not enough mana."
        self.mana -= 10
        target.health -= 10
        print(f"{target.name} takes {dmg} damage.")

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

