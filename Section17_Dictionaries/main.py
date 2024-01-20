print()
print("Practice - Manipulating Dictionaries" + "\n" +
      "=====================================")
print()

my_bike = {
    'brand': 'Custom',
    'price': 2000
}

other_bike = {
    'price': 2000,
    'brand': 'Custom'
}

print(my_bike == other_bike)

print(my_bike)
print(type(my_bike))
print(len(my_bike))
print(id(my_bike))

print(my_bike['brand'])
print(my_bike['price'])

my_bike['max_speed'] = 50
print(id(my_bike))
print(my_bike)