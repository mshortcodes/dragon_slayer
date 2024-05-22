from .enemy import Enemy

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.element = "fire"
        self.abilities = {
            "Dragonbreath": {
                "damage multiplier": 5,
                "chance": 0.1
            },
            "Wind Gust": {
                "damage multiplier": 3,
                "chance": 0.2
            },
            "Tail Whip": {
                "damage multiplier": 2,
                "chance": 0.3
            },
            "Claw": {
                "damage multiplier": 1,
                "chance": 0.4
            }
        }