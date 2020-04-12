from services.database_connection import execute_query
from .queries import StudentCourseQueries


class StudentCourseRepository:
    def __init__(self):
        pass

    def get_all(self):
        rows = [row for row in execute_query(StudentCourseQueries.get_all())]
        return rows

    def insert(self, student_id, course_id):
        execute_query(StudentCourseQueries.insert(), (student_id, course_id))
