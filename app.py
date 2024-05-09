import hashlib
import os
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS, mas_test_lich
from main import rezult_test_lic
from flask import Flask, render_template, request, session, url_for, redirect, abort, jsonify
from flask_session import Session
from base import check_user_exist, coups_mas, coup_mas, del_coup, data_user_reg, input_login, data_user, \
    password_reset_token_find, update_password, \
    user_update_coin, class_stud, user_rez, task_class, tasks_lec, answer_user, tasks_lec_rez, rez_coin, task_eval, \
    update_answer_coin, cards_corsers, cards_course, class_pre, href_update, password_reset_token_create, \
    find_user_by_email, name_lec, user_course, update_user_course, user_courses_count, name_cours_id_lect, mas_lecture, \
    update_progress, faq_mas, leaders, icons, icon_users, type_href, type_update
from werkzeug.utils import secure_filename
from mail import send_mail, send_password_reset_mail
import joblib
from model import pipe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fsa87asd782asd'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


href_intr = "../static/intr.css"
href_extr = "../static/extr.css"
href_ambr = "../static/ambr.css"

href_intr_t = "../static/intr_t.css"
href_extr_t = "../static/extr_t.css"
href_ambr_t = "../static/ambr_t.css"

type_css = {"Интроверт": href_intr, "Экстраверт": href_extr, "Амбиверт": href_ambr}
type_css_t = {"Интроверт": href_intr_t, "Экстраверт": href_extr_t, "Амбиверт": href_ambr_t}
type_svg = {"Интроверт": "intr", "Экстраверт": "extr", "Амбиверт": "ambr"}
svg_t = {0: "#000", 1: "#FFF"}
svg_prog = {0: "", 1: "_t"}
svg_icons = {0: "", 1: "nightshift_"}


def type_href_css(type, href):
    if type == 0:
        return type_css[href]
    else:
        return type_css_t[href]


def generate_csrf_token():
    return hashlib.sha256(os.urandom(64)).hexdigest()


def generate_salt():
    return hashlib.sha256(os.urandom(32)).hexdigest()


def generate_password_reset_token():
    return hashlib.sha256(os.urandom(64)).hexdigest()


def generate_password_hash(password, salt):
    return hashlib.sha3_256(str(password + salt).encode()).hexdigest()


@app.route('/get_test_data', methods=['GET', 'POST'])
def get_test_data():
    if request.method == "GET":
        return mas_test_lich.json()


@app.route('/', methods=['GET', 'POST'])
def base():
    if request.method == "GET" and 'tasks_test_lich' not in session:
        session['tasks_test_lich'] = mas_test_lich
        session['now_task_test_lich'] = 1
        session['count_tasks_test_lich'] = len(session['tasks_test_lich'])
        session['tasks_test_lich_rez'] = [' '] * session['count_tasks_test_lich']
    if request.method == "POST":
        print(request.form)
        if 'back' in request.form and session['now_task_test_lich'] > 1:
            session['tasks_test_lich_rez'][session['now_task_test_lich'] - 1] = request.form['radio']
            session['now_task_test_lich'] -= 1
        if 'next' in request.form and session['now_task_test_lich'] < session['count_tasks_test_lich']:
            session['tasks_test_lich_rez'][session['now_task_test_lich'] - 1] = request.form['radio']
            session['now_task_test_lich'] += 1
        if 'finish' in request.form:
            session['tasks_test_lich_rez'][session['now_task_test_lich'] - 1] = request.form['radio']
            rezult = rezult_test_lic(session['tasks_test_lich_rez'])
            session['tasks_test_lich_rez'] = [' '] * session['count_tasks_test_lich']
            session['now_task_test_lich'] = 1
            if rezult == "Интроверт":
                return redirect(url_for("introvert"))
            if rezult == "Экстраверт":
                return redirect(url_for("extrovert"))
            if rezult == "Амбиверт":
                return redirect(url_for("ambivert"))
    if 'user_href' in session:
        session['type_href'] = type_href(session['id_user'])
        return render_template('main.html', title="Главная",
                               href=type_href_css(session['type_href'], session['user_href']),
                               user=data_user(session['id_user']),
                               task=session['tasks_test_lich'][session['now_task_test_lich'] - 1],
                               count_tasks=session['count_tasks_test_lich'], now_task=session['now_task_test_lich'],
                               rez_task=session['tasks_test_lich_rez'][session['now_task_test_lich'] - 1],
                               navig=["Главная"], href_svg=type_svg[session['user_href']],
                               svg_t=svg_t[session['type_href']], svg_prog=svg_prog[session['type_href']])
    return render_template('main.html', title="Главная", href=href_intr,
                           task=session['tasks_test_lich'][session['now_task_test_lich'] - 1],
                           count_tasks=session['count_tasks_test_lich'], now_task=session['now_task_test_lich'],
                           rez_task=session['tasks_test_lich_rez'][session['now_task_test_lich'] - 1],
                           navig=["Главная"], href_svg="intr", svg_t=svg_t[0])


