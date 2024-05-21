from weapons.base import Base

class Shield(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "Shield Bash": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "Shield Throw": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "Shield Spin": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "Shield Crush": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }

