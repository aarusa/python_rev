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
days = ["sun", "mon", "tue", "wed"]
weekends = ["sun", "sat"]
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")

# scan emails to block unsafe data from entering your system
