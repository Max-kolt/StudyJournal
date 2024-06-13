import secrets
import string


def password_generator(lenght: int = 8, with_symbols: bool = False):
    symbols = string.ascii_letters+string.digits
    if with_symbols:
        symbols += "@$*"
    return "".join([secrets.choice(symbols) for i in range(lenght)])  # Random symbols choices
