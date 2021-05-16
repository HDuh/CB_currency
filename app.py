import sqlite3
import time
from flask import Flask, flash, redirect, render_template, \
    request, url_for
import base_control as bc
from base_control import create_db
from fill_db import parsing_data_and_fill_db as pars_data

app = Flask(__name__)
app.config.from_pyfile('config.py')
create_db()


def get_db_connection():
    conn = sqlite3.connect('valutes.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download')
def download():
    print('Скачивание началось!')
    pars_data()
    return redirect('/results')


@app.route('/results')
def results():
    flash('Вышрузка закончена')
    conn = get_db_connection()
    valutes = conn.execute('SELECT * FROM valutes').fetchall()
    max_val = bc.get_max()
    min_val = bc.get_min()
    avg_val = bc.get_average()
    conn.close()
    return render_template('results.html',
                           valutes=valutes, max_val=max_val,
                           min_val=min_val, avg_val=avg_val)


if __name__ == '__main__':
    app.run()
