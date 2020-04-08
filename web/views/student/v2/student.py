from flask import Blueprint, render_template, redirect, request
from services.student.student_service import StudentsService
from services.student.student_model import StudentModel

student_v2 = Blueprint('student-v2', __name__, template_folder='templates', static_folder='static')


@student_v2.route('/create')
def create_student():
    return render_template('/student/form.html', student=StudentModel(), post_link='/v2/student/save')


@student_v2.route('/update/<int:id>')
def update_student(id):
    students_service = StudentsService()
    students = students_service.get_by_id(id)
    if len(students) != 1:
        # return redirect('404')
        pass
    return render_template('/student/form.html', student=students[0], post_link='/v2/student/save/'+str(id))


@student_v2.route('/save', defaults={'id': None}, methods=['POST'])
@student_v2.route('/save/<int:id>', methods=['POST'])
def save_student(id):
    students_service = StudentsService()
    student_to_save = StudentModel(**request.form)
    if id:
        student_to_save.id = id
        students_service.update(student_to_save)
    else:
        students_service.insert(student_to_save)
    return redirect('/student')