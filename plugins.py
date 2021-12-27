import json

dirs = {
    "config": "assets/data/config.json",
    "settings": "assets/data/settings.json"
}


def load_files():
    try:
        with open(dirs["config"], "r") as f:
            global config

            config = json.load(f)

            f.close()

        with open(dirs["settings"], "r") as f:
            global settings
            settings = json.load(f)

            f.close()

        with open(f"assets/themes/{settings['theme']}.json") as f:
            global theme
            theme = json.load(f)

            f.close()

        return True

    except Exception:
        raise


def reload_file(file):
    try:
        if file == "config":
            with open(dirs["config"]) as f:
                config = json.load(f)  # noqa

                f.close()

                return True
        elif file == "settings":
            with open(dirs["settings"], "r") as f:
                settings = json.load(f)

                f.close()

                return True
        elif file == "theme":
            with open(f"assets/themes/{settings['theme']}.json", "r") as f:
                theme = json.load(f)  # noqa

                f.close()

                return True
        else:
            raise
    except Exception:
        return False
