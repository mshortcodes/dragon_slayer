from weapons.base import Base

class Staff(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "Fireball": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": "fire"
            },
            "Freeze": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": "ice"
            },
            "Tornado": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "Flood": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }
