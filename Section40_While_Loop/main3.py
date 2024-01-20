print()
print("Practice - Using break statements in While and For-In Loops" + "\n" +
      "==========================================================="
      )
print()

user_password = 'admin123'
password = ''

while password != user_password:
    print("Enter 'quit' in order to exit from login")
    password = input("Please enter your password: ")
    if password == 'quit':
        print("Quitting...")
        break

if password == user_password:
    print("Login sucessfull!")
else:
    print("Login failed")

print("**"*30)

my_list = [10, 5, 2, 100, 35]

for num in my_list:
    if num == 2:
        break
    print(num)