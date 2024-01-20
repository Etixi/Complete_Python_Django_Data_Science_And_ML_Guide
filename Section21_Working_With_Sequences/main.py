print()
print("Practice - Working With zip Objects" + "\n" +
      "=====================================")
print()

products = ['phone', 'tablet', 'laptop']
quantiles = [343, 13, 74]
tags = 'asd'

products_zip = zip(products, quantiles, tags)
print(products_zip)
print(type(products_zip))

# for product in products_zip:
#    print(product)

# for product in enumerate(products_zip):
#    print(product)


products_list = list(products_zip)
print(products_list)

