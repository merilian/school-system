from services.database_connection import execute_query
from .queries import StudentQueries


class StudentsRepository:
    def __init__(self):
        pass

    def get_all(self):
        rows = [row for row in execute_query(StudentQueries.get_all())]
        return rows

    def insert(self, first_name, last_name, email):
        execute_query(StudentQueries.insert(), (first_name, last_name, email))

    def update(self, id, first_name, last_name, email):
        execute_query(StudentQueries.update(), (first_name, last_name, email, id))

    def delete(self, id):
        execute_query(StudentQueries.delete(), (id,))
