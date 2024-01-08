print()
print("Practice - Utilizing The Ternary Operator" + "\n" +
      "===============================================")
print()

def convert_status_to_str(is_active):
    return "Active" if is_active else "Inactive"

user_is_active = False
user_status = convert_status_to_str(user_is_active)
print(user_status)