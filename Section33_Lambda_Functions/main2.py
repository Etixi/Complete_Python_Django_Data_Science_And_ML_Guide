print()
print("Practice - Sorting a List using Lambda Functions" + "\n" +
      "========================================================")
print()

students = [

    {'name': 'John', 'score':50},
    {'name': 'Alice', 'score':20},
    {'name': 'Bob', 'score':90}
]

# def sorted_by_score(student):
#    return student['score']

# students.sort(key=sorted_by_score)
students.sort(key=lambda student : student['score'])
print(students)