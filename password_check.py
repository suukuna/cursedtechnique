SPECIAL_SYMBOLS = '+-/*!"№;%:?*()='


def password_verification(password: str) -> bool:
    if not password.isascii():
        return False
    contain_upper = False
    contain_lower = False
    contain_digit = False
    contain_special_symbol = False
    if len(password) < 8:
        return False
    if ' ' in password:
        return False
    for symbol in password:
        if symbol.isdigit():
            contain_digit = True
        if symbol.islower():
            contain_lower = True
        if symbol.isupper():
            contain_upper = True
        if symbol in SPECIAL_SYMBOLS:
            contain_special_symbol = True
    return all([contain_lower, contain_upper, contain_digit, contain_special_symbol])


print(password_verification('йBb+jkwcnwї88'))
