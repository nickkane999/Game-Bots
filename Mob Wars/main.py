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


risk_model = {
    'rounds': 10,
    'mob_count': 55
}
risk_model2 = {
    'rounds': 10,
    'mob_count': 54
}
application.bot.runFightsLoop(risk_model2)


application.bot.runFights(risk_model2)



application.bot.switchToIFrame()
application.bot.pullMobs()
scripts = "INSERT DATA HERE"
application.bot.addMobs(scripts)

//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[2]
//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[2]

//*[@id="battle_response_wrapper"]/div[1]/div[4]/div/table/tbody/tr[2]/td[4]/a

//*[@id="header_profile_pic"]/div/a
//*[@class="header-profile"]/div/a

//*[@class="ri-contents-tab-wrapper"]/div[1]


//*[@id="ri-item-0"]/div/div[2]/a