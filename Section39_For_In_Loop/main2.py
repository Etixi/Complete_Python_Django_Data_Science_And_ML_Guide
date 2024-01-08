print()
print("Practice - Iterating Through Dictionaries Using For-In-Loops" + "\n" +
      "==========================================================")
print()


product_prices = {
    'PC':1000,
    'Mobile Phone': 200,
    'Tablet' : 350,
    'Camera': 700
}

# for key in product_prices:
#     print(key)
#     print(product_prices[key])


# print(type(product_prices.items()))

for k, v in product_prices.items():
    print(k, v)