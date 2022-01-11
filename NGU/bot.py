# from data.models.actions.FunctionActions import FunctionActions
# from data.models.instructions.ProgramInstructions import ProgramInstructions
from Application import Application;
instructions = {
    'data_file': r'C:\Users\nickk\Music\Portfolio\Game-Bots\NGU\data\database.json'
}
application = Application(instructions)
application.bot.rebirth_manager.idleCycleRotation()
application.bot.rebirth_manager.idleCycle("cycle_six")


application.bot.gear_manager.applyCubeBoostLoop()
application.bot.cycle_manager.capNGULoop()


application.bot.rebirth_manager.changeGearSlot("drop_rate_build")
application.bot.rebirth_manager.assignAugments("energy_buster")
application.bot.rebirth_manager.assignAugments("energy_buster", True)
application.bot.rebirth_manager.idleCycle()
application.bot.rebirth_manager.idleCycleRotation()


time.sleep(2)
application.bot.rebirth_manager.timeMachineSet([1000, "add", 1000, "add"])

time.sleep(2)
application.bot.rebirth_manager.augmentsSet(["energy_buster", 2400000000, "add", 900000000, "add"])


application.bot.rebirth_manager.assignAugments("energy_buster")

application.bot.cycle_manager.idleCycle(1255)
resource_build
application.bot.cycle_manager.idleCycle(1)

application.bot.battle_manager.adventureCycle()
application.bot.battle_manager.quickKillCycle()
application.bot.battle_manager.quickKillCycle(2)


application.bot.battle_manager.getState("parry")
application.bot.battle_manager.getState("pierce")
application.bot.battle_manager.getState("ultimate_attack")

application.bot.battle_manager.getState("block")
application.bot.battle_manager.getState("defense_buff")

application.bot.battle_manager.getState("paralyze")
application.bot.battle_manager.getState("regen")


application.bot.gear_manager.applyCubeBoostLoop()
application.bot.gear_manager.get_pixel_colour(1600, 720)
application.bot.cycle_manager.timeMachineCycle()

application.bot.cycle_manager.yggdrasilHarvest()
application.bot.cycle_manager.wandosCycle()
application.bot.cycle_manager.capNGULoop()



application.bot.gear_manager.upgradeItems(True)

application.bot.startCycle()

application.bot.setAugmentation(True)
application.bot.setTimeMachine()
application.bot.setBasicTraining()
application.bot.fightBosses()


application.bot.gear_manager.upgradeItems(True)


application.bot.setAugmentation(True)

application.bot.gear_manager.clearInventory()

application.bot.gear_manager.upgradeItems()


application.bot.gear_manager.upgradeGearPriority()d
application.bot.gear_manager.upgradeInventoryPriority()
get_pixel_colour

application.bot.gear_manager.clearInventory()
application.bot.gear_manager.upgradeGear("accessory_1")


application.bot.gear_manager.upgradeGear("head")
application.bot.gear_manager.upgradeGear("pants")
application.bot.gear_manager.upgradeGear("accessory_2")






import pyautogui
import time

def startProgram():add_member_posta
    gear_pos = (1025, 200)
    inv_pos = (1515, 675)
    inv_start_pos = (765, 600)
    counter = 0

    positions = {
        (-75, 0),
        (-75, 75),
        (-75, 150),
        (0, 75),
        (75, 75),
        (0, 150),
        (0, 225)
    }

    inv_positions = {
        (-150, 150),
        (-75, 150),
        (0, 150),
        (75, 150),
        (-75, 0),
        (-75, -75),
        (-75, 75),
        (0, 0),
        (0, 75),
        (0, -75),
        (75, 0),
        (75, 75),
        (75, -75),        
        (-150, 0),
        (-150, -75),
        (-150, 75),
        (-225, 0),
        (-225, -75),
        (-225, 75),
        (-300, 0),
        (-300, -75),
        (-300, 75),
    }

    inv_start_positions = {
        (0, 0),
        (75, 0),
        (150, 0),
        (225, 0),
        (300, 0),
        (375, 0),
        (0, 75),
        (75, 75),
        (150, 75),
        (225, 75),
        (300, 75),
        (375, 75),
        (0, 150),
        (75, 150),
        (150, 150),
        (225, 150),
        (300, 150),
        (375, 150),
    }
    
    while True:
        counter = counter + 1
        modifyGear('a', gear_pos, positions, True)
        modifyGear('a', inv_pos, inv_positions)
        modifyGear('d', gear_pos, positions)
        modifyGear('d', inv_pos, inv_positions)
        if counter % 1000 == 0:
            modifyGear('ctrl', inv_start_pos, inv_start_positions)
        print("I upgraded gear. Sleeping")
        time.sleep(10)

def modifyGear(key, start_pos, points, multiple_clicks = False):
    start_x = start_pos[0]
    start_y = start_pos[1]
    pyautogui.moveTo(start_x, start_y)
    pyautogui.keyDown(key)
    time.sleep(0.5)
    if multiple_clicks:
        for x in range(0, 5):
            for point in points:
                pyautogui.click(start_x + point[0], start_y + point[1])
                time.sleep(0.3)
    else:
        for point in points:
            pyautogui.click(start_x + point[0], start_y + point[1])
            time.sleep(0.3)
    time.sleep(1)
    pyautogui.keyUp(key)


# unsure on resolution

time.sleep(5)
print("Starting program")
startProgram()
