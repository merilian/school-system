from collections import defaultdict

from .repository.teacher_repository import TeacherRepository
from services.course.course_service import CourseService
from services.student_course.student_course_service import StudentCourseService
from .teacher_model import TeacherModel


class TeacherService:
    def __init__(self):
        self.teacher_repository = TeacherRepository()
        self.course_service = CourseService()
        self.student_course_service = StudentCourseService()

    def get_all(self):
        teacher_records = self.teacher_repository.get_all()
        return [TeacherModel(**teacher) for teacher in teacher_records]

    def get_all_with_max_students(self):
        teacher_records = self.teacher_repository.get_all_with_student_count()
        max_student_count = max(teacher_records, key=lambda t: t['student_count'])['student_count']
        return [TeacherModel(**teacher) for teacher in teacher_records if teacher['student_count'] == max_student_count]

    def get_all_with_max_students_v2(self):
        teachers = self.get_all()
        courses = self.course_service.get_all()
        student_courses = self.student_course_service.get_all()

        students_by_teacher = defaultdict(set)
        for teacher in teachers:
            for course in filter(lambda c: c.teacher_id == teacher.id, courses):
                student_ids = [sc.student_id for sc in filter(lambda sc: sc.course_id == course.id, student_courses)]
                students_by_teacher[teacher.id].update(student_ids)

            teacher.student_count = len(students_by_teacher[teacher.id])

        max_student_count = max(teachers, key=lambda t: t.student_count).student_count
        return list(filter(lambda t: t.student_count == max_student_count, teachers))

    def insert(self, teacher: TeacherModel):
        self.teacher_repository.insert(teacher.first_name, teacher.last_name, teacher.email)

    def update(self, teacher: TeacherModel):
        self.teacher_repository.update(teacher.id, teacher.first_name, teacher.last_name, teacher.email)

    def delete(self, id):
        self.teacher_repository.delete(id)
