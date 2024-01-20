print()
print("Practice - Comparison Operators" + "\n" +
      "=========================================")
print()

a = [1, 2] #7
b = [1, 2] #10

print(id(a))
print(id(b))


print(a > b)
#a.__gt__
print(a >= b)
#a.__ge__
print(a < b)
#a.__lt__
print(a <= b)
#a.__le__
print(a == b)
#a.__eq__
print(a != b)
#a.__ne__

name = 'Bob'

if len(name)>4:
    print("Name is longer than 4 characters")

my_nums = (1, 3, 2, 6)
print(sum(my_nums))

if sum(my_nums) > 20:
    print("Sum is greater than 20")

my_nums = [10, 3, 5, 20]
print(sorted(my_nums))
if my_nums == sorted(my_nums):
    print("List is already sorted!")

other_nums = [3.5, 5.10, 7.75, 10.05]

if other_nums == sorted(other_nums):
    print("List other_nums is already sorted")

print(id(other_nums) == id(sorted(other_nums)))


