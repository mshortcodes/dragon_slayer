import time

class Enemy:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.is_alive = self.health > 0

    def use_ability(self, ability, target):
        time.sleep(1)
        print(f"{self.name} uses {ability} on you.")
        damage = self._calc_damage(ability)
        if target.health <= damage:
            time.sleep(1)
            print(f"You take {target.health} damage and have {target.health - target.health} health remaining.\n")
            target.health -= target.health
            target.is_alive = target.health > 0
            
        else:
            time.sleep(1)
            target.health -= damage
            print(f"You take {damage} damage and have {target.health} health remaining.\n")
    
    def _calc_damage(self, ability):
        damage = int(10 * self.abilities[ability]["damage multiplier"])
        return damage