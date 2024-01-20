from Section50_Modules.src import utils as u, utils as my_utils
from Section50_Modules.src.utils import my_name as name
from Section50_Modules.src.utils import *
from Section50_Modules.src.other import sum_fn

print(utils)
print(type(utils))
print(dir(utils))
print(utils.my_name)
print(utils.hello(utils.my_name))

print(u)
print(type(u))
print(dir(u))
print(u.my_name)
print(u.hello(u.my_name))

print(hello('Etienne'))
print(name)
print(dir())

my_name = 'Alice'
print(hello('Etienne'))
print(my_name)
print(dir())


print(sum_fn(10, 2))
print(my_utils.hello('Etienne'))
print(my_utils.my_name)


def main():
    print("Running main block of code")