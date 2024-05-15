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

    def create_data_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_scores(self):
        if os.path.exists(self.scores_file):
            with open(self.scores_file, 'r') as file:
                scores = []
                for line in file:
                    score, user_name, date = line.strip().split(', ')
                    try:
                        score = int(score)
                    except ValueError:
                        print(f"\tInvalid score value for user {user_name} on {date}. Skipping this entry.")
                        continue
                    scores.append((user_name, int(score), date))
                return scores
        return []

    def savescore(self, user_name, score):
        if not isinstance(score, int):
            print(f"\tInvalid score value: {score}")
        try:
            with open(self.scores_file, 'a') as file:
                now = datetime.now()
                score_date = now.strftime("%Y-%m-%d %H:%M:%S")
                file.write(f'{score}, {user_name}, Achieved on: {score_date}\n')
        except IOError:
            return print("\tAn error occurred while trying to save the score.")

    def play_game(self, user_name):
        user_score = 0
        cpu_score = 0

        for i in range (3):
            user_num = random.randint(1,6)
            cpu_num = random.randint(1,6)

            if user_num > cpu_num:
                print(f"\tUser: {user_num}\n\tCPU: {cpu_num}\n\n\t***User Won!***\n")
                user_score += 1
            elif user_num < cpu_num:
                print(f"\tUser: {user_num}\n\tCPU: {cpu_num}\n\n\t***CPU Won!***\n")
                cpu_score += 1
            else:
                print(f"\n\tUser: {user_num}\n\tCPU: {cpu_num}\n\n\t***DRAW!***\n")

        if user_score > cpu_score:
            user_score += 3
        
        save_user_scores = int(user_score)

        self.savescore(user_name, save_user_scores)

        print(f"Game Over! {user_name}'s score: {user_score}, \tCPU's score: {cpu_score}")

        while True:
            continue_game = input("\n\tPlay Again? (y/n): ")

            if continue_game.lower() == 'y':
                self.play_game(user_name)
            elif continue_game.lower() == 'n':
                print("\n\tThanks for playing!")
                self.menu(user_name)
            else:
                print("\n\tInvalid input. To continue please enter 'y' or 'n'.")

    def show_top_scores(self):
        scores = self.load_scores()
        scores.sort(key=lambda x: x[1], reverse=True)

        print("\n\t\t\t****PLAYERS SCORES****")

        print(f'{"\n\tRanking":<10} {"Username":<10} {"Score":<10} {"\t\tDate":<10}')

        for i in range(10): 
            if i < len(scores):
                user_name, score, date = scores[i]
                print(f'\t{i+1:<10} {user_name:<10} {score:<10} {date:<10}')
            else:
                print(f"{i+1:<10}****")

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
                print("\n\tLogging out. Thanks for playing...\n")
                self.menu(user_name)
