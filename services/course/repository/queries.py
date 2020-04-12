class CourseQueries:
    @staticmethod
    def get_all():
        return """SELECT * FROM Course"""

    @staticmethod
    def insert():
        return """INSERT INTO Course (name, teacher_id) VALUES (%s, %s)"""
