from datetime import date, timedelta
import xml.etree.ElementTree as ET

import sqlite3

import download_currency


# делаем запрос на API ЦБ и парсим XML
def parsing_data_and_fill_db():
    # сегодняшний день
    today_date = date.today()

    # предыдущие 90 дней
    temp_date = today_date - timedelta(days=89)

    # Подключаемся к базе данных:
    conn = sqlite3.connect('valutes.db')
    cursor = conn.cursor()

    for date_i in range(90):
        try:
            temp_date_str = temp_date.strftime("%d.%m.%Y")
            currency_data = download_currency.get_currency_on_date(temp_date_str)
            temp_date += timedelta(days=1)

            root = ET.fromstring(currency_data)

            curr_day = root.attrib['Date']

            # for name, value in root.iter('Name', 'Value'):

            # 0 NumCode
            # 1 CharCode
            # 2 Nominal
            # 3 Name
            # 4 Value

            for i, elem in enumerate(root):
                # id валюты
                valute_id = elem.attrib['ID']

                # записываем данные в DataBase
                num_code = root[i][0].text
                char_code = root[i][1].text
                nominal = int(root[i][2].text)
                name = root[i][3].text
                RUB = root[i][4].text
                RUB = float(RUB.replace(',', '.'))
                try:
                    date_to_db = (None, curr_day, valute_id, num_code, char_code, nominal, name, RUB)

                    cursor.execute("""INSERT  INTO valutes VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", date_to_db)

                    print(f'Данные за {curr_day} успешно загружы в DataBase')
                    conn.commit()
                except Exception as e:
                    print(f'Exception on DB fill {e.args}')


        except Exception as e:
            print(f'{e.args}')
