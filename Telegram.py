import telebot  # Импортируем модуль, который позволяет работать с телеграмм
from telebot import types
import random
token = '6591048150:AAECf92SVTqBhxwadcDQrHsEOqfvUE6M3J4' # токен телеграмм бота
bot = telebot.TeleBot(token) # считывает токен бота

'Команды '
# Список идентификаторов стикеров
sticker_ids = [
    'CAACAgIAAxkBAAEB7uJlUOk1aRmQCgLgvcMLVmXUvIJnlAACoAADlp-MDmce7YYzVgABVTME',
    'CAACAgIAAxkBAAEB7uRlUOlWriErrHBhLOu1sUlKwqdR1QACwi4AAuJUIUtpSs4e3PowOTME',
    'CAACAgIAAxkBAAEB7uZlUOmA7_4w3E2TNye1uRkg-axSyAACuw0AAuYAASFL9-t-HOXBDy8zBA',
    # Добавьте еще идентификаторы стикеров по вашему выбору
]


@bot.message_handler(content_types='sticker')
def handle_sticker(message):
        random_sticker_id = random.choice(sticker_ids)
        bot.send_sticker(message.chat.id, random_sticker_id)


'Создание кнопок'
@bot.message_handler(commands=['help'])   # выполнение команды "help"
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)   # создание объекта кнопки. ReplyKeyboardMarkup - кнопки внизу панели
                                            # InlineKeyboardMarkup - кнопки в текстовом сообщении
    inf = types.KeyboardButton('Данные о пользователе')
    start = types.KeyboardButton('/start')  # Создание кнопки, по нажатию которой отправляет "/start"
    markup.add(start, inf)                       # добавляем все кнопки в переменную markup
    bot.send_message(message.chat.id,'Команды для бота', reply_markup=markup)  # отправляем пользователю кнопки




@bot.message_handler(commands=['Website'])
def info(message):
    n1 = types.InlineKeyboardMarkup()
    n2 = types.InlineKeyboardButton('Сайт для посещения', url='https://translate.yandex.ru/?source_lang=ru&target_lang=en&text=биография')
    n1.add(n2)
    bot.send_message(message.chat.id,'Посетите сайт', reply_markup=n1)








@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    photo = 'https://yandex.ru/images/search?img_url=https%3A%2F%2Fstorage.googleapis.com%2Freplit%2Fimages%2F1644407457731_e7b92fa05b89d3ad7393da6fb5d666f5.jpeg&lr=10725&pos=8&rpt=simage&source=serp&text=картинка%20python'
    bot.send_photo(message.chat.id, photo=photo, caption='Логотип питона')
    bot.send_message(message.chat.id, 'Крутое фото!', parse_mode='html')

@bot.message_handler(commands=['dog'])
def handle_start(message):
    user_id = message.from_user.id
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки для выбора животных
    cat_button = types.InlineKeyboardButton("Кот", callback_data="cat")
    dog_button = types.InlineKeyboardButton("Собака", callback_data="dog")
    lion_button = types.InlineKeyboardButton("Лев", callback_data="lion")

    # Добавляем кнопки в разметку
    markup.add(cat_button, dog_button, lion_button)

    # Отправляем сообщение с кнопками
    bot.send_message(user_id, "Выбери животное:", reply_markup=markup)


# Обработчик обратных вызовов
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    animal = call.data

    # Ответы для каждого животного
    responses = {
        "cat": "Коты мягкие и пушистые животные.",
        "dog": "Собаки верные друзья человека.",
        "lion": "Львы - короли джунглей."
    }

    response = responses.get(animal, "Я не знаю такого животного.")

    # Отправляем ответ пользователю
    bot.send_message(user_id, response)



user_choice = {}
game_options = ['Камень', 'Ножницы', 'Бумага']

