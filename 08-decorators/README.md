# Python Decorators

## Functions in Python

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

## High Order Function (HOC)

A HOC is a function that accepts another function as a parameter or, a function that returns another function

```python
def greet(fn):
    fn()

def hoc_fn():
    def inner_fn():
        # do something
    return inner_fn
```

## Decorators

Decorators are functions wrapping another function, like a HOC.

```python
def my_decorator(fn):
    def wrap_fn():
        print("Print from decorator")
        print("****")
        fn()
        print("****")

    return wrap_fn

@my_decorator
def hello():
    print("Hello!!!")

@my_decorator
def bye()
    print("See you later")

hello()
```
