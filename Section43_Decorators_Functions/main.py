print()
print("Introduction to Decorator Functions" + "\n" +
      "======================================================")
print()

def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):

        print(args)
        print(kwargs)

        # Some actions before execution, of the fn function
        print("Executed before function")

        result = original_fn(*args, **kwargs)

        # Some actions after execution of the original_fn function
        print("Executed after function")

        return result

    return wrapper_function

@decorator_function
def my_function(*args, **kwargs):
    print("This is my function")


my_function(10, name="Etienne")

