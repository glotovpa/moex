# Автор: Павел Глотов
# glotov_pa@mail.ru
# Получение информации инструментов через API ММВБ
# last_price_stock(code) - получение последней цены акции по её коду
# Пример - print(last_price_stock('SBER'))

import requests


def last_price_stock(code):
    url = "https://iss.moex.com/iss/engines/stock/markets/" \
          "shares/boards/TQBR/securities.csv?iss.meta=off&iss." \
          "only=marketdata&marketdata.columns=SECID,LAST"
    csv_text = requests.get(url).text.split('\n')
    for csv_line in csv_text:
        csv_tabl = csv_line.split(';')
        if csv_tabl[0] == code:
            return csv_tabl[1]
