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

    quary = '''INSERT INTO users(name,surname,fatherland,email,password,s,coin) VALUES(%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(quary, data)
    connection.commit()
    cursor.close()
    connection.close()


def input_login(login):
    connection = data_con()
    cursor = connection.cursor()
    quary = '''SELECT id,password FROM users WHERE email=%s'''
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

def user_update_coin(id,coin):
    connection = data_con()
    cursor = connection.cursor()
    quary = f'''UPDATE users SET coin={coin} WHERE id="{id}"'''
    cursor.execute(quary)
    connection.commit()
    cursor.close()
    connection.close()
    return True