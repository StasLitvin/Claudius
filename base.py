import mysql.connector
from config import host, user, password, db_name

mas_q_a=[]

def data_con():
    """Подключение к БД"""
    return mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )


def coups_mas():
    """Возвращает массив купонов"""
    connection = data_con()
    cursor = connection.cursor()
    quary = '''SELECT * FROM coupons'''
    cursor.execute(quary)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


print(coups_mas())


def coup_mas(id):
    """Возвращает купон по id"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT * FROM coupons WHERE id="{id}"'''
    cursor.execute(quary)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def del_coup(id):
    """Удаленеи купона по id"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''DELETE FROM coupons WHERE id="{id}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()


def check_user_exist(email: str):
    """Проверка на наличие акккаунта с данной почтой"""
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT email FROM users WHERE email=(%s)'''
    cursor.execute(query, (email,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return len(result) > 0


def data_user_reg(data):
    """Создание пользователя по данным формы"""
    connection = data_con()
    cursor = connection.cursor()

    quary = '''INSERT INTO users(name,surname,fatherland,email,password,salt,pos,s,coin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(quary, data)
    connection.commit()
    cursor.close()
    connection.close()


def input_login(login):
    """Поиск данных пользователя по почте"""
    connection = data_con()
    cursor = connection.cursor()
    quary = '''SELECT id,password,s,salt FROM users WHERE email=%s'''
    cursor.execute(quary, (login,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def data_user(id):
    """Массви пользователя под данным id"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT * FROM users WHERE id="{id}"'''
    cursor.execute(quary)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def user_update_coin(id, coin):
    """Измененние количества баллов(пряников) по id пользователя"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''UPDATE users SET coin={coin} WHERE id="{id}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()
    return True


def class_stud(id_class):
    """Данные о пользователе на определёном курсе по id курса"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT * FROM classes_user WHERE id_classes="{id_class}"'''
    cursor.execute(quary)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def task_class(id_class):
    """Массив заданий к лекциям из курса по id курса"""
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT id,name FROM lectures WHERE id_class="{id_class}"'''
    cursor.execute(quary)
    result_lecture = cursor.fetchall()
    result_task = []
    for i in result_lecture:
        quary = f'''SELECT id FROM tasks WHERE id_lecture="{i[0]}"'''
        cursor.execute(quary)
        result_task.append(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    return [result_task, result_lecture]


def user_rez(id_user, mas_tasks):
    """Обработка данных для страницы статистики курса"""
    connection = data_con()
    cursor = connection.cursor()
    result_task = []
    for i in mas_tasks:
        quary = f'''SELECT id_answer FROM answer_user WHERE id_user="{id_user}" AND id_task="{i[0]}"'''
        cursor.execute(quary)
        result_task.append(cursor.fetchall())
    result = []
    if len(result_task) == 0:
        return []
    for i in result_task:
        if i == []:
            break
        quary = f'''SELECT true_task FROM answers WHERE id="{i[0][0]}"'''
        cursor.execute(quary)
        result.append(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    return result


def tasks_lec(id_lecture):
    """Массив задач по id лекции"""
    connection = data_con()
    cursor = connection.cursor()
    tasans = []
    quary = f'''SELECT id,task FROM tasks WHERE id_lecture="{id_lecture}"'''
    cursor.execute(quary)
    tasks = cursor.fetchall()
    for i in tasks:
        mas = [i[0], i[1]]
        quary = f'''SELECT id,answer FROM answers WHERE id_task="{i[0]}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall())
        tasans.append(mas)
    connection.commit()
    cursor.close()
    connection.close()
    return tasans


def answer_user(id_user, id_task, id_answer):
    """Запись ответа по трём id"""
    connection = data_con()
    cursor = connection.cursor()
    data = (id_user, id_answer, id_task)
    quary = '''INSERT INTO answer_user(id_user,id_answer,id_task) VALUES(%s,%s,%s)'''
    rez = cursor.execute(quary, data)
    connection.commit()
    cursor.close()
    connection.close()
    return rez


def tasks_lec_rez(id_lecture, id_user):
    """"""
    connection = data_con()
    cursor = connection.cursor()
    tasans = []
    quary = f'''SELECT id,task FROM tasks WHERE id_lecture="{id_lecture}"'''
    cursor.execute(quary)
    tasks = cursor.fetchall()
    for i in tasks:
        mas = [i[0], i[1]]
        quary = f'''SELECT id,answer FROM answers WHERE id_task="{i[0]}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall())
        quary = f'''SELECT id_answer FROM answer_user WHERE id_task="{i[0]}" AND id_user="{id_user}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall())
        tasans.append(mas)
    connection.commit()
    cursor.close()
    connection.close()
    return tasans


def rez_coin(id_lecture, id_user):
    connection = data_con()
    cursor = connection.cursor()
    tasans = []
    quary = f'''SELECT id,id_complexity FROM tasks WHERE id_lecture="{id_lecture}"'''
    cursor.execute(quary)
    tasks = cursor.fetchall()
    for i in tasks:
        mas = [i[0]]
        quary = f'''SELECT point FROM complexity WHERE id="{i[1]}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall()[0][0])
        print(i[0], id_user)
        quary = f'''SELECT coin FROM answer_user WHERE id_task="{i[0]}" AND id_user="{id_user}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall()[0][0])
        tasans.append(mas)
    connection.commit()
    cursor.close()
    connection.close()
    return tasans


def task_eval(id_lecture, id_user):
    connection = data_con()
    cursor = connection.cursor()
    tasans = []
    quary = f'''SELECT id,id_complexity FROM tasks WHERE id_lecture="{id_lecture}"'''
    cursor.execute(quary)
    tasks = cursor.fetchall()
    for i in tasks:
        mas = [i[0]]
        quary = f'''SELECT id FROM answers WHERE id_task="{i[0]}" AND true_task=1'''
        cursor.execute(quary)
        mas.append(cursor.fetchall()[0][0])
        quary = f'''SELECT point FROM complexity WHERE id="{i[1]}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall()[0][0])
        quary = f'''SELECT id_answer FROM answer_user WHERE id_task="{i[0]}" AND id_user="{id_user}"'''
        cursor.execute(quary)
        mas.append(cursor.fetchall()[0][0])
        tasans.append(mas)
    connection.commit()
    cursor.close()
    connection.close()
    return tasans


def update_answer_coin(id_user, id_answer, coin):
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''UPDATE answer_user SET coin="{coin}" WHERE id_user="{id_user}" AND id_answer="{id_answer}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()


def cards_corsers():
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT name,subject,lecture_count,users_count,img,id FROM classes'''
    cursor.execute(quary)
    rez = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return [len(rez), rez]


def cards_course(id):
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT name,subject,lecture_count,users_count,img,description FROM classes WHERE id="{id}"'''
    cursor.execute(quary)
    rez = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rez


def class_pre(id):
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''SELECT id_pre FROM classes WHERE id="{id}"'''
    cursor.execute(quary)
    rez = cursor.fetchall()[0][0]
    connection.commit()
    cursor.close()
    connection.close()
    return rez


def href_update(id_user, href_user, mas):
    connection = data_con()
    cursor = connection.cursor()
    if mas != []:
        quary = f'''UPDATE users SET s="{href_user}",name="{mas[1]}",surname="{mas[0]}", fatherland="{mas[2]}" WHERE id="{id_user}"'''
    else:
        quary = f'''UPDATE users SET s="{href_user}" WHERE id="{id_user}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()


def password_reset_token_create(user_id, token):
    connection = data_con()
    cursor = connection.cursor()
    data = user_id, token
    query = '''INSERT INTO password_reset_tokens (user_id,token) VALUES(%s,%s)'''
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()


def password_reset_token_find(token):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT user_id FROM password_reset_tokens WHERE token=(%s)'''
    cursor.execute(query, (token,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def update_password(user_id, new_hash, new_salt):
    connection = data_con()
    cursor = connection.cursor()
    data = (new_hash, new_salt, user_id)
    query = '''UPDATE users SET password=(%s), salt=(%s) WHERE id=(%s)'''
    cursor.execute(query, data)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def find_user_by_email(email):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT id FROM users WHERE email=(%s)'''
    cursor.execute(query, (email,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def name_lec(id_lecture):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT name FROM lectures WHERE id=(%s)'''
    cursor.execute(query, (id_lecture,))
    result = cursor.fetchall()[0][0]
    connection.commit()
    cursor.close()
    connection.close()
    return result


def user_course(id_course, id_user):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT passed FROM classes_user WHERE id_classes=(%s) AND id_user=(%s)'''
    cursor.execute(query, (id_course, id_user))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result

def update_user_course(id_course, id_user):
    connection = data_con()
    cursor = connection.cursor()
    query = '''INSERT INTO classes_user(id_classes,id_user,passed) VALUES(%s,%s,0)'''
    cursor.execute(query, (id_course, id_user))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result
def user_courses_count(id_user):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT id_classes, passed FROM classes_user WHERE id_user=(%s)'''
    cursor.execute(query, (id_user,))
    result = cursor.fetchall()
    for i in range(len(result)):
        print(result[i])
        quary = f'''SELECT name,subject,lecture_count,users_count,img,description FROM classes WHERE id="{result[i][0]}"'''
        cursor.execute(quary)
        print(result[i][0])
        result[i] += cursor.fetchall()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return result
def max_id():
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT id FROM classes WHERE id=(SELECT MIN(id) FROM classes WHERE id>1)'''
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result
print(max_id())

def name_cours_id_lect(id_lecture):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT id_class FROM lectures WHERE id=(%s)'''
    cursor.execute(query, (id_lecture,))
    result = cursor.fetchall()[0][0]
    query = '''SELECT name FROM classes WHERE id=(%s)'''
    cursor.execute(query, (result,))
    result_name = cursor.fetchall()[0][0]
    connection.commit()
    cursor.close()
    connection.close()
    return result_name
def mas_lecture(id_class):
    connection = data_con()
    cursor = connection.cursor()
    query = '''SELECT id, name,lecture FROM lectures WHERE id_class=(%s)'''
    cursor.execute(query, (id_class,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result
def update_progress(id_class,id_user,progress):
    connection = data_con()
    cursor = connection.cursor()
    query = '''UPDATE classes_user SET passed=(%s)  WHERE id_classes=(%s) and id_user=(%s)'''
    cursor.execute(query, (progress,id_class,id_user))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result