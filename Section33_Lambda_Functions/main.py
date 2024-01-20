print()
print("Practice - Returning Lambda Functions from Functions" + "\n" +
      "========================================================")
print()



def multiply_by(multiplier):
    return lambda x : x * multiplier

multiply_by_3 = multiply_by(3)

print(multiply_by_3(10))
print(multiply_by_3(50))

multiply_by_5 = multiply_by(5)

print(multiply_by_5(10))
print(multiply_by_5(50))

