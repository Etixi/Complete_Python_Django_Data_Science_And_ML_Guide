brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2


my_motorbike = {
    'brand': brand,
    'engine_vol': engine_volume,
    'price_info': {
        'price': bike_price,
        'is_available':True
    }
}

print(my_motorbike)
print(my_motorbike['price_info']['price'])
print(my_motorbike['price_info']['is_available'])
print(len(my_motorbike))
del my_motorbike['price_info']['price']
print(len(my_motorbike))
print(my_motorbike.get('brand'))
print(my_motorbike.get('price'))
print(my_motorbike.get('qty', 0))
print(my_motorbike.get('model'))

my_dict = {}
print(my_dict.__doc__)

