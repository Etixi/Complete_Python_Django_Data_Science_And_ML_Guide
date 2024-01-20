import sqlite3

print()
print("Writing Data into the SQLite Table" + "\n" +
      "===========================================")
print()

DB_NAME = 'slqite_db.db'

courses = [
    (456,"JS course", 235, 50),
    (234, "Java course", 452, 20),
    (567, "Node.js course", 753, 70)
]

# Write multiple records on the table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """
        INSERT INTO courses VALUES(?, ?, ?, ?)
    """
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()


# Insert one record on the table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """
#         INSERT INTO courses VALUES(?, ?, ?, ?)
#     """
#     sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
#     sqlite_conn.commit()

