from enemies.slime import Slime
from story.training import print_abilities
from story.training import get_ability_choice

def leveling(player):
    print_instructions(player)
    print_fight_sleep_choices()
    choice = get_fight_sleep_choice()
    handle_fight_sleep_choice(choice, player)
    create_slime()
    print_abilities(player)
    get_ability_choice(player)

def print_instructions(player):
    print(f"\n{player.name}, you must now level up by fighting enemies in the field. You can only fight the dragon once you are level 10. \n")

def print_fight_sleep_choices():
    choices = ["Travel outside and fight enemies.", "Sleep and recover full health."]
    for i in range(2):
        print(f"{i + 1}: {choices[i]}")

def get_fight_sleep_choice():
    while True:
        try:
            choice_num = int(input("\nEnter the number. "))
            if choice_num < 1 or choice_num > 2:
                print("The number must be between 1 and 2.")
                continue
            return choice_num
        except ValueError:
            print("The input must be a number.")

def handle_fight_sleep_choice(choice, player):
    if choice == 1:
        print("\nTraveling to the fields...")
    elif choice == 2:
        player.sleep()
        print("\nTraveling to the fields...")

def create_slime():
    slime = Slime("slime")
    print(f"You see a {slime.name} sleeping near a tree. Kill it to proceed.\n")
    return slime
            