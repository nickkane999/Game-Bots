from templates.data.MenuDataTemplate import MenuDataTemplate


class DifficultyMenu(MenuDataTemplate):
    # Initializing Object
    def __init__(self):
        super(DifficultyMenu, self).__init__()
        self.options = self.getOptions()

    def getOptions(self):
        options = {
            "easy": {"x": 630, "y": 420},
            "medium": {"x": 970, "y": 420},
            "hard": {"x": 1300, "y": 420}
        }
        return options
