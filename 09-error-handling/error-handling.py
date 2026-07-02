from numbers import Real

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


Number = int | float


def sum(num1: Number, num2: Number) -> Number:
    try:
        return num1 + num2
    except TypeError as err:
        print("Please use just numbers")
        raise TypeError(f"{err}")
