import plugins

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
# from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

plugins.load_files()
'''
# Set Config
Config.set('kivy', 'pause_on_minimize', 1)
Config.set('kivy', 'log_dir', 'logs')
Config.set('kivy', 'log_enable', 0)
Config.set('kivy', 'log_level', 'debug')
Config.set('kivy', 'window_icon', 'imgs/icon.ico')
Config.set('graphics', 'minimum_height', 490)
Config.set('graphics', 'minimum_width', 829)
Config.set('graphics', 'height', 490)
Config.set('graphics', 'width', 829)
Config.set('graphics', 'resizable', 1)
Config.write()
'''
Builder.load_file('telepat.kv')


class WindowManager(ScreenManager):
    pass


class LoadingWindow(Screen):
    pass


class LoginWindow(Screen):
    def on_kv_post(self, *largs):
        Clock.schedule_once(self.anim_heading, 2)

    def anim_heading(self, dt):
        heading = self.ids.heading
        tex0, tex1 = heading.texture_size

        anim = Animation(
            texture_size=(tex0 - 20, tex1 - 20),
            duration=2.
        )
        # self.ids.heading.text = "test"

        anim.start(heading)


class TelepatMessengerApp(App):
    def build(self):
        self.root = WindowManager()

        return self.root


if __name__ == '__main__':
    TelepatMessengerApp().run()
