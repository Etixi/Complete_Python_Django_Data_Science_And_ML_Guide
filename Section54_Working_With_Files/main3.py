from pathlib import Path


print()
print("Reading and Writing Files " + "\n" +
      "=================================")
print()

# file_path = 'my_file.txt'
file_path = Path('my_file.txt')

# file = open(file_path, 'w')
# print(file)
# print(type(file))

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")


# file = open(file_path)
# print(file.read())

# with open(file_path) as file:
#     for line in file.readlines():
#         # print(line)
#         # print(type(line))
#         print(line.strip())

# with open(file_path) as file:
#     while True:
#         line = file.readlines()
#         if not line:
#            break
#         print(line.strip())

with open(file_path) as file:
    print(file.read())

with open(file_path, 'a') as file:
    file.write("Third line\n")

with open(file_path) as file:
    print(file.read())

if file_path.exists():
    file_path.unlink()