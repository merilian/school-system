class StudentCourseQueries:
    @staticmethod
    def get_all():
        return """SELECT * FROM StudentCourse"""

    @staticmethod
    def insert():
        return """INSERT INTO StudentCourse (student_id, course_id) VALUES (%s, %s)"""
