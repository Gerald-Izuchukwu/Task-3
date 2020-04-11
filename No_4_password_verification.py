# Accepted Validation:
# At least 1 letter between a-z.
# At least 1 number between 0-9.
# Minimum length 8 characters.
# Maximum length 16 characters.

import re
user_password = input("Input your password: ")
test = True
while test:
    if (len(user_password)) < 8 or (len(user_password)) > 16:
        break
    elif not re.search("[a-z]", user_password):
        break
    elif not re.search("[0-9]", user_password):
        break
    elif re.search("\s", user_password):
        break
    else:
        print("Password Accepted")
        test = False
        break

if test:
    print("Not a Valid Password")
