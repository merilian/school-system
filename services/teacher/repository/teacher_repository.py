from services.database_connection import execute_query
from .queries import TeacherQueries


class TeacherRepository:
    def __init__(self):
        pass

    def get_all(self):
        rows = [row for row in execute_query(TeacherQueries.get_all())]
        return rows

    def insert(self, first_name, last_name, email):
        execute_query(TeacherQueries.insert(), (first_name, last_name, email))

    def update(self, id, first_name, last_name, email):
        execute_query(TeacherQueries.update(), (first_name, last_name, email, id))

    def delete(self, id):
        execute_query(TeacherQueries.delete(), (id,))
