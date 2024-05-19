from weapons.base import Base

class Staff(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "fireball": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": "fire"
            },
            "freeze": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "tornado": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "flood": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }

    def fireball(self, target):
        self._use_ability("fireball", target)

    def freeze(self, target):
        self._use_ability("freeze", target)
    
    def tornado(self, target):
        self._use_ability("tornado", target)

    def flood(self, target):
        self._use_ability("flood", target)


