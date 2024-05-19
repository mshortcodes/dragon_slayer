from weapons.base import Base

class Bow(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "power shot": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "ice arrow": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "fire arrow": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "fire"
            },
            "snipe": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }

    def power_shot(self, target):
        self._use_ability("power shot", target)

    def ice_arrow(self, target):
        self._use_ability("ice arrow", target)
    
    def fire_arrow(self, target):
        self._use_ability("fire arrow", target)

    def snipe(self, target):
        self._use_ability("snipe", target)


