# Numeric
# int, float, complex
import math as m

x = 5
y = 1.2
z = 2 + 3j

# print(type(z))
# print(x*3)

# Rounding
# measure distance
# print(2-10)
# print(abs(2-10))

# price = 35.6360998883
# # print(round(price))
# print(round(price,2))
# print(m.floor(price))
# print(m.ceil(price))

# # To get rid of all the decimals
# print(m.trunc(price)) #if math is already there for other operations, use math otherwise use int() typecast
# print(int(price))

# x = 2
# print(m.sqrt(x))

import random

# to get random number
# print(random.random())

# to get a integer eg. for rolling a dice
# print(random.randint(1,6))

# used for generating dummy data for testing functions, pipelines, etc.
# eg. for age, suppose customer age is between 18-60: generate random data
# eg. for customer id, generate id between certain range

# Number Function Validation
x = 7.0
y = 7.1
# print(x.is_integer()) #is a whole number
# print(y.is_integer()) #is float number

# sometimes when output consists of 10.00, 14.00: they're actually integers but just have .00

# check if the value belongs to certain data type
# print(isinstance(x, int))
# print(isinstance(x, float))

# Challenge: generate a random number between 1 and 100 and check if it is even.
x = random.randint(1,100)
print(x)
if x % 2 == 0:
    print(True)
else:
    print(False) 


# printing remainder and quotient
print(divmod(10,3))

# printing random floating number
print(round(random.uniform(10.0, 50.0),2))

print('Python'[2::-1])