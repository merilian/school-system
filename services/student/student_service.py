from .repository.student_repository import StudentsRepository
from .student_model import StudentModel


class StudentsService:
    def __init__(self):
        self.studentsRepository = StudentsRepository()

    def get_all(self):
        return [StudentModel(student) for student in self.studentsRepository.get_all()]

    def insert(self, student: StudentModel):
        self.studentsRepository.insert(student.first_name, student.last_name, student.email)

    def update(self, student: StudentModel):
        self.studentsRepository.update(student.id, student.first_name, student.last_name, student.email)

    def delete(self, student: StudentModel):
        self.studentsRepository.delete(student.id)
