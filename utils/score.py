class Score:
    def __init__(self, scores_file):
        self.scores_file = scores_file

    def load_score(self):
        try:
            with open(self.scores_file, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in scores file.")
    
    def load_score_date(self):
        try:
            with open(self.score_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None