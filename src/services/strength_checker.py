import string


class StrengthChecker:

    @classmethod
    def checkpassword(cls, password):
        length = len(password)
        digit = any(_ in string.digits for _ in password)
        lowercase = any(_ in string.ascii_lowercase for _ in password)
        uppercase = any(_ in string.ascii_uppercase for _ in password)
        special = any(_ in string.punctuation for _ in password)
        
        if  (length > 12) and  special and digit and uppercase and lowercase:
            return("Strong Password")
        elif (10 <= length <= 12) and (digit or special) and uppercase and lowercase:
            return("Medium Password")
        elif (8 <= length <= 10) and uppercase and lowercase:
            return("Week Password")
        else:
            return("Very Week Password")            
       