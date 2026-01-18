from telebot.handler_backends import State, StatesGroup


class MovieSearchState(StatesGroup):
    title = State()
