from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Grocery Store"
            left_action_items: [["menu", lambda x: app]] 
            
        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            padding: 20
            
            MDLabel:
                text: 'Grocery Shop'
                halign: 'center'
                theme_text_color: 'Secondary'
                font_style: 'H4'
    
            MDRaisedButton:
                text: 'New User Registration'
                pos_hint: {'center_x': 0.5}
                on_release: app.show_registration()
    
            MDRaisedButton:
                text: 'Login'
                pos_hint: {'center_x': 0.5}
                on_release: app.show_login()
'''


class GroceryShopApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style = 'Light'
        return Builder.load_string(KV)

    def show_registration(self):
        print("New User Registration")

    def show_login(self):
        print("Login")


if __name__ == '__main__':
    GroceryShopApp().run()
