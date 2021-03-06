from flask import Flask, url_for, redirect, Response, request
import json
from model.users import Users

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Users.confirm_account(username, password):
            res = {'result': 'True'}
            return json.dumps(res)

        else:
            res = {'result': 'False', 'error': 'user or password error'}
            return json.dumps(res)

    else:
        return Response('''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form> 
            ''')

# @app.route()
# def add_staff():
#     return


# @app.route()
# def create_staff():
#     return


# @app.route()
# def del_template():
#     return


# @app.route()
# def add_template():
#     return

# @app.route()
# def add_template():
#     return


# @app.route()
# def crate_template():
#     return


# @app.route()
# def edit_template():
#     return


# @app.route()
# def del_template():
#     return


# @app.route()
# def add_container():
#     return


# @app.route()
# def start_container():
#     return


# @app.route()
# def edit_container():
#     return

# @app.route()
# def del_container():
#     return


if __name__ == '__main__':
    app.run(port = 5000)
