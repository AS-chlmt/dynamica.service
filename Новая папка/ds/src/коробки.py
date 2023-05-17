from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        bl = BoxLayout(padding=[200,250])

        bl.add_widget(Button(text='Записаться в сервис'))
        bl.add_widget(Button(text='Просмотреть автомобили'))

        return bl

if __name__ == "__main__":
    BoxApp().run()