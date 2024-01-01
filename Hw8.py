import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)''')

conn.commit()
conn.close()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO countries (title) VALUES ('Россия')")
cursor.execute("INSERT INTO countries (title) VALUES ('США')")
cursor.execute("INSERT INTO countries (title) VALUES ('Франция')")

conn.commit()
conn.close()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, 
                  area REAL DEFAULT 0, country_id INTEGER,
                  FOREIGN KEY (country_id) REFERENCES countries(id))''')

conn.commit()
conn.close()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Москва', 2561.4, 1)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Нью-Йорк', 783.8, 2)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Париж', 105.4, 3)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Лондон', 1572, 4)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Токио', 2190, 5)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 16411.56, 6)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Сидней', 2058.9, 7)")

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE students
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, 
                  last_name TEXT NOT NULL, city_id INTEGER,
                  FOREIGN KEY (city_id) REFERENCES cities(id))''')

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алексей', 'Сидоров', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Елена', 'Смирнова', 4)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Анна', 'Козлова', 5)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Дмитрий', 'Морозов', 6)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Ольга', 'Новикова', 7)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Максим', 'Павлов', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алина', 'Федорова', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Никита', 'Соколов', 4)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Екатерина', 'Волкова', 5)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Ирина', 'Медведева', 6)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Артем', 'Лебедев', 7)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Виктория', 'Андреева', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Сергей', 'Степанов', 2)")

conn.commit()
conn.close()

import sqlite3

def display_students_by_city_id(city_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                      FROM students
                      JOIN cities ON students.city_id = cities.id
                      JOIN countries ON cities.country_id = countries.id
                      WHERE cities.id = ?''', (city_id,))

    students = cursor.fetchall()

    if len(students) > 0:
        for student in students:
            first_name, last_name, country, city, area = student
            print("Имя: {}, Фамилия: {}, Страна: {}, Город: {}, Площадь города: {}".format(first_name, last_name, country, city, area))
    else:
        print("Нет учеников в данном городе.")

    conn.close()

def main():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(city[0], city[1])

    conn.close()

    while True:
        city_id = int(input("Введите id города: "))
        if city_id == 0:
            break
        display_students_by_city_id(city_id)

if __name__ == "__main__":
    main()
