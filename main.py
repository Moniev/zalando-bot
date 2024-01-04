import time
from app import createDriver
from app.bot import Bot

driver = createDriver(proxy=False)
bot = Bot(driver=driver)

if __name__ == "__main__":
    if bot.operations is not None:
        bot.operations.checkForUpcomingDrops() 
    bot.login.logoutUser()
    time.sleep(5)
    bot.driver.quit()
