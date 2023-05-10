from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
import sqlite3

res=''
i=0

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        
        
        #q=1
        #print(' '.join(map(rows, q)))
        return Button(text = "моя первая кнопка",
                      font_size=30,
                      on_press=self.db_res,
                      background_color=[1,0,0,1],
                      background_normal='',
                      size_hint = (.5, .25),
                      pos = (640 / 2 - 160, 480 / 2 - (480 / 2 / 2))
                     )
    
    def btn_press(self, instance):
        
        print('кнопка нажата')
        instance.text=self.db_res(15)


    def db_res(self, instance, records):
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
            instance.text=row[1]
        
        cursor.close()
        
        return row[1]


        
        '''except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
            
            
            
            
            
            
        con = sqlite3.connect('test.db')
        curObj = con.cursor()
        curObj.execute("SELECT name FROM manga WHERE id = '2'")
        rows = curObj.fetchall()
        print(rows)
    
        for i in rows:
            print(rows[1])
'''
class Library():
	def __init__(self):
		self.libra = []
	
	def addBook(self, book):
		self.libra.append(book)
		
	def getBooksByAuth(self, auth):
		arr = []
		for b in self.libra:
			if b.autor == auth:
				arr.append(b.name)
			
		if arr == []:
			return "Íåò òàêîãî àâòîðà"
			
		return arr
		
	def getBooksByTitle(self, title):
		i = 0
		for b in self.libra:
			if b.name == title:
				return b
	
	def showBookList(self):
		for b in self.libra:
			print(b.name, b.autor, b.year, b.vid, b.age)


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

if __name__ == "__main__":
    MyApp().run()