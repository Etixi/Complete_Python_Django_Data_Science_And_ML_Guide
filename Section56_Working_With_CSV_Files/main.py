import csv
print("************************************")
print(
        "Working With CSV Files" + "\n"
        "==============================="
)
print("************************************")



# Writing to CSV
csv_file_path = '../Section56_Working_With_CSV_Files/files/test.csv'

data_to_write = [
    {'user_id': 5423, 'user_name': 'etienne', 'comments_qty': 1300},
    {'user_id': 5425, 'user_name': 'alice', 'comments_qty': 830},
    {'user_id': 7245, 'user_name': 'bob', 'comments_qty': 970}
]

fieldnames = ['user_id', 'user_name', 'comments_qty']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

    # Write header
    writer.writeheader()

    # Write data
    writer.writerows(data_to_write)


print("************************************")
print(
        "Iterating Over Each Row In The CSV File" + "\n"
        "==============================="
)
print("************************************")
# Reading from CSV
with open(csv_file_path, newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    for index, row in enumerate(reader):
        print(index, row)
        for key, value in row.items():
            print(f"{key}: {value}")
