print()
print("Practice - Short For-In Loops With Conditional Statements" + "\n" +
      "========================================"
      )
print()

person = {
    'name': 'Bogdan',
    'favorite_num': 3,
    'is_instructor': True
}

person_str_values = [value for value in person.values() if type(value) == str]
print(person_str_values)

