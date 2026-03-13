import secrets
import string

class TokenGenerator:
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    SYMBOLS = string.punctuation
    ALPHANUMERIC = string.ascii_letters + string.digits