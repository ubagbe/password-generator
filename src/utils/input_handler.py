from src.utils import Validator, logger


class InputHandler:
    
    @classmethod
    def get_menu_choice(cls):
        while True:
            choice = input("Please Enter You Choice : ")  
            try:
                if choice in ["1","2","3"]:
                    return choice
                raise ValueError("Please enter 1 or 2 or 3")
            except  ValueError as ve:
                logger.error(f"{ve}. Please try again")
            except Exception as e:
                logger.error(f"{e}. Please try again")    
                

    @staticmethod
    def get_password_length():
        while True:
            try:
                length = input("Enter the password length (8 - 32): ")
                return Validator.validate_length(int(length))
            except ValueError as ve:
                logger.error(f"{ve}. Please try again")
            except Exception as e:
                logger.error(f"{e}. Please try again")

    @staticmethod
    def get_character_preferences():
        while True:
            try:
                is_uppercase = Validator.validate_yes_no(input("Includes Uppercase? (y/n): "))
                is_lowercase = Validator.validate_yes_no(input("Includes Lowercase? (y/n): "))
                includes_numbers = Validator.validate_yes_no(input("Includes Numbers? (y/n): "))
                includes_special_character = Validator.validate_yes_no(input("Includes Special Characers? (y/n): "))
    
                return (is_uppercase, is_lowercase, includes_numbers, includes_special_character)
            except ValueError as ve:
                logger.error(f"{ve}. Please try again")
            except Exception as e:
                logger.error(f"{e}. Please try again")

    @staticmethod
    def get_password_input():
        password = input("Please enter yor password: ")
        return password
