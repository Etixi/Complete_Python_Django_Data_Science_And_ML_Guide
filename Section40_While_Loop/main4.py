print()
print("Practice - Using continue and break statements in While Loops" + "\n" +
      "=============================================================="
      )
print()

current_usernames = ['bogdan123', 'bob1', 'alice75']

while True:
    username = input("Please enter desired username: ")

    if username in current_usernames:
        print("Username is already taken. Try again")
        continue

    current_usernames.append(username)
    break

print("User registration complete.")
print(current_usernames)