from app.loader import bot
from app.database.db import db
from app.database.models import SearchHistory

import app.handlers.start
import app.handlers.help
import app.handlers.movie_search
import app.handlers.movie_by_rating
import app.handlers.history  # добавим ниже


def init_db():
    db.connect()
    db.create_tables([SearchHistory], safe=True)
    db.close()


if __name__ == "__main__":
    init_db()
    bot.infinity_polling(skip_pending=True)
