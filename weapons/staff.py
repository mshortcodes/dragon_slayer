from weapons.base import Base

class Staff(Base):
    def __init__(self, name):
        super().__init__(name)
        self._weapon = "Staff"
        self._abilities = ["attack", "fireball", "freeze", "tornado", "flood"]
        self._mana_cost = {"fireball": 10, "freeze": 15, "tornado": 15, "flood": 15}
        self._damage_multiplier = {"fireball": 1.0, "freeze": 1.5, "tornado": 1.5, "flood": 1.5}

    def _use_ability(self, ability, target):
        if self.mana < self._mana_cost[ability]:
            return "Not enough mana."
        self.mana -= self._mana_cost[ability]
        damage = int(10 * self._damage_multiplier[ability])
        target.health -= damage
        print(f"The {target.name} takes {damage} damage and has {target.health} health remaining.")

    def fireball(self, target):
        self._use_ability("fireball", target)

    def freeze(self, target):
        self._use_ability("freeze", target)
    
    def tornado(self, target):
        self._use_ability("tornado", target)

    def flood(self, target):
        self._use_ability("flood", target)


