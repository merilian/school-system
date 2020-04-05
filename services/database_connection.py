import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='dbuser',
        password='dbpassword',
        db='school',
        charset='utf8mb4',
        cursorclass=DictCursor
    )


def execute_query(query, params=()):
    with closing(get_db_connection()) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            return cursor
