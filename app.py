from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from services.database_connection import init_docker_db_config

from web.views.student.common import student_common
from web.views.student.v1.student import student_v1
from web.views.student.v2.student import student_v2

from web.views.teacher.v1.teacher import teacher_v1
from web.views.teacher.v2.teacher import teacher_v2

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

app.register_blueprint(student_common)
app.register_blueprint(student_v1, url_prefix='/v1')
app.register_blueprint(student_v2, url_prefix='/v2/student')

app.register_blueprint(teacher_v1, url_prefix='/v1/teacher')
app.register_blueprint(teacher_v2, url_prefix='/v2/teacher')

bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    if app.config['ENV'] == 'docker':
        init_docker_db_config()
        app.run(host='0.0.0.0')
    else:
        app.run()
