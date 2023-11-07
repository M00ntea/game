import telebot
from random import randint

TOKEN = '6735447061:AAEUBI_Ulbf0hc47RxmF4J0Z1JVXk-YbFGM'

bot = telebot.TeleBot(TOKEN)

dialog_started = False


@bot.message_handler(commands=['start'])
def welcome(message):
    global dialog_started
    dialog_started = True
    bot.send_message(message.chat.id, '''Правила: Я загадываю число от 0 до 100. Вы должны угадать это число.
     Кол-во попыток - 8
     Если готовы, нажмите кнопку /startgame''')


@bot.message_handler(commands=['startgame'])
def start_game(message):
    if not dialog_started:
        bot.send_message(message.chat.id, 'Сначала начните игру с /start')
        return

    random_number = randint(1, 100)
    bot.send_message(message.chat.id, 'Введите число от 0 до 100')
    attempts = 8

    @bot.message_handler(func=lambda msg: msg.text.isdigit())
    def handle_guess(message):
        nonlocal attempts
        guess = int(message.text)

        if random_number == guess:
            bot.send_message(message.chat.id, "Вы угадали")
            attempts = 0
        elif guess > random_number:
            bot.send_message(message.chat.id, "Загаданное число меньше вашего")
        else:
            bot.send_message(message.chat.id, "Загаданное число больше вашего")

        attempts -= 1
        if attempts == 0:
            bot.send_message(message.chat.id, "Игра окончена. Загаданное число было: " + str(random_number))



bot.polling(none_stop=True)
