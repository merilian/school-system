class TeacherQueries:
    @staticmethod
    def get_all():
        return """SELECT * FROM Teacher"""

    @staticmethod
    def insert():
        return """INSERT INTO Teacher (first_name, last_name, email) VALUES (%s, %s, %s)"""

    @staticmethod
    def update():
        return """UPDATE Teacher SET first_name = %s, last_name = %s, email  = %s WHERE id = %s"""

    @staticmethod
    def delete():
        return """DELETE FROM Teacher WHERE id = %s"""
