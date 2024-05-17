from utils.usermanager import UserManager
import os
from utils.score import Score
from datetime import datetime
import random

class DiceGame(Score):
    def __init__(self, scores_file):
        super().__init__(scores_file)
        self.user_folder = 'user'
        self.scores_file = os.path.join(self.user_folder, 'score.txt')
        self.create_data_folder()
        self.stage_win = 0 

    def create_data_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_scores(self):
        if os.path.exists(self.scores_file):
            with open(self.scores_file, 'r') as file:
                scores = []
                for line in file:
                    parts = line.strip().split(', ')
                    try:
                        score = int(parts[0])
                        stage_win = int(parts[1])  
                        user_name = parts[2]
                        date = parts[3]
                    except (ValueError, IndexError):
                        continue
                    scores.append((user_name, score, stage_win, date))
                return scores
        return []


    def savescore(self, user_name, score):
        if not isinstance(score, int):
            print(f"\tInvalid score value: {score}")
            return
        try:
            with open(self.scores_file, 'a') as file:
                now = datetime.now()
                score_date = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f'{score}, {self.stage_win}, {user_name}, {score_date}\n')
        except IOError:
            print("\tAn error occurred while trying to save the score.")

    def play_game(self, user_name):
        user_score = 0
        cpu_score = 0
        total_score = 0

        for _ in range(3):
            user_num = random.randint(1, 6)
            cpu_num = random.randint(1, 6)

            if user_num > cpu_num:
                print(f"\n\t{user_name}: {user_num}\n\tCPU: {cpu_num}\n\n\t***User Won!***\n")
                user_score += 1
            elif user_num < cpu_num:
                print(f"\n\t{user_name}: {user_num}\n\tCPU: {cpu_num}\n\n\t***CPU Won!***\n")
                cpu_score += 1
            else:
                print(f"\n\t{user_name}: {user_num}\n\tCPU: {cpu_num}\n\n\t***DRAW!***\n")

        if user_score > cpu_score:
            print("Congratulations! You win this round.")
            total_score += user_score + 3
            self.stage_win += 1
        elif user_score < cpu_score:
            print("You lose this round.")
            total_score += user_score
        else:
            print("This round is a draw.")
            total_score += user_score

        self.savescore(user_name, total_score)

        print(f"\n\tGame Over!\n\n{user_name}'s score: {total_score}, CPU's score: {cpu_score}, Stage Wins: {self.stage_win}")

        while True:
            continue_game = input("\n\tRoll Again (y/n): ").lower()
            if continue_game == 'y':
                self.play_game(user_name)
            elif continue_game == 'n':
                print("\n\tThanks for playing!")
                self.menu(user_name)
                break
            else:
                print("\n\tInvalid input. To continue please enter 'y' or 'n'.")

    def show_top_scores(self):
        scores = self.load_scores()
        scores.sort(key=lambda x: (x[1], x[2]), reverse=True)

        print("\n\t\t\t****PLAYERS SCORES****")
        for i, (user_name, total_score, stage_win, date) in enumerate(scores[:10], start=1):
            print(f"Rank {i:<10} {user_name:<10}: \tSCORE  =  {total_score:<10} WINS = {stage_win:<10} Date & Time: {date:<10}")


    def menu(self, user_name):
        print(f"\n****Welcome to Dice Roll Game {user_name}!****")
        while True:
            print("\n1. Play Game")
            print("\n2. Show Top Scores")
            print("\n3. Log out")
            choice = input("\n\tChoice: ")

            if choice == '1':
                self.play_game(user_name)
            elif choice == '2':
                self.show_top_scores()
            elif choice == '3':
                choice = input("\nAre you sure you want to Log-out? (y/n): ").lower()
                if choice == 'y':
                    print("\n\tLogging out.....")
                    self.register()
                else:
                    print("Invalid input. Please try again.")

    def register(self):
        user_manager = UserManager('user.txt')

        while True:
            print("\n******Welcome to the Dice Roll Game!******")
            choice = input("\n\tDo you want to play?(y/n): ").lower()
            if choice == 'y':
                print("\n1. Register")
                print("\n2. Log-in")
                print("\n3. Exit")
                choice = input("\nChoice: ")

                if choice == '1':
                    username = input("\nEnter a username (at least 4 characters): ")
                    if user_manager.validate_username(username):
                        password = input("\nEnter a password (at least 8 characters): ")
                        if user_manager.validate_password(password):
                            user_manager.register(username, password)
                            print("\n\tRegistration successful!")
                            self.continuation()
                        else:
                            print("\tPassword must be at least 8 characters. Please try again.")
                    else:
                        print("\n\tInvalid username or Username Taken. Please try again.")

                elif choice == '2':
                    username = input("\nEnter your username: ")
                    password = input("\nEnter your password: ")
                    if user_manager.login(username, password):
                        print("\n\tLogin successful!")
                        self.menu(username)
                        game = DiceGame(username)
                        if not game.menu(username):
                            continue
                        else:
                            print("\nInvalid username or password. Please try again.")

                    else:
                        print("\nInvalid username or password. Please try again.")

                elif choice == '3':
                    print("\n\tExiting.....")
                    break
                else:
                    print("Invalid input. Please try again.")
            elif choice == 'n':
                print("K.")
                exit()
            else:
                print("Invalid input. Please try again.")
        
    def continuation(self): 
        user_manager = UserManager('user.txt')
 
        while True:
            print("\n******Welcome to the Dice Roll Game!******")
            print("\n1. Register")
            print("\n2. Log-in")
            print("\n3. Exit")
            choice = input("\nChoice: ")

            if choice == '1':
                username = input("\nEnter a username (at least 4 characters): ")
                if user_manager.validate_username(username):
                    password = input("\nEnter a password (at least 8 characters): ")
                    if user_manager.validate_password(password):
                        user_manager.register(username, password)
                        print("\n\tRegistration successful!")
                    else:
                        print("\tPassword must be at least 8 characters. Please Try again.")
                else:
                    print("\n\tInvalid username or Username Taken. Please try again.")

            elif choice == '2':
                username = input("\nEnter your username: ")
                password = input("\nEnter your password: ")
                if user_manager.login(username, password):
                    print("\n\tLogin successful!")
                    self.menu(username)
                    game = DiceGame(username)
                    if not game.menu(username):
                        continue
                else:
                    print("\nInvalid username or password. Please try again.")

            elif choice == '3':
                print("\n\tExiting.....")
                exit()
            else:
                print("")