@bot.message_handler(commands=['game'])
def start_game(message):
    bot.send_message(message.chat.id, 'Привет! давай сыграем в игру камень,ножницы, бумага. Выбери свой вариант. ')

    # Варианты ответа пользователя (кнопки)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stone = telebot.types.KeyboardButton('Камень')
    paper = telebot.types.KeyboardButton('Бумага')
    snip = telebot.types.KeyboardButton('Ножницы')
    keyboard.add((stone, paper, snip))

    bot.send_message(message.chat.id, 'Выберите вариант ответа', reply_markup=keyboard)

    # Обработчик обратных вызовов
@bot.message_handler(func=lambda message: True)
def handler(message):
    user_choice = message.text
    bot_choice = random.choice(game_options)
    if user_choice in game_options:
        win = winner(user_choice,bot_choice)

        result_message = f'Пользователь выбрал {user_choice}, Бот выбрал {bot_choice} \n'
        result_message += f'{win}'
        bot.send_message(message.chat.id, result_message)

def winner (user_choice,bot_choice):
    if user_choice == bot_choice:
        return 'Ничья'
    elif (
            (user_choice == 'Камень' and bot_choice == 'Ножницы') or
            (user_choice == 'Ножницы' and bot_choice == 'Бумага') or
            (user_choice == 'Бумага' and bot_choice == 'Камень')
    ):
        return 'Ты победил'
    else:
        return 'Бот победил'



@bot.message_handler(content_types=['text'])  # content_types позволяет боту реагировать на определенный тип данных
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'{message.from_user.id}', parse_mode='html')
    elif message.text == 'Данные о пользователе':
        bot.send_message(message.chat.id, f'{message.from_user}', parse_mode='html')
    elif message.text == 'Фото':
        photo= 'https://yandex.ru/images/search?img_url=https%3A%2F%2Fstorage.googleapis.com%2Freplit%2Fimages%2F1644407457731_e7b92fa05b89d3ad7393da6fb5d666f5.jpeg&lr=10725&pos=8&rpt=simage&source=serp&text=картинка%20python'
        bot.send_photo(message.chat.id,photo)   # send_photo отправляет картинку пользователю
    elif message.text == 'Отправь документ':
        doc = open('DOC1.docx','rb')  # open открывает документ и готовит к отправке
        bot.send_document(message.chat.id,doc, caption='Важнейший файл') # send_document отправляет документ пользователю
    elif message.text == 'Ответь на вопрос':
        n_1 = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton('2', callback_data='2')
        button_2 = types.InlineKeyboardButton('4', callback_data='4')
        button_3 = types.InlineKeyboardButton('5', callback_data='5')
        n_1.add(button_1,button_2,button_3)
        bot.send_message(message.chat.id, '2+2=', reply_markup=n_1)


    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')
@bot.message_handler(commands=['game'])
def start_game(message):
    bot.send_message(message.chat.id, 'Привет! давай сыграем в игру камень,ножницы, бумага. Выбери свой вариант. ')


# Запускаем бота
bot.polling()



'Основной цикл программы'
bot.polling(none_stop=True)    # () Ожидает новый сообщений пока не остановим вручную.
                                     # none_stop=True - перезапускается в случае ошибки
                                     # (interval=<seconds>) - Обновляет информацию каждые seconds секунд.



'''1.	Жирный текст: <b>текст</b> Пример: <b>Привет, мир!</b>
2.	Курсивный текст: <i>текст</i> Пример: <i>Привет, мир!</i>
3.	Подчеркнутый текст: <u>текст</u> Пример: <u>Привет, мир!</u>
4.	Зачеркнутый текст: <s>текст</s> Пример: <s>Привет, мир!</s>
5.	Моноширинный текст: <code>текст</code> Пример: <code>Привет, мир!</code>
6.	Ссылки: <a href="ссылка">текст</a> Пример: 
<a href="https://example.com">Перейти на example.com</a>
7.	Разделительная линия: <hr> Пример: <hr>'''


