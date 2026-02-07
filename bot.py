from config import TG_TOKEN
import telebot
from telebot.types import Message
from data_base import DataBase


db = DataBase()
bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start(message:Message):
    bot.send_message(chat_id=message.chat.id, text='привет я твой бот')
    db.add_user(chat_id=message.chat.id, username=message.from_user.username)
bot.polling()