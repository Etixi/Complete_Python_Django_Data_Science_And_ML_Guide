my_dict = {'a':10, 'b':[1,2]}

if my_dict: #len(my_dict) > 0:
    print("Dictionary is not empty")

if not my_dict: #len(my_dict) > 0:
    print("Dictionary is empty")

if my_dict['b']:
    print(("Key 'b' in the dictionary has value"))

if my_dict.get('b'):
    print(("Key 'b' in the dictionary has value"))


print(bool(10))
print(bool(3.6))
print(bool(3j))

print(bool(None))
print(bool(True))
print(bool(False))

print(bool('abc'))

print(bool([1, 2]))
print(bool({'a': 'abc'}))
print(bool((3, 5)))
print(bool(set()))
print(bool({10, 20}))
print(bool(range(0)))