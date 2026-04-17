# and

age = 25
licensed = True

if age >= 18 and licensed:
    print("Can drive")

# or

if age >=18 or licensed:
    print("Can drink")

# not

if not licensed:
    print("No license")
else:
    print("Has license")