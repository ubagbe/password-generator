from src.utils import InputHandler, show_menu, logger
from src.models import PasswordConfig
from src.services import PasswordGenerator, StrengthChecker

class Application:

    def run(self):
        while True:
            show_menu()
            choice = InputHandler.get_menu_choice()
            if choice == "1":
                try:
                    # Generate Password Logic
                    password_length = InputHandler.get_password_length()
                    (is_uppercase, is_lowercase, includes_numbers, includes_special_character) = InputHandler.get_character_preferences()
                    config = PasswordConfig(password_length, is_uppercase, is_lowercase, includes_numbers, includes_special_character)
                    password = PasswordGenerator.generate(config)
                    print(f"Generated Password: {password}")
                except ValueError as ve:
                    logger.error(f"{ve} Invalid value")
            elif choice == "2":
                # Password Strengh Check Logic
                password = InputHandler.get_password_input()
                final_password = StrengthChecker.check_password(password)
                logger.info(final_password)
            elif choice == "3":
                print("Thank you for using the Password Generator!")
                break
            else:
                print("Invalid menu choice. Please select the listed options.")

if __name__ == "__main__":
    app = Application()
    app.run()
