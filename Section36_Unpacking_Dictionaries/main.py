print()
print("Practice - Using the Dictionary Unpacking" + "\n" +
      "===============================================")
print()

person = {'name': 'John', 'age': 23}

# other_person = person.copy()
# other_person['age'] = 30

other_person = {
    **person,
    'age': 30,
    'occupation': 'teacher'
}
print(person)
print(other_person)
print(id(person) == id(other_person))
