# Custom Exception Class using Logging Module
import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)

# Create custom exception class
class InvalidAgeError(Exception):
    pass


def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be 18 or above.")
        else:
            print("You are eligible.")

    except InvalidAgeError as e:
        logging.error(e)


# Taking input from user
try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError:
    logging.error("Please enter a valid integer.")