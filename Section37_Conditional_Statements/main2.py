print()
print("Practice - Combining if,elif and else Statements" + "\n" +
      "===============================================")
print()

def check_shipping_fee(weight):

    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")

    if weight <= 5:
        print("The shipping fee is 5$")

    if weight <= 15:
        print("The shipping fee is 10$")

    else:
        print("The shipping fee is 20$")


check_shipping_fee(100)