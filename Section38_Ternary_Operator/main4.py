print()
print("Example - Calculating School Grades using the Ternary Operator" + "\n" +
      "==========================================================")
print()

def get_letter_grade(score):
    letter_grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
    return letter_grade

print(get_letter_grade(95))
print(get_letter_grade(75))
print(get_letter_grade(60))
print(get_letter_grade(50))