# from data.models.actions.FunctionActions import FunctionActions
# from data.models.instructions.ProgramInstructions import ProgramInstructions
from Application import Application;

instructions = {
    'data_file': r'C:\Users\nickk\Music\Portfolio\Game-Bots\Mob Wars\data\database.json',
    'url': r'https://armorgames.com/mob-wars-la-cosa-nostra-game/14870',
    'username': 'nickkane999',
    'password': 'Orange1226Monkey',
}
application = Application(instructions)
application.browser.start()



application.bot.switchToIFrame()
application.bot.battleRoyal.healSelfLoop(500)
# application.bot.battleRoyal.healSelfLoop(30)


application.bot.switchToIFrame()
application.bot.battleRoyal.reset()
application.bot.battleRoyal.attackEnemiesLoop(600)


application.bot.switchToIFrame()
risk_model = {
    'rounds': 50,
    'mob_count': 500
}
application.bot.runFightsLoop(risk_model)


# application.bot.runFights(risk_model2)

//*[@id="edb901b5-3dc3-4338-91c5-15ae5591acb9_row"]/div[2]/a

//*[@id=\"br_fl_targets\"]/[@class=\"br-fight-list-target\"]
//*[@id="br_fl_targets"]/[@class="br-fight-list-target"]
//*[@id=\"br_fl_targets\"]/[div[NNN]
//*[@id="br_pb_medkit_use"]

//*[@id="d4c6f65d-9800-4197-a452-0ab444dbabfd_row"]/div[2]/div/div

application.bot.switchToIFrame()
application.bot.pullMobs()
application.bot.addMobs(scripts)
application.bot.addMobs()



application.bot.addMobsRecommended()




//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[2]
//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[2]

//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[4]/a

//*[@id="header_profile_pic"]/div/a
//*[@class="header-profile"]/div/a

//*[@class="ri-contents-tab-wrapper"]/div[1]


//*[@id="ri-item-0"]/div/div[2]/a