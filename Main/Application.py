from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class BackgroundImage(FloatLayout):
    def __init__(self, **kwargs):
        super(BackgroundImage, self).__init__(**kwargs)

        self.bg_image = Image(
            source="DarkBack1.jpg",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.add_widget(self.bg_image)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        self.layout = BackgroundImage()

        self.image = Image(
            source="groceries.png",
            size_hint=(0.6, 0.3),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        self.layout.add_widget(self.image)

        self.greeting = Label(
            text="What's your name?",
            font_size='20sp',
            color=(0, 0.86, 0.51, 1),
            size_hint=(None, None),
            size=(self.image.size[0], self.image.size[1] * 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.layout.add_widget(self.greeting)

        self.user = TextInput(
            multiline=False,
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        self.layout.add_widget(self.user)

        self.button = Button(
            text="GREET",
            size_hint=(0.4, 0.1),
            bold=True,
            background_color=(0, 0.86, 0.51, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        self.button.bind(on_press=self.callback)
        self.layout.add_widget(self.button)

        self.add_widget(self.layout)

    def callback(self, instance):
        self.greeting.text = "Welcome to my app, " + self.user.text + "!"
        self.user.text = ""

        Clock.schedule_once(self.switch_to_main, 1)

    def switch_to_main(self, dt):
        self.manager.current = "main_screen"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.layout = BackgroundImage()

        self.image = Image(
            source="groceries.png",
            size_hint=(0.6, 0.3),
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )
        self.layout.add_widget(self.image)

        self.greeting = Label(
            text="What action do you want to do?",
            font_size='20sp',
            color=(0, 0.86, 0.51, 1),
            size_hint=(None, None),
            size=(self.image.size[0], self.image.size[1] * 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.layout.add_widget(self.greeting)

        button_names = [
            "Adjust Shopping List",
            "Make Shopping List",
            "View Shopping List",
            "Settings"
        ]
        button_positions = [
            (0.3, 0.1),  # Adjust Shopping List
            (0.7, 0.1),  # Make Shopping List
            (0.3, 0.2),  # View Shopping List
            (0.7, 0.2)   # Settings
        ]

        for name, (x, y) in zip(button_names, button_positions):
            btn = Button(
                text=name,
                size_hint=(0.4, 0.1),
                pos_hint={"center_x": x, "center_y": y},
                background_color=(0, 0.86, 0.51, 1),
                bold=True
            )
            self.layout.add_widget(btn)

        self.add_widget(self.layout)

class ShoppingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome_screen"))
        sm.add_widget(MainScreen(name="main_screen"))
        return sm

if __name__ == "__main__":
    ShoppingApp().run()
