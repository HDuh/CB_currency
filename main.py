import base_control as bc
from fill_db import parsing_data_and_fill_db

if __name__ == '__main__':
    # создание базы
    bc.create_db()

    # заполнение базы данными с сайта ЦБ
    parsing_data_and_fill_db()

