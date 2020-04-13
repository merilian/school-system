class TeacherQueries:
    @staticmethod
    def get_all():
        return """SELECT * FROM Teacher"""

    @staticmethod
    def get_all_with_student_count():
        return """
SELECT    t.*,
          COUNT(DISTINCT sc.student_id) student_count
FROM      Teacher t 
JOIN      Course c on c.teacher_id = t.id 
JOIN      StudentCourse sc on sc.course_id = c.id 
GROUP BY  t.id, t.first_name, t.last_name, t.email """

    @staticmethod
    def insert():
        return """INSERT INTO Teacher (first_name, last_name, email) VALUES (%s, %s, %s)"""

    @staticmethod
    def update():
        return """UPDATE Teacher SET first_name = %s, last_name = %s, email  = %s WHERE id = %s"""

    @staticmethod
    def delete():
        return """DELETE FROM Teacher WHERE id = %s"""
