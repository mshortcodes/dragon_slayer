from story.training import print_abilities, get_ability_choice
from enemies.dragon import Dragon
import random, time

def battle(player):
    get_fight_dragon_choice()
    print_teleport()
    dragon = create_dragon()
    print_dragon_scene(player, dragon)
    fight_dragon(player, dragon)
    won = determine_won(player)
    if won:
        print_ending(player)

def get_fight_dragon_choice():
    while True:
        time.sleep(1)
        choice = input("\nAre you ready to fight the dragon? [y/n] ")
        if choice == "y":
            return
        elif choice == "n":
            print("You must slay the dragon to beat the game.")
        else:
            print("Enter y or n.") 

def print_teleport():
    time.sleep(1)
    print("\nYou put on the Dragon Ring and get sucked into a portal.")
    time.sleep(1)
    print("Teleporting...")
    time.sleep(2)

def create_dragon():
    dragon = Dragon("Oolong")
    return dragon

def print_dragon_scene(player, dragon):
    print("\n=== Dragon Fight ===")
    print(f"I am {dragon.name}. You will regret challenging me, {player.name}.\n")

def get_dragon_ability(dragon):
    abilities = list(dragon.abilities.keys())
    chances = [dragon.abilities[ability]["chance"] for ability in abilities]
    dragon_ability = random.choices(abilities, weights=chances, k=1)[0]
    return dragon_ability

def fight_dragon(player, dragon):
    while player.is_alive and dragon.is_alive:
        time.sleep(1)
        print_abilities(player)
        player_ability = get_ability_choice(player)
        dragon_ability = get_dragon_ability(dragon)
        player.use_ability(player_ability, dragon)
        if dragon.is_alive:
            dragon.use_ability(dragon_ability, player)
        use_potion(player)

def use_potion(player):
    if not player.is_alive:
        time.sleep(1)
        player.use_potion()
        time.sleep(1)

def determine_won(player):
    time.sleep(1)
    if player.is_alive:
        print("You have slayed the dragon!\n")
        return True
    else:
        print("You have fallen.")
        time.sleep(1)
        print("\n=== Game Over ===\n")
        return False

def print_ending(player):
    time.sleep(1)
    print(f"Dragon Slayer {player.name}, you have successfully defeated Oolong.")
    time.sleep(1)
    print("You can return home to Dragonia and begin rebuilding. The kingdom is in your debt.")
    time.sleep(1)
    print("\n=== You beat the game! ===\n")