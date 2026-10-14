
import secrets
import string

print("!= Password Generator =!")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Password length must be at least 8.")
    else:
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        print("Your generated password:", password)

except ValueError:
    print("Please enter a valid number.")
