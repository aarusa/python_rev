# values: True and False
# Functions: bool(), all(), any(), isinstance(), startswith(), endswith()

# bool()
# True: if the value is non-empty or non-zero
# False: if the value is empty or zero
# print(bool())
# print(bool("hi"))
# print(bool(""))
# print(bool(0))
# print(bool(None))

# all and any functions
# all: returns True if all elements of the iterable are true (or if the iterable is empty).
# any: returns True if any element of the iterable is true. If the iterable is empty, return False.
# print(all([True, True, True]))
# print(all([True, False, True]))
# print(any([True, False, True]))
# print(any([False, False, False]))   

email = ""
phone = "123-456-7890"
username = ""

# Allows registration if at least one of the fields is filled
# print(any([email, phone, username]))

# Needs all fields to be filled for registration
# print(all([email, phone, username]))

# print(isinstance(email, str))
# print(isinstance(phone, str))
# print(isinstance(username, str))    

# print("Hello".startswith("o"))
# print("Hello".endswith("o"))

# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Memberhip operators: in, not in
# Identity operators: is, is not

# print(10 == 2)

# Allow access only if the user is logged in or are guest but they must not be in banned list
is_logged_in = True
is_guest = False
is_banned = True

# print((is_logged_in or is_guest) and not is_banned)

# Membership in operator
# print('a' in "Data")
# print('o' not in "Data")

# print("Engineering" in "Data")

# print("Banana" in ["Apple", "Cherry"])

# used for quality checks
# print("arusha.com.np" not in ["hacked.com", "blacklisted.com", "domain.spam.com", "fake.org"])
# print("fake.org" not in ["hacked.com", "blacklisted.com", "domain.spam.com", "fake.org"])

# identity operators
a = b = 5
print(a is b)


# Use case: make sure email exists and is not empty
# email = "xy@gmail.com"
email = None
print(email != "" and email != None)

print(email is not None and email != "") #best practices to use is not for comparing None value

