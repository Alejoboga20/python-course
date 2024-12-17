""" Data types in Python """
""" Python is a dynamically typed language, meaning that the type of a variable is determined at runtime """

""" Numbers: Integers, Floats, Complex numbers. We can perform arithmetic operations on numbers """
# Integers: Whole numbers
print(2 + 3)
print(type(2))

# Floats: Numbers with decimal points
print(2.0 + 3.0)
print(type(2.0))
print(type(2 + 3.0))  # The result is a float

# Complex numbers
print(2 + 3j)
print(type(2 + 3j))

# Arithmetic operations
print(2 + 3)  # Addition
print(2 - 3)  # Subtraction
print(2 * 3)  # Multiplication
print(5 / 3)  # Division
print(2 ** 3)  # Exponentiation
print(4 // 3)  # Floor division
print(5 % 3)  # Modulus

# Math functions
print(round(3.14159))  # Round to the nearest whole number
print(round(3.14159, 2))  # Round to 2 decimal places
print(abs(-3.14159))  # Absolute value
print(bin(5))  # Binary representation of a number
print(int('101', 2))  # Convert binary to integer

# augmeneted assignment operators
x = 2
x += 3  # x = x + 3
print(x)

""" Strings: strings are sequences of characters enclosed in quotes"""
greet = "Hello, World!"
print(type(greet))

username = "john_doe"
password = "password123"
long_string = """
    This is a long string
    that spans multiple lines
  """

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + last_name
print(f"Full name: {full_name}")

# Type conversion
age = 25
str_age = str(age)
print(type(str_age))
print(f"Age: {str_age}")

# Escape sequences (\n, \t, \", \', \\)
weather = "\t It's \"kind of\" \nsunny"
print(weather)
