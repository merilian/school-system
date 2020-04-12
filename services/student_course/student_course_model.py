class StudentCourseModel:
    id = 0
    name = ''
    teacher_id = ''

    def __init__(self, **entries):
        self.__dict__.update(entries)
