import sqlite3


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Виконання SQL-запиту через cursor.execute(sql)
sql = "INSERT INTO Students (name, group_id) VALUES ('John Doe', 1)"
cursor.execute(sql)


conn.commit()


conn.close()
