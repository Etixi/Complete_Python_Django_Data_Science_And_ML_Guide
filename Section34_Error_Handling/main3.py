try:
    file = open("files/file.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("File is ready for reading")
finally:
    # print(locals())
    # print(globals())
    #print('file' in globals())
    if 'file' in globals() and  file and not file.closed:
        file.close()
        print("File was closed.")
        print(file.closed)