from templates.data.MenuDataTemplate import MenuDataTemplate


class MapMenu(MenuDataTemplate):
    # Initializing Object
    def __init__(self):
        super(MapMenu, self).__init__()
        self.options = self.getOptions()

    def getOptions(self):
        options = {
            "beginner": {
                "monkey meadow": {"x": 550, "y": 260},
                "tree stump": {"x": 970, "y": 260},
                "town center": {"x": 1400, "y": 260},
                "resort": {"x": 550, "y": 570},
                "skates": {"x": 970, "y": 570},
                "lotus island": {"x": 1400, "y": 570},
            },
            "intermediate": {
                "baloonarius prime": {"x": 550, "y": 260},
                "balance": {"x": 970, "y": 260},
                "encrypted": {"x": 1400, "y": 260},
                "bazaar": {"x": 550, "y": 570},
                "adoras temple": {"x": 970, "y": 570},
                "spring spring": {"x": 1400, "y": 570},
            },
            "advanced": {
                "x factor": {"x": 550, "y": 260},
                "mesa": {"x": 970, "y": 260},
                "geared": {"x": 1400, "y": 260},
                "spillway": {"x": 550, "y": 570},
                "cargo": {"x": 970, "y": 570},
                "pats pond": {"x": 1400, "y": 570},
            },
            "expert": {
                "sanctuary": {"x": 550, "y": 260},
                "ravine": {"x": 970, "y": 260},
                "flooded valley": {"x": 1400, "y": 260},
                "infernal": {"x": 550, "y": 570},
                "bloody puddles": {"x": 970, "y": 570},
                "workshop": {"x": 1400, "y": 570},
            },
            "navigation": {
                "beginner": {"x": 580, "y": 980},
                "intermediate": {"x": 840, "y": 980},
                "advanced": {"x": 1090, "y": 980},
                "expert": {"x": 1340, "y": 980},
            },
            "next_arrow": {"x": 1650, "y": 430},
        }
        return options
