import re

print("=========== Built-In re Module for Regular Expressions ==============")

my_string = "My name is Etienne"

res = re.search('Etienne', my_string)
print()
print(res)
print(res.endpos)
print(type(res))

res = re.search('Etienne$', my_string)
print()
print(res)
print(res.endpos)
print(type(res))

res = re.search('^Etienne', my_string)
print()
print(res)
print(type(res))

res = re.search('^M.*', my_string)
print()
print(res)
print(type(res))

res = re.search('^M.*Etienne$', my_string)
print()
print(res)
print(type(res))

my_string = "My name is Etienne"
res = re.search(r'^M.*Etienne\.$', my_string)
print()
#print(res.span())
#print(res.start())
#print(res.end())
print(res)

print()
print('^M.*Etienne\n$')
print(r'^M.*Etienne\n$')

print()
print("=========== Example - Creating Patterns for Matching ==============")
print()

my_string = "My name is Etienne"

#my_pattern = re.compile(r'^M.Etienne\.$')

#print(my_pattern)
#print(type(my_pattern))
#print(my_pattern.search(my_string))

my_pattern = re.compile(r'E.....e')
print(my_pattern)
print(type(my_pattern))
print(my_pattern.search(my_string))
print(my_pattern.search("Hello, this is Etiiiie"))
print(my_pattern.match('Etiiiie'))
print(my_pattern.match('Etienne!!!!'))


print(my_pattern.findall("My name is Etienne. Hello Etienne"))

print()
print("=========== Example - Email Validation using Regular ==============")
print()

def validate_email(email):
    email_regexp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email_pattern = re.compile(email_regexp)
    is_valid = bool(email_pattern.match(email))
    return (email, is_valid)

"""
if email_pattern.match('b.s@gmail.com'):
    print("Email is valid")
else:
    print("Email is invalid")
"""

print(validate_email('etienne@gmail.com'))
print(validate_email('etiennegmail.com'))
print(validate_email('etienne@gmailcom'))

print()
print("=========== Example - Substring Remplacement using Regular Expressions ==============")
print()

regexp = r'bad' # r'a'

my_text = "Something bad is here. bad situation. bad words"

changed_text = re.sub(regexp, '*', my_text)

print(changed_text)

print()
print("=========== Example - Removing Excessive Space using Regular Expressions ==============")
print()

my_text = "This is   a very     long          unformatted         sentence"
print(text)
regexp = r'\s+'
words = re.split(regexp, my_text)
print(words)
print(' '.join(words))
print(my_text.split(' '))

#print(' '.join(my_text.split(' ')))