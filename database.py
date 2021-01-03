import sqlite3

Create_bean_table = """
                CREATE TABLE IF NOT EXISTS beans
                (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    method TEXT,
                    rating INTEGER
                );
        """

Insert_bean = """
                INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);
"""

get_all_beans = "SELECT * FROM beans"

get_beans_by_name = "SELECT * FROM beans WHERE name = ?"


get_best_preperation_for_bean = """
    SELECT * FROM beans
    WHERE name = ?
    ORDER BY rating DESC
    LIMIT 1;
"""


def connect():
    connection = sqlite3.connect("data.db")
    return connection


def create_table(connection):
    with connection:
        connection.execute(Create_bean_table)


def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(Insert_bean, (name, method, rating))


def get_all_beans_func(connection):
    with connection:
        a = connection.execute(get_all_beans).fetchall()
    return a


def get_beans_by_name_func(connection, name):
    with connection:
        a = connection.execute(get_beans_by_name, (name,)).fetchall()
    return a


def get_best_preperation_for_bean_func(connection, name):
    with connection:
        return connection.execute(get_best_preperation_for_bean, (name,)).fetchone()
