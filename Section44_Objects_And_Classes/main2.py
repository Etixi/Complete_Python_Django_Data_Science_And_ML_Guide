print()
print("Practice - Adding Instance Attributes through Dot Notation" + "\n" +
      "==============================================================")
print()
class User:
    def info(self):
        # print(dir(self))
        # print(self.__dict__)
        print(f"User {self.username} has email {self.email}")
    # def info(self, username, email):
        # print(f"User {username} has email {email}")


first_user = User()
first_user.username = 'etienne123'
first_user.email = 'etienne@gmail.com'
first_user.info()

# print(first_user.__dict__)
# first_user.info('bogdan123', 'bogdan@gmail.com')
