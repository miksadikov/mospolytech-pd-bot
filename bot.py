import telebot
from telebot import types

api_token = '2106821702:AAFnPifXBorrsVmJxGJ0m7ySTRlZ_mOArBo'

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    #if message.from_user.username == None:
    #  username = '!'
    #else:
    #  username = ', ' + message.from_user.username + '!'
    #message_text = f'Привет! \{username} \
    message_text = f'Привет! \
    \n\nЯ супербот центра проектной деятельности МосПолитеха!) \
    \n\n(Внимание, бот находится на стадии разработки!)\n\
    \nСтудентом какого курса ты являешься?'

    # открываем разметку для Keyboard кнопок, указываем кол-во кнопок в строке через row_width
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Первого')
    btn2 = types.KeyboardButton('Второго и старше')
    # и добавляем их к нашей разметке
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)

# это функция обрабатывающая все текстовые сообщения от пользователя
@bot.message_handler(content_types=['text'])
def mess(message):
    # полученную от пользователя строку (str) мы переводим в нижний регистр и убираем лишние пробелы
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "первого":
      # создаем разметку с типом клавиш inline, по одной клавише в строке и add добавляем клавиши на разметку markup
      markup = types.InlineKeyboardMarkup(row_width=1)
      markup.add(types.InlineKeyboardButton("Ссылка на страницу, посвященную ПД", url="https://study.mospolytech.ru/design", callback_data='0'),
                 types.InlineKeyboardButton("Календарь групповых сессий", callback_data='1'),
                 #types.InlineKeyboardButton("Порядок начисления баллов", callback_data='2'),
                 types.InlineKeyboardButton("Ссылка на страницу ПД ВКонтакте", url="https://vk.com/mpoly_project", callback_data='2'),
                 types.InlineKeyboardButton("Пройти опрос о ПД", callback_data='3'))
      bot.send_message(message.chat.id, f'Возможно, эта информация будет тебе полезна:', reply_markup=markup)

    if get_message_bot == "второго и старше":
      # создаем разметку с типом клавиш inline, по одной клавише в строке и add добавляем клавиши на разметку markup
      markup = types.InlineKeyboardMarkup(row_width=1)
      markup.add(types.InlineKeyboardButton("Ссылка на страницу, посвященную ПД", url="https://fit.mospolytech.ru/about/pd", callback_data='4'),
                 types.InlineKeyboardButton("График и этапы работы", callback_data='5'),
                 types.InlineKeyboardButton("Отчётность", callback_data='6'),
                 types.InlineKeyboardButton("Порядок начисления баллов", callback_data='7'),
                 types.InlineKeyboardButton("Проекты предыдущих лет", callback_data='8'))
      bot.send_message(message.chat.id, f'Возможно, эта информация будет тебе полезна:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
      answer = 'Начало: 26 Сентября 2022\n \
Презентация сфер дизайна\n\n \
ЭТАП 1: Эмпатия\n \
03 Октября 2022\n \
Организация работы групп\n\n \
ЭТАП 2: Фокусировка\n \
31 Октября 2022\n \
Планирование полевых испытаний\n \
21 ноября 2022\n \
Формулирование проблемных ситуаций\n\n \
ЭТАП 3-4: Идеация\n \
05 Декабря 2022\n \
Анализ идей и путей решения выявленых проблем\n\n \
ЭТАП 5: Прототипирование\n \
Декабрь 2022\n \
Прототипирование идей и инсайтов по IX сферам\n\n \
Завершение:\n \
Январь 2023\n \
Подведение итогов и оценка проектных групп'
      
      markup = types.InlineKeyboardMarkup(row_width=1)
      markup.add(types.InlineKeyboardButton("Ссылка на страницу, посвященную ПД", url="https://study.mospolytech.ru/design", callback_data='0'),
                 types.InlineKeyboardButton("Календарь групповых сессий", callback_data='1'),
                 #types.InlineKeyboardButton("Порядок начисления баллов", callback_data='2'),
                 types.InlineKeyboardButton("Ссылка на страницу ПД ВКонтакте", url="https://vk.com/mpoly_project", callback_data='2'),
                 types.InlineKeyboardButton("Пройти опрос о ПД", callback_data='3'))
      bot.send_message(call.message.chat.id, answer, reply_markup=markup)

    elif call.data == '3':
      options=['Доводилась ли до вас информация о сроках промежуточной аттестации по проектной деятельности?', \
      'Доводилась ли до вас информация о сроках итоговой защиты проекта?', \
      'Достаточно ли было информации для выбора проекта (направления проекта)?', \
      'Хотели бы вы ознакомиться с примерами проектов прошлых лет?', \
      'Знаете ли вы, где можно посмотреть примеры проектов прошлых лет?', \
      'Нужна ли вам дополнительная организационная/информационная поддержка в проектной деятельности?']
      bot.send_poll(call.message.chat.id, "Можно выбрать любое количество ответов \
                   (если поставить галочку - ответ ДА, если не ставить - ответ НЕТ):", \
                   options, is_anonymous = False, allows_multiple_answers = True)


    elif call.data == '5':
      answer = '14–23 сентября: Публикация списка проектов\n \
14–27 сентября: Предварительная запись на проекты\n \
24–30 сентября: РОП распределяет незаписавшихся студентов по проектам\n \
28–04 октября: Собеседования и отбор, формирование индивидуальных планов работы\n \
до 11 октября: Дополнительное распределение по проектам\n \
08–11 ноября: Рубежный контроль № 1\n \
13–15 декабря: Рубежный контроль № 2\n \
10–17 января: Допуск к защите\n \
17–29 января: Защита проектов'

      markup = types.InlineKeyboardMarkup(row_width=1)
      markup.add(types.InlineKeyboardButton("Ссылка на страницу, посвященную ПД", url="https://fit.mospolytech.ru/about/pd", callback_data='4'),
                 types.InlineKeyboardButton("График и этапы работы", callback_data='5'),
                 types.InlineKeyboardButton("Отчётность", callback_data='6'),
                 types.InlineKeyboardButton("Порядок начисления баллов", callback_data='7'),
                 types.InlineKeyboardButton("Проекты предыдущих лет", callback_data='8'))
      bot.send_message(call.message.chat.id, answer, reply_markup=markup)

    elif call.data == '6':
      answer = 'Комплект отчётных материалов\n \
1. Отчёт\n \
2. Сайт проекта (лендинг)\n \
3. Git-репозиторий\n \
4. Видеопрезентация\n \
5. Промо видео\n \
6. Презентация в формате PDF\n \
7. Постер\n \
8. Пост в социальных сетях о проекте'

      markup = types.InlineKeyboardMarkup(row_width=1)
      markup.add(types.InlineKeyboardButton("Ссылка на страницу, посвященную ПД", url="https://fit.mospolytech.ru/about/pd", callback_data='4'),
                 types.InlineKeyboardButton("График и этапы работы", callback_data='5'),
                 types.InlineKeyboardButton("Отчётность", callback_data='6'),
                 types.InlineKeyboardButton("Порядок начисления баллов", callback_data='7'),
                 types.InlineKeyboardButton("Проекты предыдущих лет", callback_data='8'))
      bot.send_message(call.message.chat.id, answer, reply_markup=markup)

@bot.poll_answer_handler(func=lambda call: True)
def handle_poll_answer(call):
  #print(call)
  print(f'{call.option_ids}, {call.user.id}')


bot.infinity_polling(timeout=10, long_polling_timeout = 5)
