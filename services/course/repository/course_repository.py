from services.database_connection import execute_query
from .queries import CourseQueries


class CourseRepository:
    def __init__(self):
        pass

    def get_all(self):
        rows = [row for row in execute_query(CourseQueries.get_all())]
        return rows

    def insert(self, name, teacher_id):
        execute_query(CourseQueries.insert(), (name, teacher_id))
