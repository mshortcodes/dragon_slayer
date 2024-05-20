from story.intro import intro
from story.training import training
from story.leveling import leveling

def main():
    player = intro()
    training(player)
    leveling(player)

main()