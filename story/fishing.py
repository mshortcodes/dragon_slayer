import random
import time

def fishing(player):
    print_instructions(player)
    get_fishing_choice()
    random_item = get_random_item()
    go_fishing(player, random_item)
    handle_fishing(player)

def print_instructions(player):
    print(f"\n{player.name}, you have completed your training and must now find the Dragon Ring.")
    time.sleep(1)
    print("You can only fight the dragon once you have the ring.")
    time.sleep(1)
    print("\nThere are stories of an old fisherman once spotting it in the nearby river. You will have to try and fish it up.")
    time.sleep(1)
    print("The Dragon Ring has a very low chance to be caught, so don't give up until you catch it!")

def get_fishing_choice():
    while True:
        time.sleep(1)
        choice = input("\nGo fishing? [y/n] ")
        if choice == "n":
            print("You must fish until you find the Dragon Ring and one potion.")
        elif choice == "y":
            return
        else:
            print("Enter y or n.")

def get_random_item():
    river = ["Dragon Ring",
             "Dragon Ring",
             "potion", 
             "potion", 
             "potion", 
             "trash", 
             "trash",
             "trout", 
             "trout",
             "bass", 
             "bass", 
             "bass",
            ]
    random_item = random.choice(river)
    return random_item

def go_fishing(player, random_item):
    print("Fishing...")
    time.sleep(2)
    if random_item == "Dragon Ring":
        print(f"You found the {random_item}!")
        player.has_dragon_ring = True
    elif random_item == "potion":
        print(f"You found a {random_item} that restores half of your health and mana.")
        player.potions += 1
    else:
        print(f"You caught {random_item}.")

def handle_fishing(player):
    while not player.has_dragon_ring or not player.potions:
        get_fishing_choice()
        random_item = get_random_item()
        go_fishing(player, random_item)
        


