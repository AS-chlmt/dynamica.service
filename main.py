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


    def db_res(self, records):
        try:
            sqlite_connection = sqlite3.connect('test.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            cursor.execute("INSERT INTO users (id, login, password) VALUES (3, 'dog', 2222)") '''уникальный id, будет ругаться'''
            sqlite_connection.commit()
            cursor.execute("SELECT * FROM USERS")
            records = cursor.fetchall()
            print("Всего строк:  ", len(records))
            print("Вывод каждой строки")
            


        
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
            
            
            
            
            
        
if __name__ == "__main__":
    MyApp().run()