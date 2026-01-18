from telebot.types import Message
from app.loader import bot
from app.keyboards.reply import main_menu_keyboard



@bot.message_handler(commands=["start"])
def cmd_start(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        "🎬 Привет!\n"
        "Я бот для поиска фильмов.\n\n"
        "Выберите действие с помощью кнопок ниже 👇",
        reply_markup=main_menu_keyboard()
    )
