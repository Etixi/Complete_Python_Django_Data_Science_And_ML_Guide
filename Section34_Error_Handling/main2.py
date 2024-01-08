try:
    file = open("files/file.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("File is ready for reading")
finally:
    if file and not file.closed:
        file.close()
        print("File was closed.")
        print(file.closed)