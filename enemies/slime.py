from .enemy import Enemy

class Slime(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.level = 3
        self.element = None
        self.abilities = {
            "bounce": {
                "damage multiplier": 0.5
            },
        }
    
    def bounce(self, target):
        self._use_ability("bounce", target)