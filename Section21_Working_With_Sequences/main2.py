print()
print("Practice - Converting a zip Objects to a Dictionary" + "\n" +
      "=====================================")
print()

products = ['phone', 'tablet', 'laptop']
quantiles = [343, 13, 74]


products_zip = zip(products, quantiles)
products_dict = dict(products_zip)

print(products_dict)