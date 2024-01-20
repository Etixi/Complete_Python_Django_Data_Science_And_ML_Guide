print()
print("Example - Chaining For-In Expressions" + "\n" +
      "========================================"
      )
print()

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)