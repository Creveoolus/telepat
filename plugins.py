import json

dirs = {
	"config": "assets/data/config.json",
	"settings": "assets/data/settings.json"
}


def load_files():
	try:
		with open(dirs["config"], "r", encoding='utf8') as f:
			global config

			config = json.load(f)

			f.close()

		with open(dirs["settings"], "r", encoding='utf8') as f:
			global settings
			settings = json.load(f)

			f.close()

		with open(f"assets/themes/{settings['theme']}.json", "r", encoding='utf8') as f:
			global theme
			theme = json.load(f)

			f.close()

		with open(f"assets/lang/{settings['lang']}.json", "r", encoding='utf8') as f:
			global lang
			lang = json.load(f)

			f.close()

		return True

	except Exception:
		raise


def reload_file(file):
	try:
		if file == "config":
			with open(dirs["config"], "r", encoding='utf8') as f:
				config = json.load(f)  # noqa

				f.close()

				return True
		elif file == "settings":
			with open(dirs["settings"], "r", encoding='utf8') as f:
				settings = json.load(f)

				f.close()

				return True
		elif file == "theme":
			with open(f"assets/themes/{settings['theme']}.json", "r", encoding='utf8') as f:
				theme = json.load(f)  # noqa

				f.close()

				return True
		elif file == "lang":
			with open(f"assets/lang/{settings['lang']}.json", "r", encoding='utf8') as f:
				global lang
				lang = json.load(f)

				f.close()
		else:
			raise
	except Exception:
		return False
