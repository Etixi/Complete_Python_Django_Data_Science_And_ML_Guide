print("================ Practice - Integers Manipulation =================")

# my_num = 1000
# other_num = 100

my_num = 1_000_000_000_000
other_num = 1_000

res = my_num + other_num
print(res)

input_String = input("Enter any number: ")
print(type(input_String))

try :
    input_num = int(input_String)
    print(type(input_num))
except ValueError:
    print("Not able to convert int")


print("================== Practice - Floating-Point Numbers Manipulation =================")

averate_rating = 4.85
print(type(averate_rating))
print(averate_rating.is_integer())
print(round(averate_rating))  # 5
print(int(averate_rating))    # 4
print(float(100))             # 100.0

print("====================== Working with Complex Numbers =======================")
complex_a = 3 + 5j
complex_b = 4 + 7j

sum = complex_a + complex_b

print(sum)
print(type(sum))