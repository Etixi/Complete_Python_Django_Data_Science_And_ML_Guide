print()
print("Practice - Incorporating Own Instance Attributes with the __init__ Method" + "\n" +
      "==========================================================================")
print()

class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")



first_user = User('etienne123', 'etienne@gmail.com')
print(first_user.username)
print(first_user.email)
first_user.info()

other_user = User('alice3245', 'alice@alice.com')
other_user.info()
print(other_user.username)
print(other_user.email)
print(other_user.__dict__)

other_user.username = 'a6245'
print(other_user.username)



