import sys
import random
import time

def fishing(player):
    print_instructions(player)
    get_fishing_choice()
    random_item = get_random_item()
    fish(random_item)

def print_instructions(player):
    print(f"\n{player.name}, you have completed your training and must now find the Dragon Ring. You can only fight the dragon once you have the ring. \n")
    print("There are stories of an old fisherman once spotting it in the nearby river. You will have to try and fish it up.")
    print("The Dragon Ring has a very low chance to be caught, so don't give up until you catch it!")

def get_fishing_choice():
    while True:
        choice = input("Begin fishing? [y/n] ")
        if choice == "n":
            print("=== Game over ===")
            sys.exit()
        elif choice == "y":
            return
        else:
            print("Enter y or n.")
            continue

def get_random_item():
    river = ["Dragon Ring", "Bass", "Potion", "Trash", "Trout", "Potion", "Bass", "Bass", "Trash", "Trout"]
    random_item = random.choice(river)
    return random_item

def fish(random_item):
    print("Fishing...")
    time.sleep(2)
    print(f"You caught a {random_item}!")


