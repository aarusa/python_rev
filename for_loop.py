# for loop
# for i in (1,2,3):
#     print(i)

# for i in (1,2,3,4,5):
#     print(f"Round: {i}")

items = (1,2,3,4,5) #tuple
items = [1,2,3,4,5] #list
# for item in items:
#     print(item)

# fruits = ["apple", "banana", "cherry", "dragonfruit"]
# for fruit in fruits:
#     print(fruit)

# text = "Python"
# for i in text:
#     print(i)

# range
# range(start, stop): includes start but stop is not included
# for i in range(5):
#     print(i)

# for i in range(1,10):
#     print(i)

# range(start, stop, step): increment by step
# for i in range(2, 20, 2):
#     print(i)

# for i in sequence (sequence: string, tuple, list, range, dict, file)

# real world applications
files = [' Report.csv ', ' Data.csv ', 'final.TXT']

# First clean up data and then transform
for file in files:
    file = file.strip().lower().replace("txt", "csv")
    print(f"Processing {file}")


