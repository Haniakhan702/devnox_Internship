#Custom Exception for Password Validation
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)

class WeakPasswordError(Exception):
    pass


def check_password(password):
    try:
        if len(password) < 8:
            raise WeakPasswordError("Password must contain 8 characters.")
        
        print("Password accepted.")

    except WeakPasswordError as e:
        logging.error(e)


password = input("Enter password: ")
check_password(password)