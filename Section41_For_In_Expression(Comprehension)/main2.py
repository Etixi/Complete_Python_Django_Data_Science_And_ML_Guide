print()
print("Practice - Using Dictionary Comprehension" + "\n" +
      "========================================"
      )
print()

fruits = ['banana', 'mandarin', 'orange', 'apple']
fruit_length = {fruit:len(fruit) for fruit in fruits}
print(fruit_length)