# Print the 7 times table from 1 to 10 using a for loop
# for i in range(1,11):
#     print(f"7 * {i} = {7 * i}")

# Print left aligned pyramid of stars with 6 rows
# for i in range(7):
#     print(i * "*")

# break, continue and pass
# for i in range(20):
#     print(i)
#     if i == 4:
#         break

names = ['john', 'maria', '', 'evelyn']

# for name in names:
#     if name == '':
#         print("Empty value detected!")
#         break
#     print(f"Name: {name}")

# for name in names:
#     if name == '':
#         print(f"Empty value detected!")
#         continue
#     print(f"Name: {name}")

# pass is like a placeholder, eg: we know smth needs to be done, but don't know the solution yet.
# so to not forget the condition, just add pass
# for name in names:
#     if name == '':
#         pass #todo: handle empty value
#     print(f"Name: {name}")


# Skip weekends in calender loop
# days = ["sun", "mon", "tue", "wed"]
# weekends = ["sun", "sat"]
# for day in days:
#     if day in weekends:
#         continue
#     print(f"Workday: {day}")


# scan emails to block unsafe data from entering your system
emails = [
    'shahiarusha@gmail.com',
    'datawithbaraa@outlook.de',
    'DROP TABLE USERS;',
    'hi@support.co'
]

# for email in emails:
#     # check if there's a semi-colon(;) in email
#     if ';' in email:
#         print('SQL Injection Detected: Hacker Attack')
#         break
#     print(f"Processing email: {email}")


# break: High/Critical Risk - Exit immediately: cost, security, integrity
# continue: Medium Risk - Bad rows, Empty Files/Data, Skip special cases
# pass: No Risk - Just a placeholder - Future planning for solution

# for - else: else is executed only if for loop is completed
# check for even number
# items = [1,9,5,7]
# for item in items:
#     if item % 2 == 0:
#         print("Even number is found:", item)
#         break
# else:
#     print("All numbers are odd.")

# Check for missing names in list
# names = ['Karma', 'Tuba', None, 'Mona']

# for name in names:
#     if name == None:
#         print("Found a missing name.")
#         break
# else:
#     print("No missing value.")


# Check if all files are csv
files = ['data1.csv', 'report.pdf', 'summary.csv', 'data2.txt']
flag = True

for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not CSV")
        flag = False
        continue
else:
    if flag:
        print("All files are CSV")