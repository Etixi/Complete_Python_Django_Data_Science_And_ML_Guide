print("Practice - Calculating Symmetric Difference of Set" + "\n" +
      "======================================================")
print()

my_set = {'a', 'c', 'd'}
other_set = {'l', 'm', 'c'}

print(my_set.symmetric_difference(other_set))
print((my_set | other_set) - (my_set & other_set))