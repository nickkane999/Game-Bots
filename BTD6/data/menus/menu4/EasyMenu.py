from templates.data.MenuDataTemplate import MenuDataTemplate


class EasyMenu(MenuDataTemplate):
    # Initializing Object
    def __init__(self):
        super(EasyMenu, self).__init__()
        self.options = self.getOptions()

    def getOptions(self):
        options = {
            "standard": {"x": 640, "y": 600},
            "primary only": {"x": 960, "y": 450},
            "deflation": {"x": 1290, "y": 450},
            "sandbox": {"x": 970, "y": 740},
            "overrite_save": {"x": 1140, "y": 720},
        }
        return options
