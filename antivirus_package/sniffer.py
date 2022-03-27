import sqlite3
with sqlite3.connect("C:\\PycharmProjects\\Antivirus\\database_package\\customs_officers.db") as con:
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM `customs_officers_users`;
        """)
    print(cur.fetchall())



