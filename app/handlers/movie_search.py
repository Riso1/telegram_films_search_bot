from telebot.types import Message

from app.loader import bot
from app.states.movie_states import MovieSearchState
from app.api.tmdb_client import search_movie
from app.database.models import SearchHistory


@bot.message_handler(commands=["movie_search"])
def cmd_movie_search(message: Message) -> None:
    bot.set_state(
        message.from_user.id,
        MovieSearchState.title,
        message.chat.id
    )
    bot.send_message(
        message.chat.id,
        "🎬 Введите название фильма:"
    )

@bot.message_handler(func=lambda m: m.text == "🎬 Поиск фильма")
def menu_movie_search(message: Message) -> None:
    cmd_movie_search(message)


@bot.message_handler(state=MovieSearchState.title)
def get_movie_title(message: Message) -> None:
    title = message.text.strip()

    movies = search_movie(title, limit=5)

    if not movies:
        bot.send_message(
            message.chat.id,
            "❌ Фильмы не найдены. Попробуйте другое название."
        )
        return

    lines = ["🎬 Найденные фильмы:\n"]

    for movie in movies:
        name = movie.get("title")
        year = movie.get("release_date", "—")[:4]
        rating = movie.get("vote_average", "—")

        lines.append(
            f"• {name} ({year})\n"
            f"  ⭐ Рейтинг: {rating}\n"
        )

    bot.send_message(message.chat.id, "\n".join(lines))

    # сохраняем историю
    SearchHistory.create(
        user_id=str(message.from_user.id),
        command="/movie_search",
        query=title
    )

    bot.delete_state(message.from_user.id, message.chat.id)
