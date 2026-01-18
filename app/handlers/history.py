from telebot.types import Message

from app.loader import bot
from app.database.models import SearchHistory


@bot.message_handler(commands=["history"])
def cmd_history(message: Message) -> None:
    records = (
        SearchHistory
        .select()
        .where(SearchHistory.user_id == str(message.from_user.id))
        .order_by(SearchHistory.created_at.desc())
        .limit(10)
    )

    if not records:
        bot.send_message(
            message.chat.id,
            "📭 История запросов пуста."
        )
        return

    lines = ["🕘 Ваша история запросов:\n"]

    for record in records:
        lines.append(
            f"• {record.created_at:%d.%m.%Y %H:%M}\n"
            f"  {record.command} — {record.query}\n"
        )

    bot.send_message(message.chat.id, "\n".join(lines))

@bot.message_handler(func=lambda m: m.text == "🕘 История")
def menu_history(message: Message) -> None:
    cmd_history(message)

