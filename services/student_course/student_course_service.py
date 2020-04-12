from .repository.student_course_repository import StudentCourseRepository
from .student_course_model import StudentCourseModel


class StudentCourseService:
    def __init__(self):
        self.course_repository = StudentCourseRepository()

    def get_all(self):
        course_records = self.course_repository.get_all()
        return [StudentCourseModel(**course) for course in course_records]

    def insert(self, course: StudentCourseModel):
        self.course_repository.insert(course.name, course.teacher_id)
