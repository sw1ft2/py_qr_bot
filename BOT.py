import telebot as tg
from telebot import types
import qrcode
import time
import random


token = ''
bot = tg.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Таймер')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)
    bot.send_message(message.chat.id, "Вот это встреча!")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    chatId = message.chat.id
    text = message.text
    text1 = "Подождите:"
    print(text)
    if text:
        if text in name:
            bot.send_message(chatId, random.choice(pril))
        elif text == "Таймер":
            bot.send_message(chatId, "Таймер 10 секунд запущен")
            time.sleep(10)
            bot.send_message(chatId, "Время вышло")
        else:
            img = qrcode.make(text)
            img.save('Photo.png')
            p = open('Photo.png', 'rb')
            bot.send_message(chatId,text1)
            bot.send_message(chatId, text)
            bot.send_photo(chatId, p)

@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'Photo' + message.photo[1].file_id
    with open(src + '.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Фото добавлено")

if __name__ == '__main__':
    bot.infinity_polling()
