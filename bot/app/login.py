
from app.crud import CRUD
from app.models import Login, Logout as _Login, Logout
from app.settings import USER_MAIL, PASSWORD
from datetime import datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time


class Login():
    def __init__(self, crud: CRUD, driver: webdriver.Chrome, id: int=1):
        self.__id: int = id
        self.__crud: CRUD = crud
        self.__driver: webdriver.Chrome = driver
        self.__is_logged_in: bool = False
        self.__tries: int = 0
        self.__wait: WebDriverWait = lambda : WebDriverWait(self.driver, randint(9, 64))

    @property
    def crud(self):
        return self.__crud

    @property
    def driver(self):
        return self.__driver
    
    @driver.setter
    def driver(self, driver: webdriver.Chrome):
        self.__driver = driver

    @property
    def id(self):
        return self.__id

    @property
    def is_logged_in(self):
        return self.__is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, value: bool):
        self.__is_logged_in = value

    @property
    def tries(self):
        return self.__tries

    @tries.setter
    def tries(self, value: int):
        self.__tries = value

    @property
    def wait(self) -> WebDriverWait:
        return self.__wait()

    async def loginUser(self) -> None:
        self.tries += 1

        if self.driver.current_url != "https://www.zalando-lounge.pl/event#":
            self.driver.get("https://www.zalando-lounge.pl/#/")
        if self.is_logged_in is not True and self.driver.current_url != "https://www.zalando-lounge.pl/event#":
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@id="topbar-cta-btn"]')))
            login_button.click()
            second_login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button')))
            second_login_button.click()

            email = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]')))
            password = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]')))

            email.send_keys(USER_MAIL)
            password.send_keys(PASSWORD)
            
            time.sleep(randint(2, 5))

            continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button')))
            continue_button.click()
            
        if self.driver.current_url != "https://www.zalando-lounge.pl/event#":
            potential_error = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[1]/div/div')))
            time.sleep(randint(5, 7))

        if self.driver.current_url != "https://www.zalando-lounge.pl/event#" and potential_error is not None:
            self.driver.back()
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button')))
            login_button.click()

            email = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]')))
            password = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]')))

            email.send_keys(USER_MAIL)
            password.send_keys(PASSWORD)

            time.sleep(randint(2, 5))

            continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button')))
            continue_button.click()
        else:
            self.is_logged_in = True
            
            login: _Login = _Login(user_id=self.id, date_time=datetime.now())
            self.crud.add(login)

        if not self.is_logged_in and self.tries < 5:
            time.sleep(randint(4, 5))
            await self.loginUser()
            return
        if not self.is_logged_in and self.tries > 5:
            self.driver.quit()
            return
            
    async def logoutUser(self) -> None:
        if self.is_logged_in:
            self.driver.get("https://www.zalando-lounge.pl/#/")
            account_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="nav-to-myaccount"]')))
            account_button.click()

            logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@id="myaccount-menu-link-logout"]')))
            logout_button.click()
            
            logout: Logout = Logout(user_id=self.id, date_time=datetime.now())
            self.crud.add(logout)
            
            self.is_logged_in = False
            self.tries = 0
            return
    
    