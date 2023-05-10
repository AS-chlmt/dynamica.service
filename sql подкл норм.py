import sqlite3

def read_sqlite_table(records):
    try:
        sqlite_connection = sqlite3.connect('test.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        cursor.execute("SELECT * FROM users")
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("Имя:", row[1])
            print("Почта:", row[2])

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

read_sqlite_table(15)