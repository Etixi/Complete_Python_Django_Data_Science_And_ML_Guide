print()
print("Practice - Unpacking Tuples" + "\n" +
      "===========================")
print()

color = (225, 128, 10)

red, green, blue = color

print(red)
print(green)
print(blue)

red = 200
blue = 20

color = (red, green, blue)
print(color)

employee_info = ("Jane Doe", 32, "Junior Developer")

employee_name, employee_age, employee_position = employee_info

# employee_name = employee_info[0]
# employee_age = employee_info[1]
# employee_position = employee_info[2]

print(employee_name, employee_age, employee_position)