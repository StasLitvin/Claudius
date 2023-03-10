from flask import Flask, render_template, request, session, url_for, redirect, abort
from base import check_user_exist, coups_mas, coup_mas, del_coup, data_user_reg, input_login, data_user, \
    user_update_coin
from mail import send_mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fsa87asd782asd'

href_intr = ["../static/css/trade_intr.css", "../static/css/profile_intr.css", "../static/css/style_intr.css",
             "../static/css/reset_intr.css"]
href_extr = ["../static/css/trade_extr.css", "../static/css/profile_extr.css", "../static/css/style_extr.css",
             "../static/css/reset_extr.css"]


@app.route('/')
def base():
    if 'user_href' in session:
        if session['user_href'] == "Экстроверт":
            return render_template('base.html', title="Главная", href=href_extr, user=data_user(session['id_user']))
        if session['user_href'] == "Интроверт":
            return render_template('base.html', title="Главная", href=href_intr, user=data_user(session['id_user']))
    return render_template('base.html', title="Главная", href=href_intr)


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        return render_template('reg.html', title="Главная", href=href_intr)
    if request.method == "POST":

        req = (request.form['name'], request.form['surname'], request.form['fatherland'], request.form['login'],
               request.form['password'], request.form['pos'], request.form['s'], 0)
        if "Заполните поле!" in req or '' in req:
            return render_template('reg.html', error_text="Некоторые поля не заполнены", href=href_intr)
        if check_user_exist(request.form['login']):
            return render_template('reg.html', error_text="Этот e-mail уже зарегистрирован", href=href_intr)
        data_user_reg(list(req))
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        return render_template('login.html', title="Авторизация", href=href_intr)
    if request.method == "POST":
        print(request.form)
        req = (request.form['login'], request.form['password'])
        if not check_user_exist(request.form['login']):
            return render_template('login.html', error_text="Этого пользователя не существует")
        print(req[0])
        if input_login(req[0])[0][1] == req[1]:
            print(input_login(req[0])[0])
            session['id_user'] = input_login(req[0])[0][0]
            session['user_href'] = input_login(req[0])[0][2]
            print(input_login(session['user_href']))
            session['login_user'] = req[0]
            return redirect(url_for('profile', username=session['login_user']))
        return render_template('login.html', title="Авторизация", href=href_intr)


@app.route('/mag', methods=['GET', 'POST'])
def mag():
    if request.method == "GET":
        if 'user_href' in session:
            if session['user_href'] == "Экстроверт":
                return render_template('mag.html', coup=coups_mas(), title="Обменник", href=href_extr,
                                       user=data_user(session['id_user']))
            if session['user_href'] == "Интроверт":
                return render_template('mag.html', coup=coups_mas(), title="Обменник", href=href_intr,
                                       user=data_user(session['id_user']))
        return render_template("mag.html", coup=coups_mas(), title="Обменник", href=href_intr)
    if request.method == "POST":
        id_coup = request.form['id_coup']
        coup = coup_mas(id_coup)

        if 'id_user' not in session:
            return redirect(url_for('login', title="Aвторизация", href=href_intr))
        else:
            user = data_user(session['id_user'])
            if coup[0][-1] <= user[0][-1]:
                user_update_coin(session['id_user'], user[0][-1] - coup[0][-1])
                send_mail(user[0][4], coup[0][-2])
                del_coup(id_coup)
        if session['user_href'] == "Экстроверт":
            return render_template('mag.html', coup=coups_mas(), title="Обменник", href=href_extr,
                                   user=data_user(session['id_user']))
        if session['user_href'] == "Интроверт":
            return render_template('mag.html', coup=coups_mas(), title="Обменник", href=href_intr,
                                   user=data_user(session['id_user']))
        return render_template("mag.html", coup=coups_mas(), title="Обменник", href=href_intr)


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    if 'id_user' not in session or session['login_user'] != username:
        abort(401)
    else:
        print(session['user_href'])
        if session['user_href'] == "Экстроверт":
            return render_template('profile.html', title="Главная", href=href_extr, user=data_user(session['id_user']))
        if session['user_href'] == "Интроверт":
            return render_template('profile.html', title="Главная", href=href_intr, user=data_user(session['id_user']))


@app.route('/exit', methods=['GET'])
def exit():
    session.clear()
    return render_template('base.html', title="Главная", href=href_intr)


if __name__ == '__main__':
    app.run(debug=True)
