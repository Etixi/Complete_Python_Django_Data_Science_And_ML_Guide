print()
print("Practice - Incorporating if Statements into Functions" + "\n" +
      "======================================================")
print()

def check_divisibility(num: int, divider1: int, divider2: int):
    if num % divider1 == 0 and num % divider2 == 0:
        print(f"Number is divisible by {divider1} and {divider2}")
    elif num % divider1 == 0:
        print(f"Number is divisible only by {divider1}")

    elif num % divider2 == 0:
        print(f"Number is divisible only by {divider2}")
    else:
        print(f"Number is not divisible by {divider1} or by {divider2}")


check_divisibility(15, 4, 1)
check_divisibility(20, 4, 5)
check_divisibility(15, 5, 3)