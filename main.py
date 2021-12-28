import plugins

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import DictProperty
import time
import plugins

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


# class LoadingWindow(Screen):
# 	sm = DictProperty(None, allownone=True)
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
# 		self.sm = App.get_running_app().root
# 		self.bind(on_sm=self.execute)

# 	def execute(self, *largs):
# 		self.sm.current = 'login'


class LoginWindow(Screen):
	def on_kv_post(self, *largs):
		Clock.schedule_once(self.anim_heading, 2)

	def anim_heading(self, _):
		heading = self.ids.heading

		tex0, tex1 = heading.texture_size
		anim = Animation( # animate fadein/opacity
			opacity=1.,
			duration=.7
		) + Animation( # wait
			opacity=1.,
			duration=.5
		) + Animation( # animate position
			pos_hint={"top": 0.9},
			duration=.6
		) + Animation( # wait
			opacity=1.,
			duration=.2
		) + Animation( # animate size
			texture_size=(tex0 / 1.3, tex1 / 1.3),
			duration=.3
		)

		anim.start(heading)

	def anim_login_form(self, _):
		pass

with open('telepat.kv', encoding='utf8') as fd:
	kv = Builder.load_string(fd.read())

class TelepatApp(App):
	def build(self):
		return kv


if __name__ == '__main__':
	TelepatApp().run()
