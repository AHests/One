from string import digits
from string import ascii_letters

file1 = []
# file = open(r"C:\Users\HP\Desktop\Уроки\ООП\easy_passwords.txt",encoding="utf-8")
# with open(r"C:\Users\HP\Desktop\Уроки\ООП\easy_passwords.txt", "r") as f:
#     file1 = f.readlines()


forbidden = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
             '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
             'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
             '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']


class Registration:
    def __init__(self, login, password):
        self.login = login  # self.login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, vale):
        if "@" not in vale or vale.count('@') > 1:
            raise ValueError("Логин должен содержать один символ '@'")
        elif "." not in vale[vale.index("@")::]:
            raise ValueError("Логин должен содержать символ '.'")

        else:
            self.__login = vale



    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for i in password:
            if i.isupper():
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for litter in password:
            if litter not in ascii_letters:
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        return password in forbidden

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")  # +
        if len(value) < 4 or len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')  # +
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')  # +
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')  # -
        if Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')  # -
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')  # +


        else:
            self.__password = value

r1 = Registration('qwerty@rambler.ru', 'QwrRt124')
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124


r1.password = '123456'  # ValueError
# r1.password = 'LoW'  # raise ValueError len
r1.password = 43  # raise TypeError