# Отдельная утилита создания БД пользователей (таблица user)
from dao.model.user import User, UserSchema
import sqlite3

# ################################ Копипаста из задания ################################
u1 = User(username="vasya", password="my_little_pony", role="user")
u2 = User(username="oleg", password="qwerty", role="user")
u3 = User(username="oleg", password="P@ssw0rd", role="admin")
# ######################################################################################
u4 = User(username="Monya", password="Biba", role="user")

us = list()
us.append(u1)
us.append(u2)
us.append(u3)
us.append(u4)

uss = UserSchema(many=True).dump(us)

# Подключение к БД
with sqlite3.connect('..\movies.db') as connection:
    cursor = connection.cursor()
    query = """CREATE TABLE IF NOT EXISTS user 
    (id INTEGER PRIMARY KEY NOT NULL, 
    username VARCHAR(255), 
    password VARCHAR(255), 
    role VARCHAR(255))"""
    cursor.execute(query)
    for i, u in enumerate(uss):
        query = f"""
        INSERT INTO user 
        VALUES ({i+1}, "{u['username']}", "{u['password']}", "{u['role']}")
        """
        cursor.execute(query)

    connection.commit()
