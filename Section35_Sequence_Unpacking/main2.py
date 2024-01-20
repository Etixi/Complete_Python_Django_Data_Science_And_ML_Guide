print()
print("Practice - Unpacking a List of Tuples" + "\n" +
      "========================================")
print()


user_credentials = [
    ("user1", "password_one"),
    ("user2", "password_two"),
    ("user3", "password_three")
]

user1, user2, user3 = user_credentials

print(user1)
print(user2)
print(user3)

user1_username, user1_password = user1
user2_username, user2_password = user2
user3_username, user3_password = user3

print(user1_username, user1_password)
print(user2_username, user2_password)
print(user3_username, user3_password)
