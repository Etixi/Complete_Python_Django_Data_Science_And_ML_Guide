my_motorbike= {
    'brand': 'Ducati',
    'price': 2500,
    'engine_vol': 1.2
}

other_motorbike = {
    'price': 2500,
    'engine_vol': 1.2,
    'brand': 'Ducati',
}

print(my_motorbike['brand'])
print(my_motorbike['price'])

my_motorbike['price'] = 2000
print(my_motorbike['price'])

my_motorbike['is_new'] = True
print(my_motorbike)

del my_motorbike['engine_vol']
print(my_motorbike)

key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike)


print(id(my_motorbike) == id(other_motorbike))
print(my_motorbike == other_motorbike)