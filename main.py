from settings import *
from api.telegram_bot import SendIPTelegramBot


if __name__ == "__main__":
    bot = SendIPTelegramBot(token, authorized_users, known_commands)
    bot.run()
