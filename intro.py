from classes import Mage

def intro():
    print_intro_message()
    player_name = get_player_name()
    print(f"\nGreetings, {player_name}!")
    player = choose_class(player_name)
    return player
  
def print_intro_message():
    print("⚔️ Welcome to Dragon Slayer! ⚔️")
    print("\nThe kingdom of Dragonia, your home, and dragons were once at peace until the Great War. \nYou escaped to a neighboring kingdom to find refuge from the last surviving dragon, Oolong. \nMany have tried to defeat him, but all have failed. \nIt is up to you to train and become the hero of this world, the Dragon Slayer!\n")

def get_player_name():
    print("All heroes need a name.")
    return input("What is your name? ")

def choose_class(player_name):
    print("You must choose a class, train, and defeat the dragon.\n")

    classes = ["Warrior", "Paladin", "Mage", "Ninja"]
    for i, j in enumerate(classes):
        print(f"{i + 1}: {j}")

    # get input as integer
    has_chosen = False
    while not has_chosen:
        chosen_class = int(input("Enter the number. "))
        if chosen_class > 0 and chosen_class <= 4:
            has_chosen = True

    # convert input to class str
    chosen_class = classes[chosen_class - 1]

    if chosen_class == "Mage":
        player = Mage(player_name)

    print(f"You have chosen the {chosen_class} class.")

    return player