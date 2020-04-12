import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing

connection_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'dbuser',
    'password': 'dbpassword',
    'db': 'school',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}


def init_docker_db_config():
    connection_config['host'] = 'school_system_db'


def get_db_connection():
    return pymysql.connect(**connection_config)


def execute_query(query, params=()):
    with closing(get_db_connection()) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            return cursor
