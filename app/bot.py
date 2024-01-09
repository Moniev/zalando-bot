from app.login import Login
from app.buy import Operations 
from selenium import webdriver

class Bot():
    def __init__(self, driver: webdriver.Chrome):
        self.proxies: list[str] = []
        self.login: Login = Login(driver)
        self.login.loginUser()
        self.driver: webdriver.Chrome = driver
        self.operations: Operations | None = Operations(self.driver) if self.login.is_logged_in else None

    def scrapProxies(self):
        pass

    def testConnection(self, proxy_ip_port: str):
        pass

    def __del__(self):
        self.login.logoutUser()
        self.driver.quit()