# Create an @authenticated decorator that only allows the function to run if user has 'valid' set to True:
valid_user = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}

invalid_user = {
    'name': 'Test',
    'valid': False
}


def authenticated(fn):

    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            print("Invalid User")

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(valid_user)
message_friends(invalid_user)
