from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time


class Operations():
    def __init__(self, driver: webdriver.Chrome):
        self.__driver: webdriver.Chrome = driver
        self.__cash: float = 0
        self.__hunted_items: list = []
        self.cart: list = []

    @property
    def driver(self):
        return self.__driver
    
    @driver.setter
    def driver(self, driver: webdriver.Chrome):
        self.__driver = driver

    @property
    def cash(self):
        return self.__cash
    
    @cash.setter
    def cash(self, value: float):
        self.__cash = value

    def findGivenDrop(self):
        pass

    def setHuntedItems(self):
        pass

    def checkForAlreadyOpenDrops(self):
        self.driver.get("https://www.zalando-lounge.pl/#/")

    def checkForUpcomingDrops(self):
        self.driver.get("https://www.zalando-lounge.pl/#/")
        WebDriverWait(self.driver, randint(10, 14)).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="main"]/div[4]')))
        grid = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'upcoming-')]")
        for notification in grid:
            print(notification)

    def checkForItems(self):
        pass

    def addItemsToCart(self):
        pass

    def setTimeOfDrop(self):
        pass

    def cashout(self):
        pass