from weapons.base import Base

class Bow(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "Power Shot": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "Ice Arrow": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "Fire Arrow": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "fire"
            },
            "Snipe": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }
