def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res)


def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy

person_one = {
    'name':'bob',
    'age': 24
}

new_person = increase_person_age(person_one)
print(new_person)
print(new_person['age'])
print(person_one['age'])