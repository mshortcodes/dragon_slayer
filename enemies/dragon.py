from .enemy import Enemy

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.element = "fire"
        self.abilities = {
            "Dragonbreath": {
                "damage multiplier": 5
            },
            "Wind Gust": {
                "damage multiplier": 3
            },
            "Tail Whip": {
                "damage multiplier": 2
            },
            "Claw": {
                "damage multiplier": 1
            }
        }