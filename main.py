
from faker import Faker
import sqlite3

fake = Faker()

# Підключення до бази даних
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Заповнення таблиці студентів
for _ in range(30):  # 30 студентів
    name = fake.name()
    group_id = fake.random_int(min=1, max=3)  # випадкова група від 1 до 3
    cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (name, group_id))

# Збереження змін до бази даних
conn.commit()

# Закриття з'єднання з базою даних
conn.close()

