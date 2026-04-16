import random
import string


class PasswordGenerator:

    @classmethod
    def generate(cls, config):
        character_pool = cls.create_character_pool(config)
        return cls.build_password(character_pool, config.password_length)  

    @classmethod
    def create_character_pool(cls, config):
        character_pool = ""

        if config.is_uppercase =="y":
            character_pool += string.ascii_uppercase
        if config.is_lowercase =="y":
            character_pool += string.ascii_lowercase
        if config.includes_numbers =="y":
            character_pool += string.digits
        if config.includes_special_character  =="y":
            character_pool += string.punctuation
        if character_pool == "":
            raise ValueError("At least one character type must be selected.")
        return character_pool
    
    @classmethod
    def build_password(cls, character_pool, length):
        password = ''.join(random.choices(character_pool, k=length))
        return password
