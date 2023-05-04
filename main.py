from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
import sqlite3

res=''

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
                      on_press=self.btn_press,
                      background_color=[1,0,0,1],
                      background_normal='',
                      size_hint = (.5, .25),
                      pos = (640 / 2 - 160, 480 / 2 - (480 / 2 / 2))
                     )
    
    def btn_press(self, instance):
        print('кнопка нажата')
        instance.text = str(self.db_res)


    def db_res(self):
        con = sqlite3.connect('test.db')
        curObj = con.cursor()
        curObj.execute("SELECT name FROM manga WHERE id = '2'")
        rows = curObj.fetchall()
        print(rows)
        return rows[1][1]


if __name__ == "__main__":
    MyApp().run()