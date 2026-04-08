class InputHandler:

    @staticmethod
    def show_menu():
        print("-------------------------")
        print("PASSWORD GENERATOR SYSTEM")
        print("-------------------------")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

    @classmethod
    def get_menu_choice(cls):
        while True:
            cls.show_menu()
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
        length = input("Enter the password length (8 - 32): ")
        return length

    @staticmethod
    def get_character_preferences():
        is_uppercase = input("Includes Uppercase? (y/n): ")
        is_lowercase = input("Includes Lowercase? (y/n): ")
        includes_numbers = input("Includes Numbers? (y/n): ")
        includes_special_character = input("Includes Special Characers? (y/n): ")

        return (is_uppercase, is_lowercase, includes_numbers, includes_special_character)

    @staticmethod
    def get_password_input():
        password = input("Please enter yor password: ")
        return password

if __name__ == "__main__":
    InputHandler.get_menu_choice()
