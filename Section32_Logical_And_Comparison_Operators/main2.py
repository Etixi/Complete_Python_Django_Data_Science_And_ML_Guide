print()
print("Practice - Short-Circuit AND Operator" + "\n" +
      "=========================================")
print()

print('' and print('CALLED'))
print('' and 0 and [] and {} and print('CALLED'))
print('apple' and 'banana')
print('apple' and 'banana' and 'strawberry')
print('' and 'banana' and 'strawberry')
print(0 and 'banana' and 'strawberry')
print(10 > 100 and print('CALLED') and 'banana' and 'strawberry')
print('apple' and print('CALLED') and 'banana' and 'strawberry')