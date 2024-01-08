print("================ Practice - Working with Lists =================")
my_nums = [10, 3, 100, 35, 100]
other_nums = [351, 245, 425]
my_list = [True, None, 'abc', 10, 10.5, [1,2], {'name': 'Bogdan'}]

print(my_nums)
print(type(my_nums))
print(isinstance(my_nums, list))
print(my_nums[0], my_nums[-1],my_nums[2])
print(id(my_nums))
my_nums.append(50)
print(id(my_nums))
print(my_nums)
my_nums.pop(2)
print(my_nums)
print(len(my_nums))
my_nums.extend([34, 62, 'abc'])
print(my_nums)
print(my_nums.index(100))
print(my_nums)
my_nums.append(50)
print(my_nums)
merged_nums = my_nums + other_nums
# merged_nums = my_nums.__add__(other_nums)
print(merged_nums)
my_nums[2] = 0
my_nums.clear()
print(my_nums)
print(my_list)

print("================ Practice - Copying Lists =================")
my_list = [10, 'abc', True]
copy_of_my_list = my_list

copy_of_my_list.append(None)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))

my_list = [10, 'abc', True]
copy_of_my_list = my_list.copy()

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))

my_list = [10, 'abc', True]
copy_of_my_list = list(my_list)

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))

my_list = [10, 'abc', True]
copy_of_my_list = my_list[:]

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))

my_list = [10, 'abc', True]
copy_of_my_list = my_list

copy_of_my_list.append(100)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))
print(id(my_list))
print(id(copy_of_my_list))