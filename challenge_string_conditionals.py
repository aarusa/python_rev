# Check if a user's name is not empty and the age is greater than or equal to 18
name = ""
age = 45
# print((name is not None and name != "") and age >= 18)

# Check if the password is at least 8 characters long and does not contain spaces
# password = "  1 23 412 34"
# password = "hello_world"
# password = input("Enter password:")
# print(len(password)>=8 and (len(password.strip("")) == len(password)) and (len(password.replace(" ", "")) == len(password)))

# Check if user's email is not empty, contains '@', and ends with '.com'.
email = "a@gmail.com"
# email = None
# email = ""
# print((email != "" and email is not None) and '@' in email and email.endswith(".com"))

# Check if a username is a string, is not None, and is longer than 5 characters.
username = None
username = ""
username = "hello123"
# username = 123
# username = "123Hello"
# username = "@sdefe"
# username = "_arusha"
# print(isinstance(username, str) and username is not None and len(username) > 5)

# Check if username strictly begins with string and not integer
# print(isinstance(username, str) and use rname is not None and len(username) > 5 and username[0].isalpha())

# Check if username does not begins with an integer but can have anything else (strings or special characters).
# print(isinstance(username, str) and username is not None and len(username) > 5 and not username[0].isdigit())

# Check if the user is an admin or moderator, and either they're not banned or they've verified their email
is_admin = False
is_moderator = True
is_banned = False
is_email_verified = True
# print(((is_admin or is_moderator) and is_email_verified) and not is_banned)

# Check and validate the quality and correctness of the email values
# - must not be empty
# - must contain '.' and '@'
# - must contain exactly one '@' symbol
# - must end with '.com', '.org', or '.net'
# - must not be longer than 254 characters
# - must start and end with a letter or digit

email = "sha@hiarusha@gmailcom#"
email = "shahiarusha@gmail.com"
valid = True

# first clean the string
email = email.strip()

# to get all the validation errors at once use independent if statements
# - must not be empty
if email == "":
    print("Email cannot be empty.")
    valid = False
# - must contain '.' and '@'
if not("@" in email and "." in email):
    print("Email must contain . and @")
    valid = False
# - must contain exactly one '@' symbol
if not(email.count("@") == 1):
    print("Email must contain only 1 @")
    valid = False
# - must end with '.com', '.org', or '.net'
# elif not(email.endswith('.com') or email.endswith('.org') or email.endswith('.net')):
if not(email.endswith(('.com', '.net', '.org'))):
    print("Only .com, .net, and .org are accepted.")
    valid = False
# - must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters.")
    valid = False
# - must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and with with a letter or digit only.")
    valid = False
if valid:
    print("Email address is valid.")

# Checking everything
# if((email != "" and email is not None) and '@' in email and '.' in email and email.count('@') == 1 and (email.endswith('.com') or email.endswith('.org') or email.endswith('.net')) and len(email) <= 254 and email[0].isalnum() and email.split('@')[0][-1].isalnum()):
#     print("Email address is valid.")
# else:
#     print("Invalid email address.")

# Validate the Quality and correctness of passwords
# Must not be empty
# Must be at least 8 characters long
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be same as the email
# Must not contain any spaces
# Must start and end with  a letter or digit

import string
password = "@1Sahiarusha@gmail.com"
# password = input("Enter password:")
password_valid = True

# Must not be empty
if password == "":
    print("Password must not be empty.")
    password_valid = False
# Must be at least 8 characters long
if len(password)<8:
    print("Password must atleast be eight characters long.")
    password_valid = False
# Must include at least 1 uppercase
if not any(char.isupper() for char in password):
    print("Password must contain atleast one uppercase letter.")
    password_valid = False
# Must include at least 1 lowercase
if not any(char.islower() for char in password):
    print("Password must contain atleast one lowercase letter.")
    password_valid = False
# Must not be same as the email
if password == email:
    print("Password must not be same as email.")
    password_valid = False
# Must not contain any spaces
if len(password.strip()) != len(password) or " " in password: #should be invalid if there's space in mid
    print("Password must not contain spaces.")
    password_valid = False
# Must start and end with  a letter or digit
if not(password[0].isalnum and password[-1].isalnum):
    print("Password should start and end with letter or number")
    password_valid = False
# Must have atleast one number
if not any(char.isnumeric() for char in password):
    print("Password must contain atleast one number.")
    password_valid = False
# Must have atleast one special character
if not any(char in string.punctuation for char in password):
    print("Password must contain atleast one special character.")
    password_valid = False
# Check password validity
if password_valid:
    print("Password is valid.")


