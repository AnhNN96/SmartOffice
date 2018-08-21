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
