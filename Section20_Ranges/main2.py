print()
print("Practice - Range Methods and Attributes" + "\n" +
      "=====================================")
print()

odd_nums = range(1, 100, 2)

print(list(odd_nums))
print(tuple(odd_nums))
print(set(odd_nums))
# print(dict(odd_nums))

print(odd_nums.index(51))
print(odd_nums.count(51))
print(odd_nums.start)
print(odd_nums.stop)
print(odd_nums.step)

print(" ")
my_range = range(5, 8)
print(my_range.start)
print(my_range.stop)
print(my_range.step)