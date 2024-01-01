
from app.settings import USER_MAIL, PASSWORD
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

class Login():
    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver.Chrome = driver
        self.__is_logged_in: bool = False
        self.__try: int = 0

    def loginUser(self):
        self.__try += 1
        self.driver.get("https://www.zalando-lounge.pl/#/")

        WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//span[@id="topbar-cta-btn"]'))).click()
        WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button'))).click()
        WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]'))).send_keys('m0ni3v@gmail.com')
        WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]'))).send_keys('1488Monieev!')
        WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button'))).click()

        potential_error = WebDriverWait(self.driver, randint(1, 14)).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[1]/div/div')))
        time.sleep(3)

        if potential_error is not None and self.driver.current_url != "https://www.zalando-lounge.pl/event#":
            self.driver.back()
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button'))).click()
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]'))).send_keys(USER_MAIL)
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]'))).send_keys(PASSWORD)
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button'))).click()
        else:
            self.__is_logged_in = True
        if not self.__is_logged_in and self.__try < 5:
            time.sleep(1)
            self.loginUser()

    def logoutUser(self):
        if self.__is_logged_in:
            self.driver.get("https://www.zalando-lounge.pl/#/")
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="nav-to-myaccount"]'))).click()
            WebDriverWait(self.driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//span[@id="myaccount-menu-link-logout"]'))).click()
            self.__is_logged_in = False
            self.__try = 0

    