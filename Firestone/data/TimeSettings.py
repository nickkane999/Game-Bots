class TimeSettings:
    # Initializing Object
    def __init__(self, actors):
        self.data = self.setTimeSettings(actors)

    # Major object functions
    def setTimeSettings(self, actors):
        time_settings = {
            # Actions listed first in dictionary get higher priority
            "actions": {
                "startup": {
                    "rotation_time": 0,
                    "times_performed": 0,
                    "start_function": actors["startup"].runStartup,
                    "action_settings": {
                        "run_once": True,
                        "has_ran": False,
                    }
                },
                "guild": {
                    "rotation_time": 600,
                    "times_performed": 0,
                    "start_function": actors["guild"].startGuildDuties,
                    "action_settings": {
                        "sample": 123
                    }
                },
                "library": {
                    "rotation_time": 1200,
                    "times_performed": 0,
                    "start_function": actors["library"].startLibraryDuties,
                    "action_settings": {
                        "sample": 123
                    }
                },
                "campaign": {
                    "rotation_time": 1200,
                    "times_performed": 0,
                    "start_function": actors["campaign"].startCampaignDuties,
                    "action_settings": {
                        "sample": 123
                    }
                },
                "temple": {
                    "rotation_time": 600,
                    "times_performed": 0,
                    "start_function": actors["temple"].startTempleDuties,
                    "action_settings": {
                        "reset_time_requirement": 3600,
                        "reset_firestone_level": 100,
                        "time_firestone_level_reached": 0
                    }
                },
                "server_swap": {
                    "rotation_time": 300,
                    "times_performed": 0,
                    "start_function": actors["server_swap"].determineServerSwap,
                    "action_settings": {
                        "tbd": 3,
                    }
                },
                "battle": {
                    "rotation_time": 0,
                    "times_performed": 0,
                    "start_function": actors["battle"].startBattleDuties,
                    "action_settings": {
                        "active_party": True,
                        "captain_slot": 6,
                        "priority_buying": True,
                        "idle_attack_button": 3,
                    }
                },
            }
        }

        return time_settings
