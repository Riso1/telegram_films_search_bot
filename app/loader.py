import telebot
from telebot.storage import StateMemoryStorage
from telebot import custom_filters

from app.config import BOT_TOKEN

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

# ВАЖНО: включаем поддержку состояний
bot.add_custom_filter(custom_filters.StateFilter(bot))
