print()
print("Practice - Using **kwargs to Merge Keyword Arguments ina Dictionary" + "\n" +
      "====================================================================")
print()

def product_price_info(product_title, product_price):
    print(f'{product_title} costs {product_price}$')

def product_price_info_kwargs(**product):
    print(product)

def product_price_info_kwargs_args(**product):
    print(f"{product['product_title']} costs {product['product_price']}$")

def product_price_info_kwargs_params(**product):
    title = product['product_title']
    price = product['product_price']
    print(f"{title} costs {price}$")

product_price_info_kwargs(product_title="Bottle of water", product_price=2, product_availibility=True)
product_price_info_kwargs_params(product_title="Bottle of water", product_price=2)
product_price_info("Bottle of water", 2)


