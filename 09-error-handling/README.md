# Error Handling

Error handling is handling exceptions risen by python's interpreter.

There different error types, we can find them here: https://docs.python.org/3/library/exceptions.html
In Python, all exceptions must be instances of a class that derives from BaseException. In a try statement with an except clause that mentions a particular class, that clause also handles any exception classes derived from that class (but not exception classes from which it is derived). Two exception classes that are not related via subclassing are never equivalent, even if they have the same name.

```python
class CustomException(Exception):
    pass


raise CustomException("Something went wrong")
```
