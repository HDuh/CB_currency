import base_control as bc
from fill_db import parsing_data_and_fill_db

if __name__ == '__main__':
    # создание базы
    bc.create_db()

    # заполнение базы данными с сайта ЦБ
    parsing_data_and_fill_db()

# import os
# from flask_script import Manager
#
# from app import create_app
#
# app = create_app()
# app.config.from_object(os.environ['APP_SETTINGS'])
# manager = Manager(app)
#
# if __name__ == '__main__':
#     manager.run()