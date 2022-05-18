import sqlite3

with sqlite3.connect("../dependencies/database_dir/customs_users.db") as conn:
    cur = conn.cursor()
    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS `customs_users` (
    #         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         Имя TEXT,
    #         Фамилия TEXT,
    #         Отчество TEXT,
    #         email TEXT,
    #         пароль TEXT);""")

    # cur.execute("""
    #     INSERT INTO
    #         `customs_users` (user_id, Имя, Фамилия, Отчество, email, пароль)
    #     VALUES (NULL, "Антон", "Макеев", "Николаевич", "antonmakeev18@gmail.com", "12345");
    # """)
    res = cur.execute("""
    SELECT * FROM `customs_users`
    """).fetchall()
    print(res)
    conn.commit()


