import hashlib
import os
from flask import Flask, render_template, request, session, url_for, redirect, abort
from base import check_user_exist, coups_mas, coup_mas, del_coup, data_user_reg, input_login, data_user, \
    user_update_coin, class_stud, user_rez, task_class, tasks_lec, answer_user, tasks_lec_rez, rez_coin, task_eval, \
    update_answer_coin, cards_corsers
from mail import send_mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fsa87asd782asd'

href_intr = ["../static/css/trade_intr.css", "../static/css/profile_intr.css", "../static/css/style_intr.css",
             "../static/css/reset_intr.css", "../static/css/courses_intr.css"]
href_extr = ["../static/css/trade_extr.css", "../static/css/profile_extr.css", "../static/css/style_extr.css",
             "../static/css/reset_extr.css", "../static/css/courses_extr.css"]
href_ambr = ["../static/css/trade_ambr.css", "../static/css/profile_ambr.css", "../static/css/style_ambr.css",
             "../static/css/reset_ambr.css", "../static/css/courses_ambr.css"]
type_css = {"Интроверт": href_intr, "Экстроверт": href_extr, "Амбиверт": href_ambr}


def generate_csrf_token():
    return hashlib.sha256(os.urandom(64)).hexdigest()

def generate_salt():
    return hashlib.sha256(os.urandom(32)).hexdigest()

def generate_password_hash(password, salt):
    return hashlib.sha3_256(str(password + salt).encode())

@app.route('/')
def base():
    if 'user_href' in session:
        return render_template('base.html', title="Главная", href=type_css[session['user_href']],
                               user=data_user(session['id_user']))
    return render_template('base.html', title="Главная", href=href_intr)


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('reg.html', title="Главная", href=href_intr, csrf_token=csrf_token)
    if request.method == "POST":
        if request.form['CSRFToken'] == session['csrf_token']:
            password = request['password']
            salt = generate_salt()
            password_hash = generate_password_hash(password, salt)
            req = (request.form['name'], request.form['surname'], request.form['fatherland'], request.form['login'],
                   password_hash, salt, request.form['pos'], request.form['s'], 0)
            if "Заполните поле!" in req or '' in req:
                return render_template('reg.html', error_text="Некоторые поля не заполнены", href=href_intr)
            if check_user_exist(request.form['login']):
                return render_template('reg.html', error_text="Этот e-mail уже зарегистрирован", href=href_intr)
            data_user_reg(list(req))
            return redirect('/login')
        else:
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            return render_template('reg.html', title="Главная", href=href_intr, csrf_token=csrf_token,
                                   error_text='Invalid cstf token')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('login.html', title="Авторизация", href=href_intr, csrf_token=csrf_token)
    if request.method == "POST":
        if request.form['CSRFToken'] == session['csrf_token']:
            request_login, request_password = request.form['login'], request.form['password']
            if not check_user_exist(request_login):
                return render_template('login.html', error_text="Этого пользователя не существует", href=href_intr)
            print(request_login)
            user_id, user_password, user_s, salt = input_login(request_login)[0]
            password_hash = generate_password_hash(request_password, salt)
            if user_password == password_hash:
                print(input_login(request_login)[0])
                session['id_user'] = user_id
                session['user_href'] = user_s
                print(input_login(session['user_href']))
                session['login_user'] = request_login
                return redirect(url_for('profile', username=session['login_user']))
        else:
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            return render_template('login.html', title="Авторизация", href=href_intr, csrf_token=csrf_token,
                                   error_text='Invalid cstf token')


@app.route('/mag', methods=['GET', 'POST'])
def mag():
    if request.method == "GET":
        if 'user_href' in session:
            return render_template('mag.html', title="Обменник", coup=coups_mas(), href=type_css[session['user_href']],
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
        return render_template('mag.html', title="Обменник", coup=coups_mas(), href=type_css[session['user_href']])


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    if 'id_user' not in session or session['login_user'] != username:
        abort(401)
    else:
        return render_template('profile.html', title="Личный кабинет", href=type_css[session['user_href']],
                               user=data_user(session['id_user']))


@app.route('/class/<id_class>', methods=['GET'])
def class_rez(id_class):
    session['id_class'] = 1
    if session['id_class'] == id_class:
        abort(401)
    else:
        stud = class_stud(session['id_class'])
        task = task_class(session['id_class'])
        print(stud)
        print(task)
        mas_studs = []
        for i in stud:
            mas_stud = []
            user = data_user(i[2])[0]
            mas_stud.append([str(user[1]) + " " + str(user[2]) + " " + str(user[3])])
            for j in range(len(task[0])):
                m = user_rez(i[2], task[0][j])
                if m != []:
                    true_count = m.count([(1,)])
                    mas_stud.append([str(true_count) + '/' + str(len(task[0][j])), task[1][j][0], i[2]])
                else:
                    mas_stud.append(['-/' + str(len(task[0][j]))])
            mas_studs.append(mas_stud)
        sh = ["ФИО"]
        for i in task[1]:
            sh.append(i[1])
        print(sh)
        print(mas_studs)
        return render_template('class.html', title="Результаты курса", href=href_intr, sh=sh, mas_studs=mas_studs)


@app.route('/tasks/<id_lecture>', methods=['GET', 'POST'])
def tasks(id_lecture):
    if request.method == "GET":
        session['id_lecture'] = 1
        if session['id_lecture'] == id_lecture:
            abort(401)
        else:
            mas = tasks_lec(id_lecture)
            return render_template('tasks.html', title="Задания к лекцие", href=href_intr, mas_tasks=mas)
    if request.method == "POST":
        print(request.form)
        session['id_user'] = 12
        for i in request.form:
            answer_user(session['id_user'], int(i), int(request.form[i].split("/")[1]))
        mas = task_eval(id_lecture, session['id_user'])
        for i in mas:
            if i[1] == i[3]:
                update_answer_coin(session['id_user'], i[3], i[2])
            else:
                update_answer_coin(session['id_user'], i[3], 0)
        return redirect(url_for('rez_tasks', id_lecture=id_lecture, id_user=session['id_user']))


@app.route('/rez_tasks/<id_lecture><id_user>', methods=['GET', 'POST'])
def rez_tasks(id_lecture, id_user):
    print(id_user)
    print(id_lecture)
    session['id_lecture'] = id_lecture
    if request.method == "GET":
        session['id_user'] = id_user
        mas = tasks_lec_rez(id_lecture, session['id_user'])
        rez_coins = rez_coin(id_lecture, session['id_user'])
        print(mas)
        return render_template('task_rez.html', title="Результаты заданий", href=href_intr, mas_tasks=mas,
                               rez_coin=rez_coins)


@app.route('/courses/course', methods=['GET', 'POST'])
def course():
    if request.method == "GET":
        return render_template('course.html', tittle="Курс", href=href_intr)


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == "GET":
        cards = cards_corsers()
        if 'user_href' in session:
            return render_template('courses.html', title="Курсы", count_courses=cards[0], courses=cards[1],
                                   href=type_css[session['user_href']], user=data_user(session['id_user']))
        return render_template('courses.html', title="Курсы", count_courses=cards[0], courses=cards[1], href=href_intr)


@app.route('/exit', methods=['GET'])
def exit():
    session.clear()
    return render_template('base.html', title="Главная", href=href_intr)


if __name__ == '__main__':
    app.run(debug=True)
