from story.intro import intro
from story.training import training

def main():
    player = intro()
    training(player)
    
main()