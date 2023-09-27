import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.monitor = Label(text='')
        self.monitor.bind()
        self.add_widget(self.monitor)

        self.submit = Button(text="Generate!", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        chars = '+-/*!&$#?=@<>%^:;()abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = 1
        length = 5
        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chars)
        print("YourPassword:", password)
        self.monitor.text = password




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()