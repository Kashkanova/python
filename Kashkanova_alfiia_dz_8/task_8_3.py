from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        i = 0
        s = f'{func.__name__}('
        for item in args:
            if i != 0:
                s+= ', '
            i += 1
            s += (f'{item}:{type(item)}')
        for item in kwargs:
            if i != 0:
                s+= ', '
            i += 1
            s += (f'{item}={kwargs[item]}:{type(kwargs[item])}')
        s += (')')
        print(s)
        return func(*args, **kwargs)
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3
a = calc_cube(5)
print(a)

@type_logger
def test_func(*args, **kwargs):
    #print(args, kwargs)
    return
test_func(5, 8.5, 'f', some_named_arg=110)
