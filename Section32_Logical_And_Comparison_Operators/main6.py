print()
print("The del statement" + "\n" +
      "=========================================")
print()

my_dict = {'a': True, 'b': 10, 'c': 'Etienne'}
del my_dict['a']
my_dict.__delitem__('b')
print(my_dict)
print(my_dict.__delitem__)