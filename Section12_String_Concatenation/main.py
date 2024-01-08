my_name_concat = 'Etienne'
my_hobby_concat = 'running'
time_concat = 8

print("============== Practice - Concatening Strings using the + Operator =========")
info_concat = my_name_concat + ' likes ' + my_hobby_concat + ' at ' + str(time_concat) + " o'clock"
print(info_concat)


print("============== Practice-Using f-strings for String Formatting ==============")
my_name = 'Etienne'
my_hobby = 'running'
time = 8 # [1, 2)

# info_format = f"{my_name} likes {my_hobby} at {str(time)} o'clock"
info_format = f"{my_name} likes {my_hobby} at {time} o'clock"
print(info_format)

print("============== Practice- Alternative String Formatting Methods ==============")
info = "{} likes {} at {} o'oclok".format(my_name, my_hobby, time)
print(info)

info = "%s likes %s at %s o'oclok" % (my_name, my_hobby, time)
print(info)