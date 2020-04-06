from flask import Blueprint, render_template, redirect, request
from services.student.student_service import StudentsService
from services.student.student_model import StudentModel

student = Blueprint('student', __name__, template_folder='templates', static_folder='static')


@student.route('/student')
def show_students():
    studentsService = StudentsService()
    students = studentsService.get_all()
    return render_template('student/list.html', students=students)


@student.route('/student/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'GET':
        return render_template('/student/form.html', student=StudentModel(), post_link='/student/create')
    else:
        studentsService = StudentsService()
        studentToCreate = StudentModel(**request.form)
        studentsService.insert(studentToCreate)
    return redirect('/student')


@student.route('/student/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    studentsService = StudentsService()
    if request.method == 'GET':
        students = studentsService.get_by_id(id)
        if len(students) != 1:
            # return redirect('404')
            pass
        return render_template('/student/form.html', student=students[0], post_link='/student/update/'+str(id))
    else:
        studentToUpdate = StudentModel(**request.form)
        studentToUpdate.id = id
        studentsService.update(studentToUpdate)
    return redirect('/student')


@student.route('/student/delete/<int:id>')
def delete_student(id):
    studentsService = StudentsService()
    studentsService.delete(id)
    return redirect('/student')
