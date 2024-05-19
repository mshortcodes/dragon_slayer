from enemies.dummy import Training_Dummy
import time

def training(player):
    view_stats(player)
    training_dummy = create_dummy()
    print_abilities(player)
    ability_choice = get_ability_choice(player)
    fight_dummy(player, training_dummy, ability_choice)
    get_training_choice(player, training_dummy, ability_choice)

def view_stats(player):
    time.sleep(1)

    print(f"""
Your current stats are: 
Level: {player.level}
Health: {player.health}
Mana: {player.mana}
Potions: {player.potions}
""")
    
def create_dummy():
    training_dummy = Training_Dummy("training dummy")
    print(f"Test your abilities on the {training_dummy.name}.")
    return training_dummy

def print_abilities(player):
    print("All classes have a basic attack and 4 unique abilities.")
    for i in range(5):
        print(f"{i + 1}: {player._abilities[i]}")

def get_ability_choice(player):
    while True:
        try:
            choice_num = int(input("\nEnter the number. "))
            if choice_num < 1 or choice_num > 5:
                print("The number must be between 1 and 5.")
                continue
            ability_choice = player._abilities[choice_num - 1]
            return ability_choice
        except ValueError:
            print("Input must be a number.")
            continue
        
def fight_dummy(player, training_dummy, ability_choice):
    print(f"\nYou use {ability_choice} on the {training_dummy.name}.")
    time.sleep(1)
    player.__getattribute__(ability_choice)(training_dummy)
    time.sleep(1)
    training_dummy.invincible()
    time.sleep(1)
        
def get_training_choice(player, training_dummy, ability_choice):
    while True:
        continue_training = input("\nContinue training? [y/n] ")
        if continue_training == "n":
            break
        elif continue_training == "y":
            print_abilities(player)
            ability_choice = get_ability_choice(player)
            fight_dummy(player, training_dummy, ability_choice)
        else:
            print("Enter y or n.")
            continue