print()
print("Functions" + "\n" +
      "==========")
print()

a = 5
b = 3
c = a + b
print(c) # 8

a = 8
b = 12
c = a + b
print(c) # 20


# Same code blocks

def sum(a, b):
    c = a + b
    print(c)

print(type(sum))


a = 5
b = 3
sum(a, b) # 8

a = 8
b = 12
sum(a, b) # 20


def my_fn():
    pass

print(my_fn())

def my_fn(a, b):
    return a + b

print(my_fn(60, 45))


def my_fn(a, b):
    a += 1
    c = a + b
    return c
res = my_fn(10, 3)
print(res) # 13
