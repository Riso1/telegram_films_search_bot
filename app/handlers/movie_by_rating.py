from telebot.types import Message, CallbackQuery

from app.loader import bot
from app.api.tmdb_client import movies_by_rating
from app.keyboards.inline import rating_keyboard
from app.database.models import SearchHistory


@bot.message_handler(commands=["movie_by_rating"])
def cmd_movie_by_rating(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        "⭐ Выберите минимальный рейтинг:",
        reply_markup=rating_keyboard()
    )

@bot.message_handler(func=lambda m: m.text == "⭐ Фильмы по рейтингу")
def menu_movie_by_rating(message: Message) -> None:
    cmd_movie_by_rating(message)


@bot.callback_query_handler(func=lambda call: call.data.startswith("rating_"))
def callback_rating(call: CallbackQuery) -> None:
    rating = float(call.data.split("_")[1])
    chat_id = call.message.chat.id

    movies = movies_by_rating(rating, limit=5)

    if not movies:
        bot.edit_message_text(
            "❌ Фильмы с таким рейтингом не найдены.",
            chat_id=chat_id,
            message_id=call.message.message_id
        )
        return

    # сохраняем историю
    SearchHistory.create(
        user_id=str(call.from_user.id),
        command="/movie_by_rating",
        query=f"rating >= {rating}"
    )

    lines = [f"🎬 Фильмы с рейтингом от {rating}:\n"]

    for movie in movies:
        title = movie.get("title")
        year = movie.get("release_date", "—")[:4]
        vote = movie.get("vote_average", "—")

        lines.append(
            f"• {title} ({year})\n"
            f"  ⭐ Рейтинг: {vote}\n"
        )

    bot.edit_message_text(
        "\n".join(lines),
        chat_id=chat_id,
        message_id=call.message.message_id
    )
