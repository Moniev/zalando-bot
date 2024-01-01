import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from random import randint
from app import driver


class Login():
    def __init__(self):
        self.is_logged_in: bool = False
        self.__try: int = 0

    def loginUser(self):
        self.__try += 1
        driver.get("https://www.zalando-lounge.pl/#/")

        WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//span[@id="topbar-cta-btn"]'))).click()

        WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button'))).click()

        WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]'))).send_keys('m0ni3v@gmail.com')
        WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]'))).send_keys('1488Monieev!')

        WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button'))).click()

        potential_error = WebDriverWait(driver, randint(1, 14)).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[1]/div/div')))
        time.sleep(3)

        if potential_error is not None and driver.current_url != "https://www.zalando-lounge.pl/event#":
            driver.back()
            WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-form"]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button'))).click()
            WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-email"]'))).send_keys('m0ni3v@gmail.com')
            WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-password"]'))).send_keys('1488Monieev!')
            WebDriverWait(driver, randint(1, 14)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root-content"]/div/div[2]/div[2]/div[2]/div/div/div/form/button'))).click()
        else:
            self.is_logged_in = True
        if not self.is_logged_in and self.__try < 5:
            time.sleep(1)
            self.loginUser()

    def logoutUser(self):
        self.is_logged_in = False