age = input("What's your age? ")

try:
    age = int(age)
    # 10 / age
    print(f"Age: {age}")
except ValueError:
    print("Please enter a number")
    # raise ValueError("Please enter a number")
except ZeroDivisionError:
    print("Age can not be zeo")
else:
    print("Thanks")
