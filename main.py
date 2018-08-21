from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)


@app.route()
def login():
    return

@app.route()
def add_staff():
    return


@app.route()
def create_staff(name):
    return


@app.route()
def del_template(name):
    return


@app.route()
def add_template(name):
    return

@app.route()
def add_template():
    return


@app.route()
def crate_template(name):
    return


@app.route()
def edit_template(name):
    return


@app.route()
def del_template(name):
    return


@app.route()
def add_container():
    return


@app.route()
def start_container(name):
    return


@app.route()
def edit_container(name):
    return

@app.route()
def del_container(name):
    return


if __name__ == '__main__':
    app.run(debug=True)
