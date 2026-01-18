from telebot.types import Message
from app.loader import bot


@bot.message_handler(commands=["help"])
def cmd_help(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        "📋 Доступные команды:\n\n"
        "/start — запуск бота\n"
        "/help — справка\n"
        "/movie_search — поиск фильма по названию\n"
        "/movie_by_rating — поиск фильмов по рейтингу\n"
        "/history — история ваших запросов\n\n"
        "Также вы можете пользоваться кнопками меню 👇"
    )


@bot.message_handler(func=lambda m: m.text == "ℹ️ Помощь")
def menu_help(message: Message) -> None:
    cmd_help(message)
