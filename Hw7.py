import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS products (  
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    product_title TEXT NOT NULL,  
                    price REAL NOT NULL DEFAULT 0.0,  
                    quantity INTEGER NOT NULL DEFAULT 0  
                )''')

conn.commit()
conn.close()


def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ('Жидкое мыло с запахом ванили', 150.0, 10),
        ('Мыло детское', 80.5, 5),
        ('Шампунь для сухих волос', 200.0, 8),
        ('Крем для лица', 300.0, 12),
        ('Зубная паста', 50.0, 15),
        ('Мыло для рук', 70.0, 20),
        ('Кондиционер для волос', 180.0, 7),
        ('Дезодорант', 100.0, 10),
        ('Гель для душа', 120.0, 10),
        ('Крем для рук', 70.0, 15),
        ('Мыло для тела', 90.0, 12),
        ('Шампунь для жирных волос', 180.0, 8),
        ('Крем для ног', 80.0, 10),
        ('Гель для волос', 70.0, 10),
        ('Лосьон для тела', 150.0, 15)
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()

def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def select_products_by_limit(limit_price, limit_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (limit_price, limit_quantity))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

def search_products_by_title(title):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + title + '%',))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


add_products()
update_quantity(1, 20)
update_price(2, 90.0)
delete_product(3)
select_all_products()
select_products_by_limit(100.0, 5)
search_products_by_title('мыло')