from flask import Flask, render_template, request, session, url_for, redirect, abort
from base import check_user_exist, coups_mas, coup_mas, del_coup, data_user_reg, input_login, data_user, user_update_coin
from mail import send_mail

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
               request.form['password'], request.form['s'], 0)
        if check_user_exist(request.form['login']):
            return render_template('reg.html', error_text="Этот e-mail уже зарегистрирован")
        data_user_reg(list(req))
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html', title="Авторизация")
    if request.method == "POST":
        print(request.form)
        req = (request.form['login'], request.form['password'])

        print(req[0])
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
        coup = coup_mas(id_coup)
        if 'id_user' not in session:
            return redirect(url_for('login', title="Aвторизация"))
        else:
            user = data_user(session['id_user'])
            if coup[0][-1] <= user[0][-1]:
                print(1)
                user_update_coin(session['id_user'], user[0][-1] - coup[0][-1])
                send_mail(user[0][4], coup[0][-2])
                del_coup(id_coup)
        return render_template("mag.html", coup=coups_mas())


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    if 'id_user' not in session or session['login_user'] != username:
        abort(401)
    else:
        return render_template('base.html', title="Главная")


if __name__ == '__main__':
    app.run(debug=True)
