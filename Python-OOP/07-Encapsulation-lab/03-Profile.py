class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not len(value) in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.password_size(value) and self.upper_case(value) and self.digits(value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def password_size(self, password):
        if len(password) >= 8:
            return True
        return False

    def upper_case(self, password: str):
        uppers = [char for char in password if char.isupper()]
        return True if uppers else False

    def digits(self, password: str):
        numbers = [char for char in password if char.isdigit()]
        return True if numbers else False

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)



