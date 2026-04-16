import string


class StrengthChecker:

    @classmethod
    def check_password(cls, password):
        length = len(password)
        digit = any(char in string.digits for char in password)
        lowercase = any(char in string.ascii_lowercase for char in password)
        uppercase = any(char in string.ascii_uppercase for char in password)
        special = any(char in string.punctuation for char in password)

        if  (length > 12) and  special and digit and uppercase and lowercase:
            return "Strong Password"
        elif (10 <= length <= 12) and (digit or special) and uppercase and lowercase:
            return "Medium Password"
        elif (8 <= length <= 10) and uppercase and lowercase:
            return "Weak Password"
        else:
            return "Very Weak Password"
