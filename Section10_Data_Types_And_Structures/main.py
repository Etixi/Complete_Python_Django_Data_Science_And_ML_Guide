#  Created By Etienne KOA


print("=" * 60)
print(" Using the built-in id() Function ")
print("=" * 60)


print(id(print()))

my_name = "etixi"
print(id(my_name))

my_num = 123
print(id(my_num))

other_num = my_num
print(id(other_num))
print(id(my_num) == id(other_num))

print("=" * 60)
print(" Exploring Core Data Classes(str, int, bool, dict, list) ")
print("=" * 60)

"""
        Variables Types
        ===============
            + str
            + int
            + bool
            + list
            + dict
"""

my_num = 123
print(type(my_num) == int)

print(type(int))
print(type(str))
print(type(bool))
print(type(list))
print(type(dict))

print(type("etixi") == str)


print("=" * 60)
print(" Using the built-in isinstance() Function ")
print("=" * 60)

print(isinstance(123, int))
print(isinstance(123, object))
print(isinstance("etixi", str))
print(isinstance("etixi", object))
print(type(object))
