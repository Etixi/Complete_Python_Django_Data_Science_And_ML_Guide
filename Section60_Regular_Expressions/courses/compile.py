import re

pet = re.compile(r'dog')
print(type(pet))

print(bool(pet.search('They bought a dog')))
print(bool(pet.search('A cat crossed their path')))


pat = re.compile(r'\([^)]*\)')
print(pat.sub('', 'a+b(addition) - foo() + c%d(#modulo)'))
print(pat.sub('', 'Hi there(greeting). Nice day(a(b)'))
