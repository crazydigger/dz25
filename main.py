import psycopg2
import  pandas as pd
your_database_name="postgres"
your_username="postgres"
your_password="password"
# Подключение к базе данных
conn = psycopg2.connect(
    dbname=your_database_name,
    user=your_username,
    password=your_password,
    host="localhost",
    port="5432"
)

# Создание курсора
cur = conn.cursor()

# Создание таблицы apartments
cur.execute('''
    CREATE TABLE IF NOT EXISTS apartments (
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        district VARCHAR(100),
        address VARCHAR(255),
        area NUMERIC,
        rooms INT,
        floor INT,
        year_built INT,
        price NUMERIC,
        type VARCHAR(50)
    )
''')

# Заполнение таблицы 10 строками данных
apartments_data = [
    ('Москва', 'Центральный', 'ул. Тверская, д. 1', 50.0, 2, 5, 2020, 8000000, 'новостройка'),
    ('Санкт-Петербург', 'Невский', 'Невский пр., д. 10', 70.0, 3, 3, 2018, 6500000, 'вторичное жильё'),
    ('Казань', 'Центр', 'ул. Баумана, д. 5', 40.0, 1, 4, 2015, 3000000, 'вторичное жильё'),
    ('Екатеринбург', 'Центральный', 'ул. Малышева, д. 10', 60.0, 2, 6, 2019, 4500000, 'новостройка'),
    ('Нижний Новгород', 'Центральный', 'ул. Большая Покровская, д. 15', 55.0, 3, 2, 2021, 5000000, 'новостройка'),
    ('Челябинск', 'Центральный', 'ул. Кировоградская, д. 20', 80.0, 4, 7, 2017, 4000000, 'вторичное жильё'),
    ('Ростов-на-Дону', 'Центральный', 'ул. Буденовская, д. 25', 45.0, 2, 3, 2016, 3500000, 'вторичное жильё'),
    ('Уфа', 'Центральный', 'ул. Ленина, д. 30', 90.0, 4, 8, 2014, 5500000, 'вторичное жильё'),
    ('Волгоград', 'Центральный', 'ул. Красноармейская, д. 12', 65.0, 3, 4, 2013, 4200000, 'вторичное жильё'),
    ('Самара', 'Центральный', 'ул. Гагарина, д. 50', 75.0, 3, 5, 2022, 7000000, 'новостройка')
]

# Вставка данных в таблицу
cur.executemany('''
    INSERT INTO apartments (city, district, address, area, rooms, floor, year_built, price, type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''', apartments_data)

# Сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()
# Создание подключения к базе данных через SQLAlchemy
conn = psycopg2.connect("host='{}' port='{}' dbname='{}' user='{}' password={}".format('localhost', 5432, your_database_name, your_username, your_password))



# Выполнение SQL-запроса и получение данных в виде DataFrame
query = "SELECT * FROM apartments WHERE price < 5000000"
df = pd.read_sql(query, conn)

# Вывод полученных данных
print(df)