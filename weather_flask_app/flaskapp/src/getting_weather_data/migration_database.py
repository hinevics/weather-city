# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# # Устанавливаем соединение с postgres
# connection = psycopg2.connect(user="postgres", password="1932")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# # Создаем курсор для выполнения операций с базой данных
# cursor = connection.cursor()
# # Создаем базу данных

# sql_create_database = cursor.execute('create database sqlalchemy_tuts')

# # Закрываем соединение
# cursor.close()
from sqlalchemy import create_engine
# connection.close()

# 1111 это мой пароль для пользователя postgres
engine = create_engine("postgresql+psycopg2://postgres:1932@localhost/sqlalchemy_tuts")
engine.connect()

print(engine)
