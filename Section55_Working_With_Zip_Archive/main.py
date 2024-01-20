from zipfile import ZipFile
from pathlib import Path

print("********************************************************")
print(
        "Built-In ZipFile Module And Creating Zip Archives" + "\n"
        "================================================="
)
print("********************************************************")


files_dir = Path('../Section55_Working_With_Zip_Archive/files')
if not files_dir.exists():
    files_dir.mkdir()

with open('files/first.txt', 'w') as file:
    file.write("This is first file\n")

with open('files/second.txt', 'w') as file:
    file.write('This is second file\n')




print("********************************************************")
print(
        "Reading From Zip Archives" + "\n"
        "================================================="
)
print("********************************************************")

zip_archive = Path('my-files.zip')
if zip_archive.exists():
    zip_archive.unlink()

with ZipFile('my-files.zip', mode='w') as zip_file:
    for file in files_dir.iterdir():
        print(file)
        zip_file.write(file)

with ZipFile('my-files.zip') as zip_file:
    # print(zip_file)
    # print(type(zip_file))
    # print(zip_file.compression)
    # print(zip_file.infolist())
    # zip_file.extractall('unzipped-my-files')
    zip_file.extract('../Section55_Working_With_Zip_Archive/files/first.txt', 'individual-files')