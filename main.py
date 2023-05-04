from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text = "моя первая кнопка", font_size=30, on_press=self.btn_press)
    
    def btn_press(self, instance):
        print('кнопка нажата')
        instance.text='я нажата'

if __name__ == "__main__":
    MyApp().run()