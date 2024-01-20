print()
print("Example - Calculating Discounts with the Ternary Operator" + "\n" +
      "==========================================================")
print()

def check_discount_eligibility(is_member):
    discount = 0.1 if is_member else 0.05
    return discount

customer_membership = False
discount_percentage = check_discount_eligibility(customer_membership)
print(discount_percentage)