from enemies.dummy import Training_Dummy
import time

def training(player):
    view_stats(player)
    training_dummy = create_dummy()
    print_abilities_info()
    print_abilities(player)
    ability_choice = get_ability_choice(player)
    fight_dummy(player, ability_choice, training_dummy)
    get_training_choice(player, ability_choice, training_dummy)

def view_stats(player):
    time.sleep(1)
    print(f"Your current stats are:\n")
    time.sleep(1)
    print(f"Health: {player.health}")
    print(f"Mana: {player.mana}")
    print(f"Potions: {player.potions}")
    time.sleep(1)
    
def create_dummy():
    training_dummy = Training_Dummy("Training Dummy")
    print(f"\nTest your abilities on the {training_dummy.name}.")
    time.sleep(1)
    return training_dummy

def print_abilities_info():
    print("All classes have a basic attack and 4 unique abilities.\n")
    time.sleep(1)

def print_abilities(player):
    for i, ability in enumerate(player.abilities):
        print(f"{i + 1}. {ability}")

def get_ability_choice(player):
    while True:
        try:
            time.sleep(1)
            choice_num = int(input("\nEnter the number. "))
            if choice_num < 1 or choice_num > len(player.abilities):
                print("The number must be between 1 and 5.")
                continue
            ability_choice = list(player.abilities.keys())[choice_num - 1]
            return ability_choice
        except ValueError:
            print("Input must be a number.")
            continue
        
def fight_dummy(player, ability_choice, training_dummy):
    time.sleep(1)
    player.use_ability(ability_choice, training_dummy)
    player.mana = 100
    time.sleep(1)
    training_dummy.invincible()
    time.sleep(1)
        
def get_training_choice(player, ability_choice, training_dummy):
    while True:
        continue_training = input("\nContinue training? [y/n] \n")
        if continue_training == "n":
            break
        elif continue_training == "y":
            print_abilities(player)
            ability_choice = get_ability_choice(player)
            fight_dummy(player, ability_choice, training_dummy)
        else:
            print("Enter y or n.")
            continue
