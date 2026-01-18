from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def rating_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    ratings = [6, 7, 8, 9]

    buttons = [
        InlineKeyboardButton(
            text=f"⭐ {rating}+",
            callback_data=f"rating_{rating}"
        )
        for rating in ratings
    ]

    keyboard.add(*buttons)
    return keyboard
