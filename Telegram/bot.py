import telebot
from config import TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def help_command(message: telebot.types.Message):
    text = ("Добро пожаловать в Currency Bot!\n"
            "Для конвертации введите команду в формате:\n"
            "<имя валюты> <в какую валюту перевести> <количество>\n"
            "Пример: USD RUB 100\n\n"
            "Список доступных валют: /values")
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values_command(message: telebot.types.Message):
    text = "Доступные валюты:\n- USD (Доллар)\n- EUR (Евро)\n- RUB (Рубль)"
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def convert_command(message: telebot.types.Message):
    try:
        data = message.text.split(" ")
        if len(data) != 3:
            raise APIException("Неверный формат команды. Используйте: <валюта> <в какую перевести> <количество>.")

        base, quote, amount = data
        total = CurrencyConverter.get_price(base, quote, amount)
        text = f"Цена {amount} {base.upper()} в {quote.upper()} = {total}"
        bot.reply_to(message, text)
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка: {e}")


bot.polling(none_stop=True)