import mysql.connector
from config import host, user, password, db_name


def coups_mas():
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    quary = '''SELECT * FROM coupons'''
    cursor.execute(quary)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def coup_mas(id):
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    quary = f'''SELECT * FROM coupons WHERE id="{id}"'''
    cursor.execute(quary)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def del_coup(id):
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    quary = f'''DELETE coupons WHERE id="{id}"'''
    cursor.execute(quary)
    cursor.close()
    connection.close()


def data_user_reg(data):
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()

    quary = '''INSERT INTO users(name,surname,fatherland,email,password,pos,s,coin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(quary, data)
    connection.commit()
    cursor.close()
    connection.close()


def input_login(login):
    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    quary = '''SELECT id,password FROM users WHERE email=%s'''
    cursor.execute(quary, (login, ))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result