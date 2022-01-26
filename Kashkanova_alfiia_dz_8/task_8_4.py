from functools import wraps

def val_cheker(lambda_func):
    def _val_cheker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if lambda_func(args[0]) is False:
                raise ValueError('неверное входное значение')
            return func(*args, **kwargs)
        return wrapper
    return _val_cheker

@val_cheker(lambda x: x > 0)
def calc_cube(x):
    print(calc_cube)
    return x ** 3
a = calc_cube(5)
print(a)