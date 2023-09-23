# -*- coding: utf-8 -*-
# Конвертер


import requests
import json
from Keys import converter_key


class Convert_:

    def __init__(self):
        print("init")


    fromc = input("Enter from currency: ")
    to = input("Enter to currency: ")
    amount = input("Enter amount currency: ")
    url = f"https://api.apilayer.com/fixer/convert?to={to}&from={fromc}&amount={amount}"


    def validate_names(self):  # Проверка
        if len(fromc) or len(to) != 3:
            print("Неверный формат, попробуйте снова")
        else:
            return "ok"


    @classmethod
    def convert(self):
        payload = {}
        headers = {
            "apikey": converter_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text
        json_data = json.loads(result)
        print("result:", json_data["result"])
