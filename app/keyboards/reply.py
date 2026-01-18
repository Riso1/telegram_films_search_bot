from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )

    buttons = [
        KeyboardButton("🎬 Поиск фильма"),
        KeyboardButton("⭐ Фильмы по рейтингу"),
        KeyboardButton("🕘 История"),
        KeyboardButton("ℹ️ Помощь"),
    ]

    keyboard.add(*buttons)
    return keyboard
