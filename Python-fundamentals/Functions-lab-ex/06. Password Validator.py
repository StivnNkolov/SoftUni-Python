def password_validator(password):
    is_valid = True
    chars_c = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for ch in password:
        if ch.isdigit():
            chars_c += 1
    if chars_c < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


input_password = input()
password_validator(input_password)