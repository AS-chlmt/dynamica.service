from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):

        fl = FloatLayout(size=(300,300))
        fl.add_widget(Button(text = "моя первая кнопка",
                      font_size=30,
                      on_press=self.btn_press,
                      background_color=[1,0,0,1],
                      background_normal='',
                      size_hint = (.5, .25),
                      pos = (640 / 2 - 160, 480 / 2 - (480 / 2 / 2))
                     ))
        
        return fl
    
    def btn_press(self, instance):
        print('кнопка нажата')
        instance.text='я нажата и все тут'

if __name__ == "__main__":
    MyApp().run()