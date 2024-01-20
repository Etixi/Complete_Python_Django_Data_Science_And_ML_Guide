print()
print("Practice - Using List Comprehension" + "\n" +
      "========================================"
      )
print()

# Without List Comprehension
nums = [10, 2, 5, 100]

squared_nums = []

for num in nums:
    squared_nums.append(num * num)

print(squared_nums)

# Using List comprehension

nums = [10, 2, 5, 100]

squared_nums = [num * num for num in nums]
print(nums)
print(squared_nums)