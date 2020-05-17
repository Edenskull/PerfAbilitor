import os

from .modelController import database


class Menu:
    @staticmethod
    def display_credits():
        print("############################\nPerfAbilitor v0.1          #\n"
              "Created By Maxime CHAMPAIN #\n############################\n")
        input("Press Enter to continue ...")

    @staticmethod
    def main_menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--------- Main Menu ---------\n")
            print("Choose Action (Type the numeric of your choice/ 'quit' to exit) :\n\n"
                  "1 - Add Run\n2 - Display last runs\n3 - Display Ratio\n4 - Reset Table\n")
            choice = str(input("> "))
            if choice == '1':
                Menu.add_run_menu()
            elif choice == '2':
                Menu.display_runs_menu()
            elif choice == '3':
                return
            elif choice == '4':
                database.reset_table()
                print("Database Flushed. Everything is reset to 0")
            elif choice == 'quit':
                exit(123)

    @staticmethod
    def add_run_menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--------- Add a run ---------\n")
            try:
                kill = int(input("How many kills : "))
                death = int(input("How many deaths : "))
                assists = int(input("How many assists : "))
                result = str(input("Did you win (yes/no and default is 'no') ? "))
                if result.lower() not in ['yes', 'no']:
                    result = False
                elif result.lower() is 'yes':
                    result = True
                else:
                    result = False
                break
            except Exception as e:
                print("You can't add this property. Please retry")
                continue
        database.execute_insert(kill, death, assists, result)

    @staticmethod
    def display_runs_menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--------- Display my runs ---------\n")
            print("Choose Action (Type the numeric of your choice/ 'quit' to return) :\n\n"
                  "1 - Display last ten runs\n2 - Display custom numbers of runs\n"
                  "3 - Display all runs (Be careful if there is tons of runs)\n")
            choice = str(input("> "))
            if choice == '1':
                database.last_ten()
            elif choice == '2':
                while True:
                    try:
                        limit = int(input("Choose a number of runs you want to display : "))
                        break
                    except Exception as e:
                        print("This is not an appropriate number")
                        continue
                database.custom_runs(limit)
            elif choice == '3':
                database.whole_runs()
            elif choice == 'quit':
                Menu.main_menu()
