from weapons.base import Base

class Shield(Base):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "attack": {
                "mana cost": 0,
                "damage multiplier": 0.5,
                "element": None
            },
            "shield bash": {
                "mana cost": 10,
                "damage multiplier": 1.0,
                "element": None
            },
            "shield throw": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "shield spin": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            },
            "shield crush": {
                "mana cost": 15,
                "damage multiplier": 1.5,
                "element": None
            }
        }

    def shield_bash(self, target):
        self._use_ability("shield bash", target)

    def shield_throw(self, target):
        self._use_ability("shield throw", target)
    
    def shield_spin(self, target):
        self._use_ability("shield spin", target)

    def shield_crush(self, target):
        self._use_ability("shield crush", target)


