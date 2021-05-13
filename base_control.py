import sqlite3


# создание базы данных
def create_db():
    conn = sqlite3.connect('valutes.db')

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS valutes(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        date DATE,
        valute_id TEXT,
        num_code TEXT,
        char_code TEXT,
        nominal INTEGER ,
        valute_name TEXT,
        RUB FLOAT,
        UNIQUE(date, valute_id));""")

    conn.commit()
    print('База данных успешно создана.')


def delete_table_from_db():
    conn = sqlite3.connect('valutes.db')

    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS valutes;""")

    conn.commit()
    print('Таблица valutes удалена ')


# запросы в БД
def get_max():
    conn = sqlite3.connect('valutes.db')

    cursor = conn.cursor()
    cursor.execute("""SELECT RUB, valute_name, date "
                                  "FROM valutes "
                                  "WHERE RUB = (SELECT MAX(RUB) FROM valutes) ;""")
    max_results = cursor.fetchall()
    print('---')
    print('Максимальная валюта')
    print(f'Значение  валюты: {round(max_results[0][0], 1)} руб.\n'
          f'Название валюты: {max_results[0][1]}\n'
          f'Дата этого значения: {max_results[0][2]}')
    print('---')


def get_min():
    conn = sqlite3.connect('valutes.db')

    cursor = conn.cursor()
    cursor.execute("""SELECT RUB, valute_name, date "
                                  "FROM valutes "
                                  "WHERE RUB = (SELECT MIN(RUB) FROM valutes) ;""")
    min_results = cursor.fetchall()
    print('---')
    print('Минимальная валюта')
    print(f'Значение валюты: {round(min_results[0][0], 1)} руб.\n'
          f'Название валюты: {min_results[0][1]}\n'
          f'Дата этого значения: {min_results[0][2]}')
    print('---')


def get_average():
    conn = sqlite3.connect('valutes.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT avg(RUB) FROM valutes;""")
    avg_results = cursor.fetchall()
    print('---')
    print(f'Среднее значение перевода в рубли за весь период по всем валютам: {round(avg_results[0][0], 2)} руб.')
    print('---')
