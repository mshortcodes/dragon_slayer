class Enemy:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.is_alive = True
    
    def _calc_damage(self, ability):
        damage = int(10 * self.abilities[ability]["damage multiplier"])
        return damage

    def _use_ability(self, ability, target):
        print(f"The {self.name} uses {ability}.")
        damage = self._calc_damage(ability)
        target.health -= damage
        print(f"You take {damage} damage and have {target.health} health remaining.")
