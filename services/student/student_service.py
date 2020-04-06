from .repository.student_repository import StudentsRepository
from .student_model import StudentModel


class StudentsService:
    def __init__(self):
        self.studentsRepository = StudentsRepository()

    def get_all(self):
        student_records = self.studentsRepository.get_all()
        return [StudentModel(**student) for student in student_records]

    def get_by_id(self, id):
        student_records = self.studentsRepository.get_by_id(id)
        return [StudentModel(**student) for student in student_records]

    def insert(self, student: StudentModel):
        self.studentsRepository.insert(student.first_name, student.last_name, student.email)

    def update(self, student: StudentModel):
        self.studentsRepository.update(student.id, student.first_name, student.last_name, student.email)

    def delete(self, id):
        self.studentsRepository.delete(id)
