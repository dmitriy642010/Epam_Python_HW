"""
Write a wrapper class TableData for database table, that when initialized with database name and table acts as
collection object (implements Collection protocol).
Assume all data has unique values in 'name' column. So, if presidents = TableData(database_name='example.sqlite',
table_name='presidents')

then
    len(presidents) will give current amount of rows in presidents table in database
    presidents['Yeltsin'] should return single data row for president with name Yeltsin
    'Yeltsin' in presidents should return if president with same name exists in table
    object implements iteration protocol. i.e. you could use it in for loops::
    for president in presidents:
    print(president['name'])
all above mentioned calls should reflect most recent data. If data in table changed after you created collection
instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the
next one, until records are exhausted. When writing tests, it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import sqlite3
from typing import Callable, Tuple
from dataclasses import dataclass


def connect_database(func: Callable):
    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return func(self, cursor, *args, **kwargs)

    return wrapper


@dataclass
class TableData:
    database_name: str
    table_name: str

    @connect_database
    def __len__(self, cursor) -> int:
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()[0]

    @connect_database
    def __getitem__(self, cursor, item: str) -> Tuple:
        cursor.execute(
            f"SELECT * from  {self.table_name} WHERE name = :item", {"item": item}
        )
        return cursor.fetchone()

    @connect_database
    def __contains__(self, cursor, item: str) -> bool:
        cursor.execute(
            f"SELECT * from {self.table_name} WHERE name =:item", {"item": item}
        )
        return cursor.fetchone()

    @connect_database
    def __iter__(self, cursor) -> Tuple:
        cursor.execute(f"SELECT * from {self.table_name}")
        return cursor
