import math

print("========================= Built-in Math Module ==========================")
print(math.e)
print(math.pi)

print(math.sqrt(225))
print(math.sqrt(230.5))

print(math.factorial(10)) # 1 * 2 * 3 ..... * 10

print(math.log10(100))
print(math.log10(1000))
print(math.log2(8))

print(math.floor(10.7))
print(round(10.7))

print()
print("========================= Recursive Functions ==========================")
print()

def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num == 1:
        return 1
    return num * calc_factorial(num - 1)


print(calc_factorial(100))
# print(calc_factorial('abc'))

print(math.factorial(100)) # 10 * 9 * 8 * ... * 1