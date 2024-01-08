print("===================== Practice - Working With Boolean Values ========================")

db_is_available = False
print(db_is_available)
print(type(db_is_available))
print(isinstance(db_is_available, bool))

print("=="*30)
db_is_available = True
print(db_is_available)

print("=="*30)
print(bool(10))    # True
print(bool(0))     # False
print(bool(0.0))   # False
print(bool('abc')) # True
print(bool(''))    # False

print("=="*30)
print(100 > 50)
print(100 == 50)
print([1, 2, 3] == [1, 2, 3, 4])
print([1, 2, 3] == [1, 2, 3])

print("=="*30)
is_available = True
print(not  is_available)

my_name = 'Etienne'

print(is_available and my_name)

if( is_available and my_name):
    print("Is available")


print("========================== Type Conversion ===========================")
a = 5 + int('10')
print(a)

int_num = 5
float_num = 4.5

print(int_num + float_num) # 9.5
print(int_num.__add__(float_num)) # NotImplemented
print(float_num.__radd__(int_num)) # 9.5

bool_val = True
int_val = 7
print(bool_val + int_val) # 8
