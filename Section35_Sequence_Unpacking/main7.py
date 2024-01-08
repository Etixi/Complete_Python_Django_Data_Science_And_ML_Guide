print()
print("Practice - Flexibility in Function Calls" + "\n" +
      "==========================================")
print()


def create_user(username, email, password):
    # Creating user...
    return {'username': username, 'email':email, 'password':password}

user_details = {
    'username': 'bogdan-123',
    'email': 'bogdan@gmail.com',
    'password':'bogdan1341513'
}

created_user = create_user(**user_details)
print(created_user)

user_other_details = ['alice-462', 'alice@alice.com','alice235423']
other_created_user = create_user(*user_other_details)
print(other_created_user)