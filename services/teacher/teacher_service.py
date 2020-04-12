from .repository.teacher_repository import TeacherRepository
from .teacher_model import TeacherModel


class TeacherService:
    def __init__(self):
        self.teacher_repository = TeacherRepository()

    def get_all(self):
        teacher_records = self.teacher_repository.get_all()
        return [TeacherModel(**teacher) for teacher in teacher_records]

    def insert(self, teacher: TeacherModel):
        self.teacher_repository.insert(teacher.first_name, teacher.last_name, teacher.email)

    def update(self, teacher: TeacherModel):
        self.teacher_repository.update(teacher.id, teacher.first_name, teacher.last_name, teacher.email)

    def delete(self, id):
        self.teacher_repository.delete(id)
