from weapons.staff import Staff
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
    print("--- Welcome to Dragon Slayer! ---")
    print("\nThe kingdom of Dragonia, your home, and dragons were once at peace until the Great War. \nYou escaped to a neighboring kingdom to find refuge from the last surviving dragon, Oolong. \nMany have tried to defeat him, but all have failed. \nIt is up to you to train and become the hero of this world, the Dragon Slayer!\n")

def get_player_name():
    print("All heroes need a name.")
    return input("What is your name? ")

def print_instructions(player_name):
    print(f"\nGreetings, {player_name}!")
    print("You must choose a weapon, train, and defeat the dragon.\n")

def print_weapon_choices():
    weapons = ["Bow", "Shield", "Staff", "Spear"]
    for i, j in enumerate(weapons):
        print(f"{i + 1}: {j}")
    return weapons

def get_weapon_choice(weapons):
    while True:
        try:
            choice_num = int(input("Enter the number. "))
            if choice_num < 1 or choice_num > 4:
               print("The number must be between 1 and 4.")
               continue
            weapon_choice = weapons[choice_num - 1]
            print(f"You have chosen the {weapon_choice}.")
            return weapon_choice
        except ValueError:
            print("The input must be a number.")

def create_player(player_name, weapon_choice):
    if weapon_choice == "Staff":
        player = Staff(player_name)
    return player