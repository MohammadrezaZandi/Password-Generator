import random as rnd
import string

class PasswordGenerator:
    def __init__(self,PasswordSize,):
        self.PasswordSize = PasswordSize
        self.password = ''
        self.includeNumber = True
        self.special_item = True
        self.characters = ''
    def generate(self):
        lower_char = string.ascii_lowercase
        uppercase_char = string.ascii_uppercase
        self.characters = lower_char + uppercase_char
        if self.includeNumber:
            self.characters += string.digits
        if self.special_item:
            self.characters += string.punctuation
        self.password = ''.join(rnd.choice(self.characters) for _ in range(PasswordSize))
        self.PasswordValidation()
    def PasswordValidation(self):
        if not any(c in string.punctuation for c in self.password):
            print("Password must contain at least one special character")
        else:
            print(f'Password: {self.password}')
            print("Password is valid")



if __name__ == "__main__":
    while True:
        try:
            PasswordSize = int(input('Please Enter the length of your Password(Between 8 to 16): '))
            if PasswordSize >= 8 and PasswordSize <= 16:
                obj = PasswordGenerator(PasswordSize)
                obj.generate()
            else:
                print('Invalid input, please try to enter correct ')
        except ValueError:
            print('Please enter a number.')