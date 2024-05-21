from weapons.base import Base

class Spear(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "Thrust": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "Icicle": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "Spin": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "Spirit Spear": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "fire"
            }
        }