print()
print("Practice - Utilizing Tuples Comprehension" + "\n" +
      "========================================"
      )
print()

names = ['Bogdan', 'Alice', 'Bob']
names_lengths = tuple(len(name) for name in names)
print(names_lengths)