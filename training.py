from abilities import abilities
from dummy import Training_Dummy
import time

def training(player):
    view_stats(player)
    fight_dummy(player)

def view_stats(player):
    time.sleep(2)

    print(f"""
Your current stats are: 
Level: {player.level}
Health: {player.health}
Mana: {player.mana}
Potions: {player.potions}
""")
    
def fight_dummy(player):
    training_dummy = Training_Dummy("Training Dummy")
    print("Test your abilities on the training dummy.")
    print("All classes have a basic attack and 4 unique abilities.")

    num = 1
    for ability in abilities[player._weapon]:
        print(f"{num}: {ability}")
        num += 1
    

    training = True
    while training:
        choice_num = int(input("\nEnter the number. "))
        choice_str = abilities[player._weapon][choice_num - 1]
        print(f"\nYou use {player.__getattribute__(choice_str).__name__} on the {training_dummy.name}.")
        player.__getattribute__(choice_str)(training_dummy)
        
        continue_training = input("\nContinue training? [y/n] ")
        if continue_training == "n":
            training = False
