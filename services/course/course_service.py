from .repository.course_repository import CourseRepository
from .course_model import CourseModel


class CourseService:
    def __init__(self):
        self.course_repository = CourseRepository()

    def get_all(self):
        course_records = self.course_repository.get_all()
        return [CourseModel(**course) for course in course_records]

    def insert(self, course: CourseModel):
        self.course_repository.insert(course.name, course.teacher_id)
