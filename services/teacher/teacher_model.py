class TeacherModel:
    id = 0
    first_name = ''
    last_name = ''
    email = ''

    def __init__(self, **entries):
        self.__dict__.update(entries)
