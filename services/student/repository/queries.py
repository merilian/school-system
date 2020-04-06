class StudentQueries:
    @staticmethod
    def get_all():
        return """SELECT * FROM Student"""

    @staticmethod
    def get_by_id():
        return """SELECT * FROM Student WHERE id = %s"""

    @staticmethod
    def insert():
        return """INSERT INTO Student (first_name, last_name, email) VALUES (%s, %s, %s)"""

    @staticmethod
    def update():
        return """UPDATE Student SET first_name = %s, last_name = %s, email  = %s WHERE id = %s"""

    @staticmethod
    def delete():
        return """DELETE FROM Student WHERE id = %s"""