@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('reg.html', title="Главная", href=href_intr, csrf_token=csrf_token,
                               navig=["Авторизация"])
    if request.method == "POST":
        if request.form['CSRFToken'] == session['csrf_token']:
            password = request.form['password']
            salt = generate_salt()
            password_hash = generate_password_hash(password, salt)
            req = (request.form['name'], request.form['surname'], request.form['fatherland'], request.form['login'],
                   password_hash, salt, request.form['pos'], request.form['s'], 0)
            if "Заполните поле!" in req or '' in req:
                return render_template('reg.html', error_text="Некоторые поля не заполнены", href=href_intr,
                                       navig=["Авторизация"], svg_t=svg_t[0])
            if check_user_exist(request.form['login']):
                return render_template('reg.html', error_text="Этот e-mail уже зарегистрирован", href=href_intr,
                                       navig=["Авторизация"], svg_t=svg_t[0])
            data_user_reg(list(req))
            return redirect('/login')
        else:
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            return render_template('reg.html', title="Главная", href=href_intr, csrf_token=csrf_token,
                                   error_text='Invalid cstf token', navig=["Авторизация"], svg_t=svg_t[0])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'id_user' in session:
            return redirect(url_for('profile', username=session['login_user']))
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('login.html', title="Авторизация", href=href_intr, csrf_token=csrf_token,
                               navig=["Авторизация"])
    if request.method == "POST":
        if request.form['CSRFToken'] == session['csrf_token']:
            request_login, request_password = request.form['login'], request.form['password']
            if not check_user_exist(request_login):
                return render_template('login.html', error_text="Этого пользователя не существует", href=href_intr,
                                       navig=["Авторизация"])
            print(request_login)
            user_id, user_password, user_s, salt = input_login(request_login)[0]
            password_hash = generate_password_hash(request_password, salt)
            if user_password == password_hash:
                print(input_login(request_login)[0])
                session['id_user'] = user_id
                session['user_href'] = user_s
                session['type_href'] = type_href(session['id_user'])
                print(input_login(session['user_href']))
                session['login_user'] = request_login
                return redirect(url_for('profile', username=session['login_user']))
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            return render_template('login.html', href=href_intr, csrf_token=csrf_token,
                                   error_text='Неправильный логин или пароль.', navig=["Авторизация"])
        else:
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            return render_template('login.html', title="Авторизация", href=href_intr, csrf_token=csrf_token,
                                   error_text='Invalid cstf token', navig=["Авторизация"])


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('forgot_password.html', href=href_intr, csrf_token=csrf_token, password_not_reset=True,
                               navig=["Авторизация", "Восстановление пароля"])
    if request.method == 'POST':
        if request.form['CSRFToken'] == session['csrf_token']:
            if 'email' in request.form:
                email = request.form['email']
                if check_user_exist(email):
                    token = generate_password_reset_token()
                    password_reset_token_create(find_user_by_email(email)[0][0], token)
                    send_password_reset_mail(email, token)
                    print('sent')
                    return render_template('forgot_password.html', href=href_intr,
                                           navig=["Авторизация", "Восстановление пароля"])
                return render_template('forgot_password.html', href=href_intr,
                                       navig=["Авторизация", "Восстановление пароля"])
        return render_template('forgot_password.html', href=href_intr,
                               error_text="Что-то пошло не так...<br>Invalid CSRF token.",
                               navig=["Авторизация", "Восстановление пароля"])


