import random
import string


def get_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join([random.choice(letters) for i in range(length)])


def get_random_phone():
    digits = string.digits
    return "".join([random.choice(digits) for i in range(10)])


def get_random_email():
    return (
        get_random_string()
        + "@"
        + get_random_string(5)
        + "."
        + random.choice(["com", "org", "net", "su", "ru"])
    )
