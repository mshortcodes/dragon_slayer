from enemies.dummy import Training_Dummy
import time

def training(player):
    view_stats(player)
    fight_dummy(player)

def view_stats(player):
    time.sleep(1)

    print(f"""
Your current stats are: 
Level: {player.level}
Health: {player.health}
Mana: {player.mana}
Potions: {player.potions}
""")
    
def fight_dummy(player):
    training_dummy = Training_Dummy("training dummy")
    print("Test your abilities on the training dummy.")
    print("All classes have a basic attack and 4 unique abilities.")

    # list ability choices
    for i in range(5):
        print(f"{i + 1}: {player._abilities[i]}")

    # prompt user to choose ability
    training = True
    while training:
        try:
            choice_num = int(input("\nEnter the number. "))
            if choice_num < 1 or choice_num > 5:
                print("The number must be between 1 and 5.")
                continue
        except ValueError:
            print("Input must be a number.")
            continue
        
        choice_str = player._abilities[choice_num - 1]

        # combat
        print(f"\nYou use {choice_str} on the {training_dummy.name}.")
        time.sleep(1)
        player.__getattribute__(choice_str)(training_dummy)
        time.sleep(1)
        training_dummy.invincible()
        time.sleep(1)
        
        # prompt user to continue training
        while True:
            continue_training = input("\nContinue training? [y/n] ")
            if continue_training == "n":
                training = False
                break
            elif continue_training == "y":
                break
            else:
                continue