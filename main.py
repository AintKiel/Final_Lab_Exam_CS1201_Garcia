from utils.dicegame import DiceGame

def main():
    scores_file = 'path/to/scores/file.txt' 
    game = DiceGame(scores_file) 
    game.register()

if __name__ == '__main__':
    main()
