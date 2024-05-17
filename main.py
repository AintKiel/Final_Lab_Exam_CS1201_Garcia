from utils.usermanager import UserManager
from utils.dicegame import DiceGame

def main():
    user_manager = UserManager('user.txt')

    while True:
        print("\n******Welcome to the Dice Roll Game!******y")
        choice = input("\n\tDo you want to play?(y/n): ")
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
                        continuation()
                    else:
                        print("\tPassword must be at least 8 characters. Please Try again.")
                else:
                    print("\n\tInvalid username or Username Taken. Please try again.")

            elif choice == '2':
                username = input("\nEnter your username: ")
                password = input("\nEnter your password: ")
                if user_manager.login(username, password):
                    print("\n\tLogin successful!")
                    game = DiceGame(username)
                    if not game.menu(username):
                        continue
                else:
                    print("\nInvalid username or password. Please try again.")

            elif choice == '3':
                print("\n\tExiting.....")
                break
            else:
                print("")
        elif choice == 'n':
            print("K.")
        else:
            break

def continuation(): 
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
                game = DiceGame(username)
                if not game.menu(username):
                    continue
            else:
                print("\nInvalid username or password. Please try again.")

        elif choice == '3':
            print("\n\tExiting.....")
            break
        else:
            print("")

if __name__ == "__main__":
    main()
