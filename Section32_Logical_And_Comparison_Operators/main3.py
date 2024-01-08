print()
print("Practice - Combining OR and  AND Operator" + "\n" +
      "=========================================")
print()

print('' or print('CALLED'))
print('' or 0 or [] and {} and print('CALLED'))
print('apple' and 'banana')
print(('apple' or 'banana') and 'strawberry')
print('' or 'banana' and 'strawberry')
print(0 and 'banana' or 'strawberry')
print((10 > 100 and print('CALLED')) or ('banana' and 'strawberry'))
print(('apple' and print('CALLED')) or ('banana' and 'strawberry'))