from templates.data.MenuDataTemplate import MenuDataTemplate


class GameMapMenu(MenuDataTemplate):
    # Initializing Object
    def __init__(self):
        super(GameMapMenu, self).__init__()
        self.options = self.getOptions()

    def getOptions(self):
        options = {
            "victory_next": {"x": 960, "y": 910},
            "victory_home": {"x": 800, "y": 850},
            "next_wave": {"x": 1830, "y": 1000},
            "deflation_ok": {"x": 960, "y": 760},
            "level_accept": {"x": 940, "y": 540},
            "upgrade_slots": {
                "left": {
                    "slot_1": {"x": 340, "y": 490},
                    "slot_2": {"x": 340, "y": 640},
                    "slot_3": {"x": 340, "y": 790},
                },
                "right": {
                    "slot_1": {"x": 1560, "y": 490},
                    "slot_2": {"x": 1560, "y": 640},
                    "slot_3": {"x": 1560, "y": 790},
                },
            },
            "free_gift_2_open_left": {"x": 800, "y": 540},
            "free_gift_2_open_right": {"x": 1100, "y": 540},
        }
        return options
