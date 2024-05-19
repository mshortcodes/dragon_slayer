from weapons.base import Base

class Spear(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "thrust": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "icicle": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "spin": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "spirit spear": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "fire"
            }
        }

    def thrust(self, target):
        self._use_ability("thrust", target)

    def icicle(self, target):
        self._use_ability("icicle", target)
    
    def spin(self, target):
        self._use_ability("spin", target)

    def spirit_spear(self, target):
        self._use_ability("spirit spear", target)


