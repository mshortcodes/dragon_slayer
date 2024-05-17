from staff import Staff

def intro():
    print_intro_message()
    player_name = get_player_name()
    print(f"\nGreetings, {player_name}!")
    player = choose_weapon(player_name)
    return player
  
def print_intro_message():
    print("Welcome to Dragon Slayer!")
    print("\nThe kingdom of Dragonia, your home, and dragons were once at peace until the Great War. \nYou escaped to a neighboring kingdom to find refuge from the last surviving dragon, Oolong. \nMany have tried to defeat him, but all have failed. \nIt is up to you to train and become the hero of this world, the Dragon Slayer!\n")

def get_player_name():
    print("All heroes need a name.")
    return input("What is your name? ")

def choose_weapon(player_name):
    print("You must choose a weapon, train, and defeat the dragon.\n")

    weapons = ["Bow", "Shield", "Staff", "Spear"]
    for i, j in enumerate(weapons):
        print(f"{i + 1}: {j}")

    # get input as integer
    has_chosen = False
    while not has_chosen:
        chosen_weapon = int(input("Enter the number. "))
        if chosen_weapon > 0 and chosen_weapon <= 4:
            has_chosen = True

    # get weapon str from list
    chosen_weapon = weapons[chosen_weapon - 1]

    if chosen_weapon == "Staff":
        player = Staff(player_name)

    print(f"You have chosen the {chosen_weapon}.")

    return player