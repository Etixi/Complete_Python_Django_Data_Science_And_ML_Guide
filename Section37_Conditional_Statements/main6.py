def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 60:
        return 'D'
    return 'F'


print(get_letter_grade(50))
print(get_letter_grade(70))