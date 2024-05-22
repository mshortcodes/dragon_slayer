import time

class Base:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.potions = 0
        self.has_dragon_ring = False
        self.is_alive = self.health > 0

    def use_ability(self, ability, target):
            mana_cost = self._calc_mana_cost(ability)
            if self.mana < mana_cost:
                print("Not enough mana.")
                return
            print(f"\nYou use {ability} on {target.name} for {mana_cost} mana.")
            time.sleep(1)
            damage = self._calc_damage(ability, target)
            if target.health <= damage:
                print(f"{target.name} takes {target.health} damage and has {target.health - target.health} health remaining.\n")
                target.health -= target.health
                target.is_alive = target.health > 0
            else:
                target.health -= damage
                print(f"{target.name} takes {damage} damage and has {target.health} health remaining.\n")

    def use_potion(self):
        print("Checking for potions...")
        time.sleep(2)
        if self.potions:
            print(f"Drinking the potion...")
            time.sleep(2)
            self.health += 50
            self.mana += 50
            self.is_alive = self.health > 0
            print(f"You recover 50 health and 50 mana.\n")
        else:
            print("No potions found.\n")

    def _calc_damage(self, ability, target):
        damage = int(10 * self.abilities[ability]["damage multiplier"])
        if self._is_weak_to(ability, target):
            time.sleep(1)
            print(f"{target.name} is weak to {self.abilities[ability]["element"]}!")
            damage += self._calc_bonus_damage(ability)
        elif self._is_strong_to(ability, target):
            time.sleep(1)
            print(f"{target.name} is strong to {self.abilities[ability]["element"]}!")
            damage -= self._calc_bonus_damage(ability)
        return damage

    def _calc_mana_cost(self, ability):
        mana_cost = self.abilities[ability]["mana cost"]
        self.mana -= mana_cost
        return mana_cost
    
    def _calc_bonus_damage(self, ability):
        bonus_damage = int(5 * self.abilities[ability]["damage multiplier"])
        return bonus_damage
    
    def _is_weak_to(self, ability, target):
        element = self.abilities[ability]["element"]
        if not element:
            return False
        if element == "fire" and target.element == "ice":
            return True
        elif element == "ice" and target.element == "fire":
            return True
        
    def _is_strong_to(self, ability, target):
        element = self.abilities[ability]["element"]
        if not element:
            return False
        if element == "fire" and target.element == "fire":
            return True
        elif element == "ice" and target.element == "ice":
            return True
         
    