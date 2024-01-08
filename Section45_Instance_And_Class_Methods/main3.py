print()
print("Practice - Working With Classes Attributes" + "\n" +
      "===========================================")
print()




class User:
    users_qty = 0
    def __init__(self, username, email):

        self.username = username
        self.email = email
        User.users_qty += 1

first_user = User('bob234', 'bob@bob.com')
second_user = User('alice356', 'alice@alice.com')
third_user = User('john324', 'john@john.com')


print(first_user.__dict__)
print(second_user.__dict__)
print(third_user.__dict__)
# print(third_user.users_qty)
print(User.__dict__)


third_user.users_qty = 10
print(User.users_qty) # 3
print(third_user.users_qty) # 10



