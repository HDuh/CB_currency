import requests


# запрос курса на указанный день на API ЦБ
def get_currency_on_date(date):
    payload = {'date_req': date}
    r = requests.get('https://www.cbr.ru/scripts/XML_daily_eng.asp', params=payload)

    currency_on_date = r.text

    return currency_on_date
