class PasswordConfig:
    def __init__(
            self,
            password_length: int,
            is_uppercase: str,
            is_lowercase: str,
            includes_numbers: str,
            includes_special_character: str
        ):
        self.password_length = password_length
        self.is_uppercase = is_uppercase
        self.is_lowercase = is_lowercase
        self.includes_numbers = includes_numbers
        self.includes_special_character = includes_special_character
