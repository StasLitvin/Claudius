from flask import Flask, render_template, request, session, url_for, redirect, abort
from base import coups_mas, coup_mas, del_coup, data_user_reg, input_login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fsa87asd782asd'


@app.route('/')
def base():
    return render_template('base.html', title="Главная")


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        return render_template('reg.html', title="Регистарция")
    if request.method == "POST":
        req = (request.form['name'], request.form['surname'], request.form['fatherland'], request.form['login'],
               request.form['password'], request.form['pos'], request.form['s'], 0)
        data_user_reg(list(req))
        return render_template('login.html', title="Авторизация")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html', title="Авторизация")
    if request.method == "POST":
        req = (request.form['login'], request.form['password'])
        print(req)
        if input_login(req[0])[0][1] == req[1]:
            print(input_login(req[0])[0])
            session['id_user'] = input_login(req[0])[0][0]
            session['login_user'] = req[0]
            return redirect(url_for('profile', username=req[0]))
        return render_template('login.html', title="Авторизация")


@app.route('/mag', methods=['GET', 'POST'])
def mag():
    if request.method == "GET":
        return render_template("mag.html", coup=coups_mas())
    elif request.method == "POST":
        id_coup = request.form['id_coup']
        coup_mas(id_coup)
        if 1 == 0:  # Вот тут должно быть обращение к базе данных пользователя сесси
            # и далее проверка баллов и соответсвенно удаление купона из БД и отправка
            del_coup(id_coup)
        return render_template("mag.html", coup=coups_mas())


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    if 'id_user' not in session or session['login_user'] != username:
        abort(401)
    else:
        return "ЛК"


if __name__ == '__main__':
    app.run(debug=True)
