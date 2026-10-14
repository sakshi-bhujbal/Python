def decorator(func):
    def wrapper():
        print("The msg before func call")
        func()
        print("The ms after function call")
    return wrapper

@decorator
def greet():
    print("Hello, world!")
