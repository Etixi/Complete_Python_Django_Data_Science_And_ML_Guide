print()
print("Practice - Dictionary Methods" + "\n" +
      "=====================================")
print()

my_bike = {
    'brand': 'Custom',
    'price': 2000
}

other_bike = my_bike
other_bike['color'] = 'red'
print(my_bike)
print(other_bike)

keys = list(my_bike.keys())
print(type(keys))
print(keys)

print(my_bike.values())
print(my_bike.items())