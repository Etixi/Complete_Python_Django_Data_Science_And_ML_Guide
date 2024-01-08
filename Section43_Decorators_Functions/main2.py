print()
print("Example - Logging using Decorator Functions" + "\n" +
      "==============================================================")
print()

def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling functions {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Result of the function is {res}")
        return res

    return wrapper

@log_function_call
def mult_numbers(a, b):
    return a * b

@log_function_call
def sum_numbers(a, b):
    return a + b


print(mult_numbers(10, 2))
print('')
print(sum_numbers(10, 2))
print('')
print(sum_numbers(a=50, b=5))
