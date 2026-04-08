score = 90
# if score >= 90:
#     print("good")

score = 30
# if score >= 90:
#     print("good")
# else:
#     print("try again")

score = 88
# if score >= 90:
#     print("good")
# elif score >= 80:
#     print("not bad")
# else:
#     print("try again")

# Inline if (ternary)
# print("good" if score >= 90 else "try again")
# print("good" if score >= 90 else "not bad" if score >= 80 else "try again")

# match case
# Evaluate a value against multiple possible values
# Runs the code of the first match
# Convert the full country names into 2-letter abbreviations
country = "Nepal"
# if country == "Nepal":
#     print("NP")
# elif country == "Germany":
#     print("DE")
# else:
#     print("Unknown country")

country = input("Enter country:").lower()
# can be used for matching values only and works with python version 3.10+ only
# match case
match country:
    case "nepal":
        print("NP")
    case "germany":
        print("DE")
    case "egpyt":
        print("EG")
    case "australia":
        print("AU")
    case "united states" | "usa" | "us":
        print("US")
    case _:
        print("Unkown Country")