from src.models import PasswordConfig
from src.services import PasswordGenerator, StrengthChecker
from src.utils import InputHandler, logger, show_menu


class Application:

    def run(self):
        while True:
            try:
                show_menu()
                choice = InputHandler.get_menu_choice()
                if choice == "1":
                    # Generate Password Logic
                    password_length = InputHandler.get_password_length()
                    (is_uppercase, is_lowercase, includes_numbers, includes_special_character) = InputHandler.get_character_preferences()
                    config = PasswordConfig(password_length, is_uppercase, is_lowercase, includes_numbers, includes_special_character)
                    password = PasswordGenerator.generate(config)
                    print(f"Generated Password: {password}")
                elif choice == "2":
                    # Password Strengh Check Logic
                    password = InputHandler.get_password_input()
                    final_password = StrengthChecker.check_password(password)
                    logger.info(final_password)
                elif choice == "3":
                    print("Thank you for using the Password Generator!")
                    break
            except ValueError as ve:
                logger.error(f"{ve} Invalid value")
            except Exception as e:
                logger.error(f"{e}. Please try again")

if __name__ == "__main__":
    app = Application()
    app.run()
