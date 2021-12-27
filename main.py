from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock
import plugins
import time


plugins.load_files()
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


class WindowManager(ScreenManager):
	pass

class LoadingWindow(Screen):
	pass

class LoginWindow(Screen):
	def anim_heading(self):
		Clock.schedule_once(function, 2)
		root = App.get_running_app().root.ids
		anim = Animation(size=(root.header.size[0]-20, root.header.size[1]-20), duration=.2)
		# self.ids.header.text = "test"
		# anim = Animation(size=(self.ids.header.size[0]-20, self.ids.header.size[1]-20), duration=.2)
		anim.start(root.header)
		


with open('telepat.kv', encoding='utf8') as fd:
	kv = Builder.load_string(fd.read())

class TelepatMessengerApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	TelepatMessengerApp().run()