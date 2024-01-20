print()
print("Practice - Tuples Manipulation" + "\n" +
      "=====================================")
print()

screen_res = (1920, 1080, 1080)
screen_res_1 = (1920, 1080)
screen_info = (True, 'Samsung', 150)

screen_data = screen_res_1 + screen_info
print(screen_data)
print(screen_data[0])
print(screen_data[-1])

print(screen_res)
print(screen_res.index(1080))
print(screen_res.count(1080))
print(type(screen_res))
print(isinstance(screen_res, tuple))

print(id(screen_res_1))
screen_res_list = list(screen_res_1)
screen_res_list[0] = 1444
print(screen_res_list)
screen_res = tuple(screen_res_list)
print(screen_res)
