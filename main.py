import time
from app.login import Login
from app import driver

_login = Login()

if __name__ == "__main__":
    _login.loginUser()
    time.sleep(120)
    driver.quit()

