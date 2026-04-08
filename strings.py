# Types:
# type(): checks string type
# str(): converts to string type

# -------------------------------------
# Math:
# len(): counts each character
# count(): counts the appearance of a word/special character in a string

# text = """
# Python is easy to learn.
# Python is powerful.$
# Many people love python.
# """
# #function: counts each character
# print(len(text))

# #method: counts the appearance of word in a string
# print(text.count("Python"))
# print(text.count("$"))

# -------------------------------------
# Transformations
# replace(): replace a character
# price = "12,453.00"
# print(price.replace(",","."))

# phone = "+61-041-1234-23"
# print(phone.replace("-", ""))

# price = "$1,399.99"
# print(price.replace("$", "").replace(",", ""))

# Challenge
# +49 (176) 123-4567 -> 00491761234567
# phone = "+49 (176) 123-4567"
# print(phone.replace("+", "00").replace("(","").replace(")","").replace("-","").replace(" ",""))

# String concatenation
# first = "Arusha"
# last = "Shahi"
# name = first + " " + last
# print(name)

# + operator in real project
# folder = "C:/Users/Arusha/"
# file = "report.csv"
# full_path = folder + file
# print(full_path)

# f-string: formatted string
# name = "Arusha"
# age = 29
# is_student = False
# print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")
# print(f"2 + 3 = {2+3}")
# print(f"{{This is me.}}")

# Split
# data = "arusha-29-victoria"
# print(data.split("-"))

# csv_file = "123, Arusha, Nepal, 1991-02-06, F"
# print(csv_file.split(", "))

# print("="*50)

# Extracting specific parts of the string
# text = "Python"

# print(text[0])
# print(text[-6])

# print(text[0:2])
# print(text[-6:-4])

# string_length = len(text)
# print(text[string_length-1])

# date = "2026-04-09"

# #Extract year
# print(date[0:4])
# print(date[:4])

# # Extract month
# print(date[5:7])

# #Extract date
# print(date[8:10])

# print(date[-2:])

# -------------------------------------
# Cleaning

# name = '  Max    '
# print(name.lstrip()) #left
# print(name.rstrip()) #right
# print(name.strip()) #left + right

# text = "Data Engineering"
# print(text.strip()) #Doesn't remove white spaces in middle

# name = '###Arusha###'
# print(name.strip("#"))

# Case conversions
# text = "python ProGRamming"
# print(text.lower())
# print(text.upper())

# search = "Email ".lower().strip()
# text = "email".lower()

# print(search == text)

# Challenge
# "968-Maria, ( D@t@ Engineer );; 27y  " => name:maria | role:data engineer | age:27
# text = "968-Maria, ( D@t@ Engineer );; 27y  "
# name = text[4:9].lower()
# role = text[13:26].lower().replace("@","a")
# age = text[31:33].lower()
# print(f"name:{name} | role:{role} | age:{age}")

# Search
# date = "2026-Feb-10"
# print(date.startswith("2026"))
# print(date.endswith("30"))
# print("Feb" in date)

# find specific position
# find()

# real world implementation
# phone = "+61 452497529"
# email = "shahiarusha@gmail.com"

# print(phone.startswith("+61"))
# print(email.endswith("gmail.com"))

# file = "data_backup.csv"
# print(file.endswith(".csv"))

# # email validation: check if it has @
# print("@" in email)

# url = "https://api.arusha.com.np"

# print("/api" in url)

# phone1 = "+34 54523422"
# phone2 = "+041 34242342"
# phone3 = "00041 34242342"

# print(phone1[phone1.find(" ")+1:])
# print(phone2[phone2.find(" ")+1:])
# print(phone3[phone3.find(" ")+1:])

# -------------------------------------
# Validation
# country = "USA"
# print(country.isalpha())

# phone = "0423-452123"
# print(phone.isnumeric())


flower = "Rhododendron"
# print(flower[0:])
print(flower[::-1])
print(flower[-4::-1])

print('Example'[2:0:-1])

