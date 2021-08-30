from templates.data.MenuDataTemplate import MenuDataTemplate


class HomeMenu(MenuDataTemplate):
    # Initializing Object
    def __init__(self):
        super(HomeMenu, self).__init__()
        self.options = self.getOptions()

    def getOptions(self):
        options = {
            "play": {"x": 830, "y": 930}
        }
        return options
