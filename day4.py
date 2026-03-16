# lambda

# decorator


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print(f'{text} {func.__name__}()')
            func(*args, **kw)
        return wrapper
    return decorator


@log("execute:")
def say_hi():
    print("Hi!")


say_hi()
