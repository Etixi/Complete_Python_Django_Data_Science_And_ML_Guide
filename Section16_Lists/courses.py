"""
        Lists Methods
        ==============
        - append
        - pop
        - remove
        - insert
        - sort
        - index
        - clear
        - copy
        - extend
        - reverse
        - count
"""
print("================ List: APPEND =================")
happy_smiles = []
happy_smiles.append('😀')
happy_smiles.append('😅')
happy_smiles.append('😏')
happy_smiles.append('😊')

print(happy_smiles)

print(len(happy_smiles))


print("================ List: POP =================")
inputs = [True, 'hi!','😎', 10.5]

inputs.pop() # removed 10.5
print(inputs)

inputs.pop(0) # removed True
print(inputs)

removed_element = inputs.pop() # removed '😎'
print(removed_element)
print(inputs) # ['hi']


print("================ List: SORT =================")
posts_ids = [245, 151, 762, 167]
posts_ids.sort()
print(posts_ids)

posts_ids.sort(reverse=True)
print(posts_ids)

print("================ CONVERSION TO A LIST =================")
greeting = "Hello from Python"
greeting_letters = list(greeting)
print(greeting_letters)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)


print("================ ARITHMETIC OPERATIONS IN LISTS =================")
ratings = [2.5, 5.0, 4.3, 3.7]
print(min(ratings))
print(max(ratings))
print(sum(ratings))

print(sum(ratings)/len(ratings))

my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)

print("================ List Slicing =================")
ratings = [2.5, 5.0, 4.3, 3.7, 4.5]
first_two_ratings = ratings[:2]
print(first_two_ratings)
middle_ratings = ratings[1:-1]
print(middle_ratings)
last_two_ratings = ratings[-2:]
print(last_two_ratings)

print("================ Copying Lists =================")
my_cars = ['BMW', 'Mercedes']
copied_cars = my_cars
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars))

my_cars1 = ['BMW', 'Mercedes']
copied_cars = my_cars1[:]
copied_cars.append('Audi')
print(copied_cars)
print(my_cars1)
print(id(my_cars1) == id(copied_cars))

my_cars2 = ['BMW', 'Mercedes']
copied_cars = my_cars2.copy()
copied_cars.append('Audi')
print(copied_cars)
print(my_cars2)
print(id(my_cars2) == id(copied_cars))

my_cars3 = ['BMW', 'Mercedes']
copied_cars = list(my_cars3)
copied_cars.append('Audi')
print(copied_cars)
print(my_cars3)
print(id(my_cars3) == id(copied_cars))
