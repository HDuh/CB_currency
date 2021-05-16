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
    try:
        conn = sqlite3.connect('valutes.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT RUB, valute_name, date "
                                      "FROM valutes "
                                      "WHERE RUB = (SELECT MAX(RUB) FROM valutes) ;""")
        max_results = cursor.fetchall()

        return (round(max_results[0][0], 1),
                max_results[0][1],
                max_results[0][2])
    except Exception as e:
        print(f'Ошибка функции get_max: {e.args}')
        return 'Opss, ошЫбка.'


def get_min():
    try:
        conn = sqlite3.connect('valutes.db')

        cursor = conn.cursor()
        cursor.execute("""SELECT RUB, valute_name, date "
                                      "FROM valutes "
                                      "WHERE RUB = (SELECT MIN(RUB) FROM valutes) ;""")
        min_results = cursor.fetchall()

        return (round(min_results[0][0], 1),
                min_results[0][1],
                min_results[0][2])
    except Exception as e:
        print(f'Ошибка функции get_min: {e.args}')
        return 'Opss, ошЫбка.'


def get_average():
    try:
        conn = sqlite3.connect('valutes.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT avg(RUB) FROM valutes;""")

        avg_results = cursor.fetchall()

        return round(avg_results[0][0], 2)

    except Exception as e:
        print(f'Ошибка функции get_average: {e.args}')
        return 'Opss, ошЫбка.'
