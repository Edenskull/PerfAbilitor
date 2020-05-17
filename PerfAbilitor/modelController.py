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

    def last_ten(self):
        query = "SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC LIMIT 10"
        with self.db_engine.connect() as connection:
            try:
                data = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in data:
                    result = "WIN" if row[3] else "LOSS"
                    print(f'Kills: {row[0]} / Deaths : {row[1]} / Assists: {row[2]}  //  {result}')

    def whole_runs(self):
        query = "SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC"
        with self.db_engine.connect() as connection:
            try:
                data = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in data:
                    result = "WIN" if row[3] else "LOSS"
                    print(f'Kills: {row[0]} / Deaths : {row[1]} / Assists: {row[2]}  //  {result}')

    def custom_runs(self, limit):
        query = f"SELECT kills, deaths, assists, result FROM perf ORDER BY id DESC LIMIT {limit}"
        with self.db_engine.connect() as connection:
            try:
                data = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in data:
                    result = "WIN" if row[3] else "LOSS"
                    print(f'Kills: {row[0]} / Deaths : {row[1]} / Assists: {row[2]}  //  {result}')


database = Database()
