from array import array

print()
print("Saving Arrays to Files and Reading Arrays from Files" + "\n" +
      "====================================================")
print()

my_int_array = array('i', [10, 4, 3, 7, 9, 15])

with open('my_array.bin', 'wb') as file:
    my_int_array.tofile(file)


imported_array = array('i')
with open('my_array.bin', 'rb') as file:
    imported_array.fromfile(file, 6)
    print(imported_array)

