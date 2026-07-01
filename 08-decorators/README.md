# Python Decorators

In Python, functions are `first-class citizes`, that means they are just variables.

```python
def hello():
    print("Hello World!!!")

greet = hello # We can assign it to a variable
del hello # It will work because greet already has a pointer to the location of hello

print(greet())
```

We can also pass functions as arguments for other functions

```python
def hello(fn):
    fn()

def greet():
    print("Hi from greet")

a = hello(greet)

print(a())
```

`Decorators` work because of this characteristic of functions being first-class citizens. Decorators modify our functions adding extra capabilities for them.
