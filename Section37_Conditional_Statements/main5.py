def calc_discounted_price(price: float, is_member: bool):
    if is_member:
        return price - price * 0.9 # 10% discount

    return price - price * 0.05 # 5% discount


    # if is_member:
    #     return price - price * 0.1 # 10% discount
    # else:
    #     return price - price * 0.05 # 5% discount
    # return price - discount

res_price = calc_discounted_price(price=1000, is_member=True)
print(res_price)