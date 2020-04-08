from flask import Blueprint, render_template, redirect
from services.student.student_service import StudentsService

student_common = Blueprint('student-common', __name__, template_folder='templates', static_folder='static')


@student_common.route('/student')
def show_students():
    students_service = StudentsService()
    students = students_service.get_all()
    return render_template('student/list.html', students=students)


@student_common.route('/student/delete/<int:id>')
def delete_student(id):
    students_service = StudentsService()
    students_service.delete(id)
    return redirect('/student')
