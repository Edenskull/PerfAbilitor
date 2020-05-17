import os

from PerfAbilitor.menuController import Menu
from PerfAbilitor.modelController import database


def run():
    if not os.path.exists(os.path.join(os.getcwd(), 'allTables.db')):
        database.init_table()
    Menu.display_credits()
    Menu.main_menu()


if __name__ == '__main__':
    run()
