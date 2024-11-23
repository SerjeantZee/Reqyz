from config import Config
import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        dbname = Config.name,
        host = Config.host,
        password = Config.password,
        user = Config.user
        )

    cursor = connection.cursor()

#
#    sql = '''
#        CREATE TABLE users (
#            id SERIAL PRIMARY KEY,
#            login VARCHAR(20),
#            name VARCHAR(30),
#            surname VARCHAR(30),
#            id_role INTEGER,
#            tel INTEGER
#        )
#    '''

#    pips = [
#        ('admin', 'Владислав', 'Сизов'),
#        ('admin2', 'Саня', 'Бубунов')
#    ]
#    
#    cursor.executemany(
#        "INSERT INTO users (login, name, surname) VALUES (%s, %s, %s)",
#        pips
#    )
#    connection.commit()
#    print("Выполнено! ")

#    posts = [
#        (
#            'Поздравляем с первой записью!',
#            'Это маленький шаг для Web-разработчика и большой шаг для тебя!)',
#            1
#        ),
#        (
#            'А это уже следующая запись)',
#            'Вот тут начнутся сложности, но ты со всем справишься! Главное не останавливайся',
#            1
#        )
#        ]
#    cursor.executemany(
#        "insert into posts (title, content, user_id, date) values (%s, %s, %s, CURRENT_TIMESTAMP)",
#        posts
#    )
#    connection.commit()
#    print('Посты добавлены!')
    

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.execute(
        '''
            SELECT 
                posts.id,
                posts.title,
                posts.content,
                posts.user_id,
                users.name,
                users.surname,
                posts.date::date
            FROM 
                posts
            LEFT JOIN users
            ON posts.user_id = users.id
        ''')
       
        for post in cursor.fetchall():
            print(f"{post[0]} \n Автор: ID: {post[3]} {post[4]} {post[5]} \n - {post[1]} \n {post[2]} \n Дата: {post[6]}")
            print('\n -----------------------------------------------------')

        cursor.close()
        connection.close()
        print ('Connection closed')
