import random

print()
print("====================== Built-In random Module ======================")
print()

print(dir(random))

# float
print(random.random())
print(random.uniform(10.5, 11.6))

# int
print(random.randint(100,1000))

# shuffle
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)

# choice
print(random.choice('Etienne'))
print(random.choice((1, 3, 10)))
print(random.choice(['a', True, None]))

print()
print("====================== Examples  Utilizing choices and shuffle Methods from the random Module  ======================")
print()

# choices
print(random.choices([1, 2, 3, 4, 5], k=5))
print(random.choices('abcdef', k=10))

# create password (not recommended)
print(''.join(random.choices('ABCDEF0123456789', k=12)))

# sample (unique elements)
print(random.sample([1, 2, 3, 4, 5], k=5))
print(random.sample([1, 2, 3, 4, 5], k=3))
#print(random.sample([1, 2, 3, 4, 5], k=10)) # ValueError
print(''.join(random.sample('ABCDEF0123456789', k=12)))
print(random.sample([1, 1, 1, 1], k=3))
print(random.sample(range(1_000_000), k=10))


print()
print("====================== Built-In Secrets Module  ======================")
print()

import secrets
import string

def generate_password(length:int):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # print(list(secrets.choice(all_chars) for i in range(10)))
    passowrd = ''.join(secrets.choice(all_chars) for _ in range(length))
    return  passowrd

print(generate_password(5))
print(generate_password(10))
print(generate_password(20))


# print(string.digits)
#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.punctuation)

#all_chars = string.ascii_letters + string.digits + string.punctuation
#print(all_chars)


print()
print("====================== Examples - Generating CSRF tokens, URL-safe tokens,and OTP Password  ======================")
print()

import secrets

print(secrets.token_hex(8))
print(secrets.token_hex(16))
print(secrets.token_hex(24))

print(secrets.token_urlsafe())
print(secrets.token_urlsafe(16))

# https://mywebsite.com/reset-passowrd?token=VQtPMxG-yI7D4cLoeOBFO1nmOSEwUSU8tyxju52Px04


def generate_otp_generate(length):
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range(length))
    return password

generate_otp_generate(6)
generate_otp_generate(4)
generate_otp_generate(10)

print()
print("====================== Generating Strong Password  ======================")
print()


#print(any(char.islower() for char in 'asdf2342'))
#print(any(char.isupper() for char in 'asdf2342'))
#print(any(char.isdigit() for char in 'asdf2342'))
#print(any(char in string.punctuation for char in 'asdf2342!?'))

#print(list(char.islower() for char in 'asdf2342'))
#print(list(char.isupper() for char in 'asdf2342'))
#print(list(char.isdigit() for char in 'asdf2342'))
#print(list(char in string.punctuation for char in 'asdf2342!?'))7

counter = 0 # counts how many times we try to generate password
def generate_password(length:int):
    global counter
    counter += 1
    all_chars = string.ascii_letters + string.digits + string.punctuation
    passowrd = ''.join(secrets.choice(all_chars) for _ in range(length))
    return  passowrd

def generate_special_password(length: int):
    while True:
        p = generate_password(length)
        if any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(c in string.punctuation for c in p):
            break
    return p

print(generate_special_password(4))
print(counter)