import sqlite3
print()
print("Creating an SQLite3 Database and Table" + "\n" +
      "===========================================")
print()

DB_NAME = 'slqite_db.db'

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """
        CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
        );
    """

    sqlite_conn.execute(sql_request)

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(type(sqlite_conn))