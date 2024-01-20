print()
print("Example - Validating Arguments With Decorator Functions" + "\n" +
      "==============================================================")
print()

def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Arguments must be integers!", f"{arg} is of type {type(arg)}")
        return fn(*args, **kwargs)
    return wrapper

@validate_args
def sum_nums(a, b):
    return a + b

try:
    print(sum_nums(5, 2))
    print(sum_nums('5', 2))
except ValueError as e:
    print(e)