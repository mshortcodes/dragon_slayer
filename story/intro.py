from weapons.staff import Staff
from weapons.bow import Bow
from weapons.shield import Shield
from weapons.spear import Spear
import time

def intro():
    print_intro_message()
    player_name = get_player_name()
    print_instructions(player_name)
    weapons = print_weapon_choices()
    weapon_choice = get_weapon_choice(weapons)
    player = create_player(player_name, weapon_choice)
    return player
  
def print_intro_message():
    print("\n--- Welcome to Dragon Slayer! ---")
    time.sleep(1)
    print("\nThe kingdom of Dragonia, your home, and dragons were once at peace until the Great War.")
    time.sleep(1)
    print("You escaped to a neighboring kingdom to find refuge from the last surviving dragon, Oolong.")
    time.sleep(1)
    print("Many have tried to defeat him, but all have failed.")
    time.sleep(1)
    print("It is up to you become the hero of this world, the Dragon Slayer!\n")
    time.sleep(1)

def get_player_name():
    print("All heroes need a name.")
    time.sleep(1)
    return input("What is your name? ")

def print_instructions(player_name):
    time.sleep(1)
    print(f"\nGreetings, {player_name}!")
    time.sleep(1)
    print("You must choose a weapon, train, find the Dragon Ring, and defeat the dragon.\n")
    time.sleep(1)

def print_weapon_choices():
    weapons = ["Bow", "Shield", "Staff", "Spear"]
    for i, weapon in enumerate(weapons):
        print(f"{i + 1}. {weapon}")
    return weapons

def get_weapon_choice(weapons):
    while True:
        try:
            time.sleep(1)
            choice_num = int(input("\nEnter the number. \n"))
            if choice_num < 1 or choice_num > 4:
               print("The number must be between 1 and 4.")
               continue
            weapon_choice = weapons[choice_num - 1]
            print(f"\nYou have chosen the {weapon_choice}.")
            return weapon_choice
        except ValueError:
            print("The input must be a number.")

def create_player(player_name, weapon_choice):
    if weapon_choice == "Staff":
        player = Staff(player_name)
    elif weapon_choice == "Bow":
        player = Bow(player_name)
    elif weapon_choice == "Shield":
        player = Shield(player_name)
    elif weapon_choice == "Spear":
        player = Spear(player_name)
    return player