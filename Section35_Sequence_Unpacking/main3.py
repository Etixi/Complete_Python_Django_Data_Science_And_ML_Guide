print()
print("Practice - Unpacking Remaining Elements" + "\n" +
      "========================================")
print()

person = ('Bob', 25)
name, age, *other = person

school_grades = (80, 75, 35, 20, 90)
first, second, *remaining = school_grades

print(name)
print(age)
print(other)


print('')
print(first)
print(second)
print(remaining)