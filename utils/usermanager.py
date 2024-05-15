
import os
from utils.user import User

class UserManager(User):
    def __init__(self, user_file):
        self.user_folder = 'user'
        self.user_file = os.path.join(self.user_folder, user_file)

        super().__init__(self.user_file)
        self.create_user_folder()
        self.users = self.load_users()

    def create_user_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as file:
                users = {}
                for line in file:
                    username, password = line.strip().split(', ')
                    users[username] = password
                return users
        return {}

    def save_users(self, username, password):
        try:
            with open(self.user_file, 'a') as file:
                file.write(f'{username}, {password}\n')      
        except IOError:
            return print("An error occurred while trying to save the user.")
        
    def validate_username(self, username):
        return len(username) >= 4  and username not in self.users

    def validate_password(self, password):
        return len(password) >= 8

    def register(self, username, password):
        self.users[username] = password
        self.save_users(username, password)

    def login(self, username, password):
        return self.users.get(username) == password



