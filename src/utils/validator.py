class Validator:
    
    @staticmethod
    def validate_length(length):
        if 8<= length <=32:
            return length
        else:
            raise ValueError("Length must be between 8-32")
             
    @staticmethod
    def validate_yes_no(value):
        if value in ["y","n"]:
            return  value
        else:
            raise ValueError("Invalid input use only (y/n)")
