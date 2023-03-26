import mysql.connector
from config import host, user, password, db_name


def data_con():
    return mysql.connector.connect(
        host=host,
        port=3360,
        user=user,
        password=password,
        database=db_name
    )


def coups_mas():
    connection = data_con()
    cursor = connection.cursor()
    quary = '''SELECT * FROM coupons'''
    cursor.execute(quary)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def coup_mas(id):
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
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''DELETE FROM coupons WHERE id="{id}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()


def check_user_exist(email: str):
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
    connection = data_con()
    cursor = connection.cursor()

    quary = '''INSERT INTO users(name,surname,fatherland,email,password,pos,s,coin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(quary, data)
    connection.commit()
    cursor.close()
    connection.close()


def input_login(login):
    connection = data_con()
    cursor = connection.cursor()
    quary = '''SELECT id,password,s FROM users WHERE email=%s'''
    cursor.execute(quary, (login,))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result


def data_user(id):
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
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''UPDATE users SET coin={coin} WHERE id="{id}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()
    return True


def class_stud(id_class):
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


