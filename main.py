from src.utils import InputHandler

class Application:
    def __init__(self):
        pass

    def run(self):
        InputHandler.get_menu_choice()   


if __name__ == "__main__":
    app = Application()
    app.run()
