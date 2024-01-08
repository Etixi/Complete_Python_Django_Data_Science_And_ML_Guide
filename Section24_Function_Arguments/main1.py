print()
print("Practice - Using Mutable and Immutable Object as Function Arguments" + "\n" +
      "===================================================================")
print()


def print_fruits_info(person_name, fruits):
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')


my_name = 'Etienne'
favorite_fruits = ['oranges', 'apples', 'bananas']

print_fruits_info(my_name, favorite_fruits)
print(favorite_fruits)

