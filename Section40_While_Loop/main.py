import time

print()
print("Pratice - Utilizing the While loop" + "\n" +
      "==========================================================="
      )
print()

username = ''

while not username or any(char.isdigit() for char in username) or len(username) < 3:
    entered_username = input("Please enter your username (must be more than 3 characters and contain only alphabetical characters): ")
    if entered_username.isalpha() and len(entered_username) >= 3:
        username = entered_username
    else:
        print("Username is too short or contains digits. Please use only alphabetical characters.")

print(f"Welcome, {username}")



seconds_qty = 5
while seconds_qty > 0:
    print(f"Timer: {seconds_qty} second remaining...")
    seconds_qty -= 1
    time.sleep(1)

print("Timer is up!")
