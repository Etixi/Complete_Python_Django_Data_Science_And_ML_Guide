print()
print("Example - Constructing Dictionaries from Sequences" + "\n" +
      "========================================"
      )
print()

grades = (80, 95, 65)
subjects = ['Science', 'Math', 'Physics']

print(dict(zip(grades, subjects)))

grade_dict = {subject: grade - 10 for subject, grade in zip(subjects, grades)}
print(grade_dict)