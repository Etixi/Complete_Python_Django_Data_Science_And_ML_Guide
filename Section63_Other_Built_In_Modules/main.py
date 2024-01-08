print()
print("Built-In array Module" + "\n" +
      "=============================")
print()

from array import array

my_int_array = array('i', [10, 4, 3, 7, 9, 15])


print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))
print(my_int_array[2])
my_int_array.append(20)
print(my_int_array)
my_int_array.append(True)
print(my_int_array)
print(isinstance(True, bool))
print(isinstance(True, int))
print(int.__subclasses__())
my_int_array.pop(0)
print(my_int_array)