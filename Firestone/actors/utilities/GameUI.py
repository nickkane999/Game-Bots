from tkinter import *
import time


class GameUI:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.window = Tk()
        self.window.geometry("700x350")
        self.game_bot = bot
        self.run = False

    def startMenu(self):
        win = self.window
        # Create buttons to trigger the starting and ending of the loop
        start = Button(win, text="Start Game", command=self.start)
        start.pack(padx=10)
        stop = Button(win, text="Stop Game", command=self.stop)
        stop.pack(padx=15)

        # Call the print_hello() function after 1 sec.
        win.after(1000, self.game_loop)
        win.mainloop()

    def game_loop(self):
        win = self.window

        if self.run:
            Label(win, text="Running Game", font=('Helvetica 10 bold')).pack()
            self.game_bot.startQueue()
            print("Pausing for 20 seconds")
            time.sleep(20)
        if not self.run:
            Label(win, text="Not Running Game",
                  font=('Helvetica 10 bold')).pack()
        # After 1 sec call the print_hello() again
        win.after(1000, self.game_loop)

    def start(self):
        self.run = True

    def stop(self):
        self.run = False
