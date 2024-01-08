# Create few files in the my_test_directory after first code run
import os

print()
print("Working with Files and Directories using the os Module " + "\n" +
      "======================================================")
print()

directory_path = 'my_test_directory'

if not os.path.exists(directory_path):
    # Create a directory
    os.mkdir(directory_path)
    print("Directory was created: ", directory_path)
else:
    print("Directory exists: ", directory_path)

# Creating path to the file
file_path = os.path.join(directory_path, 'my_file.txt')
print("File path: ", file_path)

# Getting parent directory
parent_dir = os.path.dirname(file_path)
print("Parent directory: ", parent_dir)

# Checking if the file is file path or dir path
is_file = os.path.isfile(file_path)
is_dir = os.path.isdir(directory_path)
print(f"{file_path} is file: ", is_file)
print(f"{directory_path} is directory: ", is_dir)

# Listing files in the directory
dir_files = os.listdir(directory_path)
print(f"Files in the directory {directory_path}: ")
for file in dir_files:
    print(file)


print()
print("Removing Files and Directories using the os Module " + "\n" +
      "======================================================")
print()

# Remove directory
if os.path.exists(directory_path):
    dir_files = os.listdir(directory_path)
    for file in dir_files:
        os.remove(os.path.join(directory_path, file))
    os.rmdir(directory_path)
    print(f"Directory {directory_path} was removed")

print()
print("Summary of Directory and File Operations using the os Module " + "\n" +
      "==============================================================")
print()

