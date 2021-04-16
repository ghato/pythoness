from flask import Flask
from flask import render_template
from flask import request
from flask import session

import data as app_data

app = Flask(__name__)
app.secret_key = '90f5bbad727de239db9ed3fc0bd633776ee6ca59e35e02c6'
model = app_data.Model()


@app.route('/')
@app.route('/index')
def index():
    session['index'] = 5
    print(session)
    return render_template("index.html",
                           user_history=model.user.history,
                           )


@app.route("/start/", methods=['POST'])
def start_test():
    model.update()
    print(session)
    return render_template("start.html",
                           pythonesses=model.pythonesses,
                           guess_min=model.guess_min,
                           guess_max=model.guess_max,
                           user_history=model.user.history,
                           )


@app.route("/resume/", methods=['POST'])
def resume_test():
    if request.method == 'POST':
        answer = request.form.get('answer')
        model.result(answer)
        print(session)
    return render_template("index.html",
                           user_history=model.user.history,
                           )


if __name__ == '__main__':
    app.run(debug=True)
