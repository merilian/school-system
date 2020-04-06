from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from .views.student import student

app = Flask(__name__)
app.register_blueprint(student)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
