import time
from app import createDriver
from app.bot import Bot

bot = Bot(createDriver())

if __name__ == "__main__":
    bot.login.loginUser()
    bot.login.logoutUser()

