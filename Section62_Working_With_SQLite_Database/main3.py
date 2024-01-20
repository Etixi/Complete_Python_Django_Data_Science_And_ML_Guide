import sqlite3

print()
print("Reading Data into the SQLite Table" + "\n" +
      "===========================================")
print()

DB_NAME = 'slqite_db.db'

# Read records
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """
        SELECT * FROM courses WHERE reviews_qty > 30
    """
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #    print(record)

    courses = sql_cursor.fetchall()
    print(courses)