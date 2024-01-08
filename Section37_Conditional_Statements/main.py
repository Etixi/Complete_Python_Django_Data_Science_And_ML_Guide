print()
print("Practice - Working with multiple if Statements" + "\n" +
      "===============================================")
print()

def check_shipping_fee(weight):
    if weight <= 0:
        print("Invalid weight. Weight must be greater than zero")

    if 0 < weight <= 5:
        print("The shipping fee is 5$")

    if 5 < weight <= 15:
        print("The shipping fee is 10$")

    if weight > 15:
        print("The shipping fee is 20$")

check_shipping_fee(10.5)
check_shipping_fee(5)