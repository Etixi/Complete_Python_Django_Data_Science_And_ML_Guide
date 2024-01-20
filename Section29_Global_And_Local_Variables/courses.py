# declaring "a" in the global scope and assigning the value 10
a = 10

def my_fn():
    # declaring "a" in the scope of function and assigning the value True
    a = True
    b = 15
    print(a)
    print(b)

my_fn()

print('a = ', a) # 10
# print(b) # name 'b' is not defined

# ======================================================= #

a = 5
def my_fn():
    def inner_fn():
        print(a) # 5
    inner_fn()

my_fn()

# ===================== Using Global Variable In the Function ===================== #

a = 10

def my_fn():
    global a
    a = 15

my_fn()
print('a = ', a)