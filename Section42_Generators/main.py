from sys import getsizeof

print()
print("Practice - Generators and Iteration over the Generator" + "\n" +
      "======================================================")
print()

squares_gen = (num * num for num in range(1_000_000_000))

for num in squares_gen:
    print(num)
    if num == 100:
        break

print("START SECOND ITERATION")

for num in squares_gen:
    print(num)
    if num == 225:
        break

my_list = [1, 5, 10]

for num in my_list:
    print(num)


print("SECOND")

for num in my_list:
    print(num)

# print(getsizeof(squares_gen))
# print(type(squares_gen))

#squares_list = [num * num for num in range(1_000_000_000)]
#print(getsizeof(squares_list))
#print(type(squares_list))