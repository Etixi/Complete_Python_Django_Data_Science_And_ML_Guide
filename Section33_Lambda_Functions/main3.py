print()
print("Practice - Filtering a List using Lambda Functions" + "\n" +
      "========================================================")
print()

my_nums = [3, 4, 10, 20, 21]

print(10 % 2)
print(9 % 2)

even_nums = list(filter(lambda num : num % 2 == 0, my_nums))
print('Even numbers', even_nums)

odd_nums = list(filter(lambda num : num % 2 == 1, my_nums))
print('odd numbers', odd_nums)