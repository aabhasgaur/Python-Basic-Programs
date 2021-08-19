#Check if the password is a strong Password
import re

"""
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
while True:
    password=input("Enter the Password to be checked:")
    is_valid=False

    if (len(password)<8):
        print("Password length should be equal to or less than 8.")
        continue
    elif not re.search(r"\d",password):
        print("Password should contain atleast 1 Digit.")
        continue
    elif not re.search(r"[A-Z]",password):
        print("Password should contain atleast 1 Uppercase Letter.")
        continue
    elif not re.search(r"[a-z]",password):
        print("Password should contain atleast 1 Lowercase Letter.")
        continue
    elif not re.search(r"\W",password):
        print("Password should contain atleast 1 Symbol.")
        continue
    elif re.search("[\s]",password):
        print("Password should not contain any spaces.")
        continue
    else:
        print("Password is Valid!")
        is_valid=True
        break
