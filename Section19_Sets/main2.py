print()
print("Practice - Usage of the Set Methods" + "\n" +
      "=====================================")
print()

my_set = {10, 5}
other_set = {10, 5}

print(my_set.issubset(other_set))
print(other_set.issuperset(my_set))

my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

set_copy= other_set.copy()
set_copy.add(200)
print(set_copy)
print(other_set)

print(my_set.union(other_set))
print(other_set.union(my_set))
print(my_set.union(other_set) == other_set.union(my_set))
print(my_set | other_set)

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection((2, 100, 200)))
print(my_set & other_set)

print(my_set)
my_set.add(8)
print(my_set)
my_set.remove(5)
print(my_set)
my_set.discard(200)
print(my_set)