from src.utils import show_menu, Validator, logger


class InputHandler:
    
    @classmethod
    def get_menu_choice(cls):
        while True:
            show_menu()
            choice = input("Please Enter You Choice : ")
            # Generate Password Logic
            if choice == "1":
                password_length = cls.get_password_length()
                (is_uppercase, is_lowercase, includes_numbers, includes_special_character) = cls.get_character_preferences()
            # Password Strengh Check Logic
            elif choice == "2":
                password = cls.get_password_input()
            elif choice == "3":
                print("Thank you for using the Password Generator!")
                break
            else:
                print("Invalid menu choice. Please select the listed options.") 
        return choice

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
