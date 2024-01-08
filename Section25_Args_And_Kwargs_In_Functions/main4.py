def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(10, True, 'abc', key=20, name='Bogdan')
# my_function(key=20, name='Bogdan', 10, True, 'abc')