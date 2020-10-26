# Kivy/KivyMD
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

KV = """
ScreenManager:
    LoginScreen:    
    MenuScreen:
    BovenScreen:
    BuitenScreen:
    BenedenScreen:

<LoginScreen>:
    name: 'Login'
    FloatLayout:
    
        MDToolbar:
            pos_hint: {'center_x':0.5, 'top':1}
            title: "KNX DEMO APP"
            
        Label:
            text: 'LOGIN'
            font_size: 40
            halign: 'center'
            pos_hint: {'center_x':0.5,'center_y':0.7}
        
        MDTextFieldRect:
            id: gebruikersnaam
            hint_text: 'Gebruikersnaam'
            pos_hint: {'center_x':0.5,'center_y':0.56}
            size_hint: 0.5, 0.05
            write_tab: False
            multiline: False
        
        MDTextFieldRect:
            id: wachtwoord
            hint_text: 'Wachtwoord'
            password: True
            pos_hint: {'center_x':0.5,'center_y':0.5}
            size_hint: 0.5, 0.05
            write_tab: False
            multiline: False
    
        MDRectangleFlatButton:
            text: 'Aanmelden'
            pos_hint: {'center_x':0.5,'center_y':0.43}
            size_hint: 0.3, 0.05
            on_release: root.verify_credentials()
    
<MenuScreen>:
    name: 'Menu'
    FloatLayout:
        MDToolbar:
            title: 'menu'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Lichten boven'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Boven'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten beneden'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Beneden'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten buiten'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Buiten'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                  
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<BovenScreen>:
    name: 'Boven'
    FloatLayout:
        MDToolbar:
            title: 'Boven'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Lichten boven'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Boven'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten beneden'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Beneden'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten buiten'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Buiten'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                  
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<BenedenScreen>:
    name: 'Beneden'
    FloatLayout:
        MDToolbar:
            title: 'Beneden'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Lichten boven'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Boven'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten beneden'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Beneden'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten buiten'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Buiten'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                  
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<BuitenScreen>:
    name: 'Buiten'
    FloatLayout:
        MDToolbar:
            title: 'Buiten'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Lichten boven'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Boven'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten beneden'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Beneden'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                
                        OneLineIconListItem:
                            text: 'Lichten buiten'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Buiten'
                            IconLeftWidget:
                                icon: 'lightbulb'
                                  
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'
"""


class Example(MDApp):
    def build(self):
        # thema instellen
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        # de string 'KV' laden
        return Builder.load_string(KV)


class LoginScreen(Screen):
    def verify_credentials(self):
        # controleren op gebruikersnaam en wachtwoord.
        if self.ids["gebruikersnaam"].text == "admin" and self.ids["wachtwoord"].text == "admin":
            self.manager.current = "Menu"  # naar menu-scherm
        # Wachtwoord en gebruikernaams veld leeg maken als wachtwoord fout is.
        self.ids["gebruikersnaam"].text = ""
        self.ids["wachtwoord"].text = ""


class MenuScreen(Screen):
    pass


class BovenScreen(Screen):
    pass


class BenedenScreen(Screen):
    pass


class BuitenScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(BovenScreen(name='Boven'))
sm.add_widget(BenedenScreen(name='Beneden'))
sm.add_widget(BuitenScreen(name='Buiten'))

Example().run()