@app.route('/forgot_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'GET':
        user = password_reset_token_find(token)
        if len(user) > 0:
            csrf_token = generate_csrf_token()
            session['csrf_token'] = csrf_token
            session['user_id'] = user[0][0]
            return render_template('password_reset.html', href=href_intr, csrf_token=csrf_token,
                                   navig=["Авторизация", "Восстановление пароля"])
        return render_template('password_reset.html', href=href_intr,
                               error_text="Что-то пошло не так...<br>Invalid password reset token.",
                               navig=["Авторизация", "Восстановление пароля"])
    if request.method == 'POST':
        if request.form['CSRFToken'] == session['csrf_token']:
            if 'password' in request.form:
                password = request.form['password']
                salt = generate_salt()
                password_hash = generate_password_hash(password, salt)
                update_password(session['user_id'], password_hash, salt, )
                return redirect('/login')
            return render_template('password_reset.html', href=href_intr,
                                   error_text="Что-то пошло не так...<br>Password empty.")
        return render_template('password_reset.html', href=href_intr,
                               error_text="Что-то пошло не так...<br>Invalid CSRF token.")


@app.route('/mag', methods=['GET', 'POST'])
def mag():
    if request.method == "GET":
        if 'user_href' in session:
            return render_template('mag.html', title="Система поощерения", coup=coups_mas(),
                                   href=type_href_css(session['type_href'], session['user_href']),
                                   user=data_user(session['id_user']), navig=["Система поощерения"],
                                   svg_t=svg_t[session['type_href']])
        return render_template("mag.html", coup=coups_mas(), title="Система поощерения", href=href_intr,
                               navig=["Система поощерения"], svg_t=svg_t[0])
    if request.method == "POST":
        id_coup = request.form['id_coup']
        coup = coup_mas(id_coup)

        if 'id_user' not in session:
            return redirect(url_for('login', title="Aвторизация", href=href_intr))
        else:
            user = data_user(session['id_user'])
            print(user)
            print(coup)
            if coup[0][-1] <= user[0][-2]:
                user_update_coin(session['id_user'], user[0][-2] - coup[0][-1])
                del_coup(id_coup)
        return render_template('mag.html', title="Обменник", coup=coups_mas(),
                               href=type_href_css(session['type_href'], session['user_href']),
                               navig=["Обменник"], svg_t=svg_t[session['type_href']])


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'id_user' not in session:
        return redirect(url_for('login', title="Aвторизация", href=href_intr))
    else:
        if request.method == "POST":
            print(request.form['nick'])
            print(request.form)
            session['user_href'] = request.form['emotional_condition']
            session['type_href'] = int(request.form['type-condition'])
            if len(request.form['nick'].split(" ")) == 3:
                href_update(session['id_user'], session['user_href'], request.form['nick'].split(" "))
            else:
                href_update(session['id_user'], session['user_href'], [])
            type_update(session['id_user'], session['type_href'])
        k = user_courses_count(session["id_user"])
        passed_true = 0
        passed_false = 0
        if len(k) == 0:
            k = 0
        else:
            for i in k:
                if i[1] < 100:
                    passed_false += 1
                else:
                    passed_true += 1
        return render_template('profile.html', title="Личный кабинет",
                               href=type_href_css(session['type_href'], session['user_href']),
                               user=data_user(session['id_user'])[0], navig=["Личный кабинет"], courses=k,
                               passed_true=passed_true, passed_false=passed_false,
                               href_svg=type_svg[session['user_href']], svg_t=svg_t[session['type_href']],
                               svg_prog=svg_prog[session['type_href']], svg_icons=svg_icons[session['type_href']])


@app.route('/class/<id_class>', methods=['GET'])
def class_rez(id_class):
    print(class_pre(id_class))
    if 'id_user' not in session:
        return redirect(url_for('login'))
    if int(session['id_user']) != class_pre(id_class):
        abort(401)
    else:
        stud = class_stud(id_class)
        task = task_class(id_class)
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
        return render_template('class.html', title="Результаты курса",
                               href=type_href_css(session['type_href'], session['user_href']), sh=sh,
                               mas_studs=mas_studs,
                               navig=["Результаты курса"])


@app.route('/tasks/<id_lecture>', methods=['GET', 'POST'])
def tasks(id_lecture):
    if 'id_user' not in session:
        return redirect(url_for('login'))

    test = 'tasks_test_' + str(id_lecture)
    count = 'count_tasks_test_' + str(id_lecture)
    now = 'now_task_test_' + str(id_lecture)
    rez = 'tasks_test_rez_' + str(id_lecture)
    print(session.keys())
    if request.method == "GET":
        session[test] = tasks_lec(id_lecture)
        session[now] = 1
        session[count] = len(session[test])
        session[rez] = [0] * session[count]
    if request.method == "POST":
        print(request.form)
        if 'back' in request.form:
            session[rez][session[now] - 1] = int(request.form['radio'])
            session[now] -= 1
        if 'next' in request.form and session[now] < session[count]:
            print("N")
            session[rez][session[now] - 1] = int(request.form['radio'])
            session[now] += 1
        print(session[rez])
        if 'finish' in request.form:
            session[rez][session[now] - 1] = request.form['radio']
            for i in range(session[count]):
                print(session['id_user'], session[test][i][0], session[rez][i])
                answer_user(session['id_user'], session[test][i][0], session[rez][i])
            mas = task_eval(id_lecture, session['id_user'])

            for i in mas:
                if i[1] == i[3]:
                    update_answer_coin(session['id_user'], i[3], i[2])
                else:
                    update_answer_coin(session['id_user'], i[3], 0)
            session[rez] = [' '] * session[count]
            session[now] = 1
            print(session['id_user'])
            return redirect(url_for('rez_tasks', id_lecture=id_lecture, id_user=session['id_user']))
    print(session[test])
    return render_template('tasks.html', title="Главная",
                           href=type_href_css(session['type_href'], session['user_href']),
                           lecture=name_lec(id_lecture),
                           user=data_user(session['id_user']),
                           task=session[test][session[now] - 1],
                           count_tasks=session[count], now_task=session[now],
                           rez_task=session[rez][session[now] - 1], navig=["Тест к лекции"])


@app.route('/rez_tasks/<id_lecture>&<id_user>', methods=['GET', 'POST'])
def rez_tasks(id_lecture, id_user):
    if 'id_user' not in session:
        return redirect(url_for('login'))
    if session['id_user'] != int(id_user):
        abort(401)
    test = 'tasks_test_' + 'rez' + str(id_lecture)
    count = 'count_tasks_test_' + 'rez' + str(id_lecture)
    now = 'now_task_test_' + 'rez' + str(id_lecture)
    rez = 'tasks_test_rez_' + 'rez' + str(id_lecture)

    if request.method == "GET" and test not in session:
        print("GET")
        session[test] = tasks_lec_rez(id_lecture, session['id_user'])
        session[now] = 1
        session[count] = len(session[test])
        session[rez] = rez_coin(id_lecture, session['id_user'])

    print(session.keys())
    if request.method == "POST":
        print(request.form)
        if 'back' in request.form and session[now] > 1:
            print("B")
            session[now] -= 1
        if 'next' in request.form and session[now] < session[count]:
            print("N")
            session[now] += 1
            print('сейчас', session[now])

        print(session[rez])
        print('количество', session[count])
    session.modified = True
    return render_template('task_rez2.html', title="Результаты заданий",
                           href=type_href_css(session['type_href'], session['user_href']),
                           lecture=name_lec(id_lecture),
                           user=data_user(session['id_user']),
                           i=session[test][session[now] - 1],
                           r=session[rez][session[now] - 1],
                           count_tasks=session[count], now_task=session[now],
                           rez_task=session[rez][session[now] - 1], navig=["Результаты теста к лекции"],
                           svg_prog=svg_prog[session['type_href']])


@app.route('/courses/<id_course>', methods=['GET', 'POST'])
def course(id_course):
    if request.method == "GET":

        if 'user_href' in session and 'id_user' in session:
            stat = user_course(id_course, session["id_user"])
            if len(stat) == 0:
                stat = "Начать"
                rez = 0
            else:
                stat = "Продолжить"
                rez = user_course(id_course, session["id_user"])[0][0]
            print(stat)
            return render_template('course.html', tittle=cards_course(id_course)[0][0],
                                   href=type_href_css(session['type_href'], session['user_href']),
                                   course=cards_course(id_course)[0],
                                   navig=["Курсы", cards_course(id_course)[0][0]], course_nach=stat,
                                   id_course=id_course, rez=rez, id_u=session["id_user"],
                                   href_svg=type_svg[session['user_href']])

        return render_template('course.html', tittle=cards_course(id_course)[0][0], href=href_intr,
                               course=cards_course(id_course)[0],
                               navig=["Курсы", cards_course(id_course)[0][0]], href_svg="intr")

    elif request.method == "POST":
        if 'user_href' in session and 'id_user' in session:
            stat = user_course(id_course, session["id_user"])
            if len(stat) == 0:
                update_user_course(id_course, session["id_user"])
            return redirect(url_for('course', id_course=id_course))
        return redirect(url_for('reg'))


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == "GET":
        cards = cards_corsers()
        if 'user_href' in session:
            return render_template('courses.html', title="Курсы", count_courses=cards[0], courses=cards[1],
                                   href=type_href_css(session['type_href'], session['user_href']),
                                   user=data_user(session['id_user']),
                                   navig=["Курсы"], href_svg=type_svg[session['user_href']])
        return render_template('courses.html', title="Курсы", count_courses=cards[0], courses=cards[1],
                               href=href_intr, navig=["Курсы"], href_svg="intr")
    if request.method == "POST":
        cards = cards_corsers()[1]
        cards_true = []
        for i in cards:
            if request.form["search__input"].lower().replace("  ", " ") in i[0].lower():
                cards_true += [i]
        print(cards_true)
        if 'user_href' in session:
            return render_template('courses.html', title="Курсы", count_courses=len(cards_true), courses=cards_true,
                                   href=type_href_css(session['type_href'], session['user_href']),
                                   user=data_user(session['id_user']),
                                   navig=["Курсы"], href_svg=type_svg[session['user_href']])
        return render_template('courses.html', title="Курсы", count_courses=len(cards_true), courses=cards_true,
                               href=href_intr, navig=["Курсы"], href_svg="intr")


@app.route('/down', methods=['GET', 'POST'])
def down():
    if request.method == "GET":
        print(0)
        return render_template('down.html', name="NO")
    elif request.method == 'POST':
        print(request.files)
        file = request.files['imges']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('down.html', name=filename, mas_test_lich=mas_test_lich)


@app.route('/exit', methods=['GET'])
def exit():
    session.clear()
    return redirect(url_for('base'))


@app.route('/course_down', methods=['GET', 'POST'])
def course_down():
    if request.method == 'POST':
        print(1, request.form)
        return render_template('course_down.html', title="Курсы", href=href_intr, navig=["Курсы"])
    return render_template('course_down.html', title="Курсы", href=href_intr, navig=["Курсы"])


@app.route('/ambivert', methods=['GET', 'POST'])
def ambivert():
    if request.method == 'POST':
        print(1, request.form)
        return render_template('ambivert.html', title="Амбиверт", href=href_ambr,
                               navig=["Описание типа личности", "Амбиверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                               svg_icons=svg_icons[0])
    return render_template('ambivert.html', title="Амбиверт", href=href_ambr,
                           navig=["Описание типа личности", "Амбиверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                           svg_icons=svg_icons[0])


@app.route('/introvert', methods=['GET', 'POST'])
def introvert():
    if request.method == 'POST':
        print(1, request.form)
        return render_template('introvert.html', title="Интроверт", href=href_intr,
                               navig=["Описание типа личности", "Интроверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                               svg_icons=svg_icons[0])
    return render_template('introvert.html', title="Интроверт", href=href_intr,
                           navig=["Описание типа личности", "Интроверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                           svg_icons=svg_icons[0])


@app.route('/extrovert', methods=['GET', 'POST'])
def extrovert():
    if request.method == 'POST':
        print(1, request.form)
        return render_template('extrovert.html', title="Экстраверт", href=href_extr,
                               navig=["Описание типа личности", "Экстраверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                               svg_icons=svg_icons[0])
    return render_template('extrovert.html', title="Экстраверт", href=href_extr,
                           navig=["Описание типа личности", "Экстраверт"], svg_t=svg_t[0], svg_prog=svg_prog[0],
                           svg_icons=svg_icons[0])


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    message = request.json['message']

    return jsonify({'message': pipe.predict([str(message)])[0]})


@app.route('/chat_bot', methods=['GET'])
def chat_bot():
    if 'user_href' in session:
        return render_template('chat.html', title="Чат-бот",
                               href=type_href_css(session['type_href'], session['user_href']),
                               user=data_user(session['id_user']),
                               navig=["Чат-бот"])
    return render_template('chat.html', title="Чат-бот", href=href_intr,
                           navig=["Чат-бот"])


@app.route('/faq', methods=['GET', 'POST'])
def fag():
    type_fill = {"Интроверт": "#E3F9FF", "Экстраверт": "#90817C", "Амбиверт": "#FFC501"}
    if 'user_href' in session:
        return render_template('fag.html', title="Чат-бот",
                               href=type_href_css(session['type_href'], session['user_href']),
                               fill=type_fill[session['user_href']],
                               user=data_user(session['id_user']),
                               navig=["Часто задаваемые вопросы"],
                               mas_q_a=faq_mas())
    return render_template('fag.html', title="Чат-бот", href=href_intr,
                           navig=["Часто задаваемые вопросы"], fill="#E3F9FF", mas_q_a=faq_mas())


@app.route('/rez_cour/<id_lecture>&<id_user>', methods=['GET'])
def rez_cours(id_lecture, id_user):
    print(rez_coin(id_lecture, session['id_user']))
    if 'id_user' not in session:
        return redirect(url_for('login'))
    if session['id_user'] != int(id_user):
        abort(401)
    if request.method == "GET":
        sum_coin = 0
        all_coin = 0
        for i in rez_coin(id_lecture, session['id_user']):
            sum_coin += i[2]
            all_coin += i[1]
        n = name_lec(id_lecture)
        cours = name_cours_id_lect(id_lecture)
        return render_template('rez_cours.html', title="Просмотр попыток",
                               href=type_href_css(session['type_href'], session['user_href']),
                               navig=["Мои курсы", cours, n], name_lec=n, rez_coin=sum_coin, all_coin=all_coin,
                               i_l=id_lecture, i_u=id_user)


@app.route('/cours_mas/<id_class>&<id_user>', methods=['GET'])
def cours_mas(id_class, id_user):
    if 'id_user' not in session:
        return redirect(url_for('login'))
    if session['id_user'] != int(id_user):
        abort(401)
    if request.method == "GET":
        mas_inf = []
        allsum_coin = 0
        allcoin = 0
        for j in mas_lecture(id_class):
            id_lecture = j[0]
            sum_coin = 0
            all_coin = 0
            for i in rez_coin(id_lecture, session['id_user']):
                sum_coin += i[2]
                all_coin += i[1]
            allsum_coin += sum_coin
            allcoin += all_coin
            mas_inf.append([j[0], j[1], j[2], sum_coin, all_coin])
        cours = name_cours_id_lect(id_lecture)
        update_progress(id_class, id_user, int(allsum_coin / allcoin * 100))
        return render_template('cours_lec_task.html', title="Материалы курса",
                               href=type_href_css(session['type_href'], session['user_href']),
                               navig=["Мои курсы", cours], mas_inf=mas_inf, name_cours=cours, i_u=id_user,
                               progress=int(allsum_coin / allcoin * 100))


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    if request.method == "GET":
        board = leaders()
        return render_template('leaderboard.html', title="Главная",
                               href=type_href_css(session['type_href'], session['user_href']),
                               navig=["Таблица лидеров"], board=board)


@app.route('/icons/<id_user>', methods=['GET'])
def test(id_user):
    if 'id_user' in session:
        id_user = id_user

        return render_template('icons.html', href=type_href_css(session['type_href'], session['user_href']),
                               title="Достижения", icons=icons(),
                               navig=["Достижения"], href_svg=type_svg[session['user_href']], i_u=icon_users(id_user),
                               svg_t=svg_t[session['type_href']], svg_prog=svg_prog[session['type_href']],
                               svg_icons=svg_icons[session['type_href']])

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
