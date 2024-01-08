print()
print("Practice - Global and Local Variables" + "\n" +
      "=============================================")
print()

c = True
def mult(a, b):
    c = a * b
    print(dir())
    return c

print(mult(100, 45))
print(c)