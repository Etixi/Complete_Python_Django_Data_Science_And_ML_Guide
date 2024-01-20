print()
print("Practice - Iterating Through Ranges,Strings,and Sets with For-In-Loops" + "\n" +
      "=====================================================================")
print()

name = 'Jennifer'

for char in name:
    print(char)

print("*"*10)
for i in range(10, -1, -1):
    print(i)
print("Rocket launch!")


print("*"*10)
genres = {'Romance', 'Fantasy', 'Mystery', 'Science Fiction'}

for genre in genres:
    print(f"My favorite genre is {genre}")