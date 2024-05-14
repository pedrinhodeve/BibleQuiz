# from biblequiz.rootgame.constructor_root_game import RootGame
# from tkinter import Tk
from biblequiz.rootlogin.constructor_root_login import ConstructorRootLogin

class App():
    def __init__(self):
        # super().__init__()
        ConstructorRootLogin().mainloop()

if __name__ == "__main__":
    app = App()
    # app.mainloop()

