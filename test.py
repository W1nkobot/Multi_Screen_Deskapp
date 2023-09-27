from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.app import MDApp

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:
            OneLineIconListItem:            
                IconLeftWidget:
                    icon: "/home/student/Desktop/Wank/Stock images/shopicon.jpg" 
            OneLineListItem:
                text: "Log In"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


Screen:

    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 5
        title: 'Best Shop In The "HelloWorld"'
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Тут лента классных новостей"
                    halign: "center"            
            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Логинься! Надо!"
                    halign: "center"

            Screen:
                name: "scr 3"

                MDLabel:
                    text: "Тут твои штуки для покупки"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

Config.set('kivy', 'window_icon', '/home/student/Desktop/Wank/Stock images/shopicon.jpg')

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class GroceryStore(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_string(KV)


GroceryStore().run()