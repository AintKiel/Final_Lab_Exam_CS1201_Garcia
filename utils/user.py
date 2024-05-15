class User:
    def __init__(self, user_file):
        self.user_file = user_file

    def load_user(self):
        try:
            with open(self.user_file, 'r') as file:
                return str(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in score file. ")
            return None