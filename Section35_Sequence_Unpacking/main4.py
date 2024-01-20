print()
print("Practice - Unpacking Selected Elements" + "\n" +
      "========================================")
print()

comment = ("This is a great course", 'bob_202', 120, 4.7)

_, username, _, course_rating = comment
print(username)
print(course_rating)