print()
print("Practice - Examples With Logical Operators" + "\n" +
      "=========================================")
print()

my_list = [1, 2]
other_list = ['a', 'b']

print(my_list or other_list)
print(bool(my_list or other_list))
print(not not (my_list or other_list))
print(not not my_list or other_list)

if my_list:
    print("List is not empty")

my_list and print("List is not empty")