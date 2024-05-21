import random
import time

def fishing(player):
    print_instructions(player)
    get_fishing_choice()
    random_item = get_random_item()
    go_fishing(player, random_item)
    handle_fishing(player)

def print_instructions(player):
    print(f"\n{player.name}, you have completed your training and must now find the Dragon Ring.\n You can only fight the dragon once you have the ring. \n")
    print("There are stories of an old fisherman once spotting it in the nearby river. You will have to try and fish it up.")
    print("The Dragon Ring has a very low chance to be caught, so don't give up until you catch it!")

def get_fishing_choice():
    while True:
        choice = input("\nBegin fishing? [y/n] ")
        if choice == "n":
            print("You must fish until you find the Dragon Ring.")
        elif choice == "y":
            return
        else:
            print("Enter y or n.")

def get_random_item():
    river = ["Dragon Ring", "bass", "potion", "trash", "trout", "potion", "bass", "bass", "trash", "trout"]
    random_item = random.choice(river)
    return random_item

def go_fishing(player, random_item):
    print("Fishing...")
    time.sleep(2)
    if random_item == "Dragon Ring":
        print(f"You found the {random_item}!")
        player.has_dragon_ring = True
    elif random_item == "Potion":
        print(f"You found a {random_item} that restores half of your health and mana.")
        player.potions += 1
    else:
        print(f"You caught {random_item}.")

def handle_fishing(player):
    while not player.has_dragon_ring:
        get_fishing_choice()
        random_item = get_random_item()
        go_fishing(player, random_item)
        


