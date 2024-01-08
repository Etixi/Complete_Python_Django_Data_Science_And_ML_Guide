print()
print("Practice - Short-Circuit OR Operator" + "\n" +
      "=========================================")
print()

print('' or print('CALLED'))
print('' or 0 or [] or {} or print('CALLED'))
print('apple' or 'banana')
print('apple' or print('CALLED') or 'banana' or 'strawberry')
