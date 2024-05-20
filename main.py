from story.intro import intro
from story.training import training
from story.fishing import fishing

def main():
    player = intro()
    training(player)
    fishing(player)

main()