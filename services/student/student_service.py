from .repository.student_repository import StudentRepository
from .student_model import StudentModel


class StudentService:
    def __init__(self):
        self.student_repository = StudentRepository()

    def get_all(self):
        student_records = self.student_repository.get_all()
        return [StudentModel(**student) for student in student_records]

    def get_by_id(self, id):
        student_records = self.student_repository.get_by_id(id)
        return [StudentModel(**student) for student in student_records]

    def insert(self, student: StudentModel):
        self.student_repository.insert(student.first_name, student.last_name, student.email)

    def update(self, student: StudentModel):
        self.student_repository.update(student.id, student.first_name, student.last_name, student.email)

    def delete(self, id):
        self.student_repository.delete(id)
