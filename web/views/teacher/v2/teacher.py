import json
from flask import Blueprint
from web.views.data_encoding import ComplexEncoder
from services.teacher.teacher_service import TeacherService

teacher_v2 = Blueprint('teacher-v2', __name__, template_folder='templates', static_folder='static')


@teacher_v2.route('/get-with-max-students')
def get_with_max_students():
    teacher_service = TeacherService()
    return json.dumps(teacher_service.get_all_with_max_students_v2(), cls=ComplexEncoder)
