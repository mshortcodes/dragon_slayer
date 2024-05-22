from story.intro import intro
from story.training import training
from story.fishing import fishing
from story.battle import battle
import time

def main():
    playing = True
    while playing:
        player = intro()
        training(player)
        fishing(player)
        battle(player)
        playing = play_again()
    print("\nThanks for playing!\n")

def play_again():
    while True:
        time.sleep(1)
        choice = input("Play again? [y/n] ")
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            input("Enter y or n. ")

main()