import os

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData, Boolean


class Database:
    def __init__(self):
        self.db_engine = create_engine('sqlite:///allTables.db')

    def init_table(self):
        metadata = MetaData()
        perf = Table(
            'perf',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('kills', Integer),
            Column('deaths', Integer),
            Column('assists', Integer),
            Column('result', Boolean)
        )
        metadata.create_all(self.db_engine)
        print("Table Created")

    def reset_table(self):
        if os.path.exists(os.path.join(os.getcwd(), 'allTables.db')):
            self.db_engine.dispose()
            os.remove(os.path.join(os.getcwd(), 'allTables.db'))
            self.db_engine = create_engine('sqlite:///allTables.db')
            self.init_table()

    def execute_insert(self, kill, death, assists, result):
        query = f"INSERT INTO perf(kills, deaths, assists, result) VALUES ({kill}, {death}, {assists}, {result});"
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def display_runs(self, mode, limit=0):
        if mode == 2:
            query = f"SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC LIMIT {limit}"
        elif mode == 3:
            query = "SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC"
        else:
            query = "SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC LIMIT 10"
        with self.db_engine.connect() as connection:
            try:
                data = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                self.run_recap(data)

    def best_run(self):
        query = "SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC"
        with self.db_engine.connect() as connection:
            try:
                data = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                bestratio = 0
                for row in data:
                    try:
                        current = (row[0] + row[2]) / row[1]
                    except ZeroDivisionError:
                        current = row[0] + row[2]
                    if current > bestratio:
                        bestkill = row[0]
                        bestdeath = row[1]
                        bestassists = row[2]
                        bestresult = "WIN" if row[3] else "LOSS"
                        bestratio = current
                print("Your best run was the following :\n")
                print(f"You made {bestkill} kills, {bestdeath} deaths, {bestassists} assists, "
                      f"and it was a {bestresult}. The ratio was {bestratio}.")
        input("press Enter to continue ....")

    def run_add_recap(self, data):
        return

    def recap_for_previous(self):
        return

    def run_recap(self, data):
        ratio = 0
        best = 0
        counter = 0
        wincount = losscount = 0
        for row in data:
            counter += 1
            try:
                current = (row[0] + row[2]) / row[1]
            except ZeroDivisionError:
                current = row[0] + row[2]
            if best < current:
                best = current
            ratio += current
            if row[3]:
                wincount += 1
                result = "WIN"
            else:
                losscount += 1
                result = "LOSS"
            print(f'Kills: {row[0]} / Deaths : {row[1]} / Assists: {row[2]}  //  {result}')
        ratio = ratio / counter
        performance = (best / 100) * ratio
        winrate = (wincount / (wincount + losscount)) * 100
        print(f'\nListed runs ratio (KDA) : {round(ratio, 2)} / '
              f'This is {round(performance, 2)}% of your max performance.'
              f' / Your actual winrate is {round(winrate, 2)}%')
        input("press Enter to continue ....")


database = Database()
