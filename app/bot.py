from app.login import Login
from selenium import webdriver

class Bot():
    def __init__(self, driver: webdriver.Chrome):
        self.login: Login = Login(driver)
        self.driver: webdriver.Chrome = driver
        self.proxy: bool = None



    