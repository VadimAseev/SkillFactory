import requests
import json


class APIException(Exception):
    """Класс для обработки пользовательских ошибок."""
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> float:
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException("Количество должно быть положительным числом.")
        except ValueError:
            raise APIException("Количество должно быть числом.")

        base = base.lower()
        quote = quote.lower()
        if base == quote:
            raise APIException("Нельзя конвертировать валюту саму в себя.")

        available_currencies = {"usd": "USD", "eur": "EUR", "rub": "RUB"}
        if base not in available_currencies or quote not in available_currencies:
            raise APIException("Указана недоступная валюта.")

        try:
            url = f"https://api.exchangerate.host/latest?base={available_currencies[base]}"
            response = requests.get(url)
            rates = json.loads(response.text)["rates"]
        except Exception as e:
            raise APIException(f"Ошибка при запросе курса валют: {e}")

        if available_currencies[quote] not in rates:
            raise APIException("Указана недоступная валюта.")

        rate = rates[available_currencies[quote]]
        return round(rate * amount, 2)