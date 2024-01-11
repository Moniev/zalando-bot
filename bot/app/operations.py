from app.crud import CRUD
from app.utils import strToDatetime, calculateDateFromNow
from app.models import UpcomingDrop, OpenDrop
from datetime import datetime
from datetime import timedelta
import inspect
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.remote.webelement import WebElement


class Operations():
    def __init__(self, driver: webdriver.Chrome, crud: CRUD, drop_date: datetime):
        self.__cart: list[str] = []
        self.__cart_worth: int = 0
        self.__cash: float = 0
        self.__crud: CRUD = crud
        self.__driver: webdriver.Chrome = driver
        self.__drop_date: datetime = drop_date
        self.__hunted_items: list[str] = []
        self.__wait: WebDriverWait = lambda: WebDriverWait(self.driver, randint(14, 20))
        
    @property
    def drop_date(self):
        return self.__drop_date
    
    @drop_date.setter
    def drop_date(self, drop_date: datetime):
        self.__drop_date = drop_date

    @property
    def cart(self):
        return self.__cart
    
    @cart.setter
    def cart(self, cart: list[int]):
        self.__cart = cart

    @property
    def cart_worth(self):
        return self.__cart_worth

    @cart_worth.setter
    def cart_worth(self, cart_worth: float):
        self.__cart_worth = cart_worth

    @property
    def cash(self):
        return self.__cash
    
    @cash.setter
    def cash(self, value: float):
        self.__cash = value

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
    def hunted_items(self):
        return self.__hunted_items
    
    @hunted_items.setter
    def hunted_items(self, hunted_items: list[int]):
        self.__hunted_items = hunted_items

    @property
    def wait(self) -> WebDriverWait:
        return self.__wait()

    async def checkForAlreadyOpenDrops(self):
        func_name = inspect.stack()[0][3]
        print(func_name)
        self.driver.get("https://www.zalando-lounge.pl")
        if self.driver.current_url == "https://www.zalando-lounge.pl/event#":
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]')))
            
            website: WebElement  = self.driver.find_element(By.TAG_NAME, "html")
            website.send_keys(Keys.END)

            i : int = 1
            drops: list[WebElement] = self.driver.find_elements(By.XPATH, '//a[starts-with(@id, "open-ZZO2")]')
            
            for notification in drops:
                website_id: str = notification.get_attribute("id")[-7:]
                title: str = notification.find_element(By.XPATH, './/div[@id="image_wrappper"]/img').get_attribute("alt")
                time_left: str = notification.find_element(By.XPATH, './/div[@class="campaign-cardstyles__InnerWrapper-sc-1ye77dr-4 eRKwns"]/div/div/div/div/div[2]/div[1]/span[2]/span/span').text
                
                end_datetime: datetime = await calculateDateFromNow(time_left)
                drop: OpenDrop = OpenDrop(website_id=website_id, title=title, end_datetime=end_datetime)
                await self.crud.add(drop)

                print(i, website_id, end_datetime, title)
                i += 1
                
    async def checkForUpcomingDrops(self):
        func_name = inspect.stack()[0][3]
        print(func_name)
        self.driver.get("https://www.zalando-lounge.pl")
        if self.driver.current_url == "https://www.zalando-lounge.pl/event#":
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]')))
           
            website = self.driver.find_element(By.TAG_NAME, "html")
            website.send_keys(Keys.END)

            i : int = 1
            events: list[WebElement] = self.driver.find_elements(By.XPATH, '//div[starts-with(@id, "upcoming-ZZO2")]')
            
            for notification in events:
                website_id: str = notification.get_attribute("id")[-7:]
                title: str = notification.find_element(By.XPATH, './/div[@class="InfoWrapper-sc-5c8jzs bAKWAQ"]/div/button').get_attribute("aria-label")
                date: str = notification.find_element(By.XPATH, './/div[@class="InfoWrapper-sc-5c8jzs bAKWAQ"]/div/div/div/span[2]/span/span').text
                
                open_datetime: datetime = await calculateDateFromNow(date)
                drop: UpcomingDrop = UpcomingDrop(website_id=website_id, title=title, open_datetime=open_datetime)
                await self.crud.add(drop)

                print(i, website_id, date, title)
                i += 1

    async def getCartWorth(self) -> float:
        func_name = inspect.stack()[0][3]
        print(func_name)    
        if not await self.isCartEmpty() :
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
            cart_button.click()
            cart_worth: str = self.driver.find_element(By.XPATH, '//*[@class="Wrapper-sc-va3ki5 jDtuT"]/div/div/p[3]/span[2]').text[:-3].replace(",", '.')
            cart_worth: float = float(cart_worth)            
            cart_button.click()
            self.cart_worth = cart_worth
            return cart_worth
        
        self.cart_worth = 0
        return 0

    async def emptyCart(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)    
        if not await self.isCartEmpty() :
            cart_button: WebElement  = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
            cart_button.click()

            trash_buttons: list[WebElement] = self.driver.find_elements(By.XPATH, '//button[starts-with(@class, "RemoveItem-sc-")]')
            
            for button in trash_buttons:
                button.click()
            
            self.cart.clear()
            cart_button.click()

    async def addItemsToCart(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)
        start_cart_time = datetime.now()
        end_cart_time = start_cart_time + timedelta(minutes=20)
        
    async def setTimeOfDrop(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)
        pass

    async def isCartEmpty(self) -> bool:
        func_name = inspect.stack()[0][3]
        print(func_name)
        cart_button: WebElement  = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
        cart_button.click()
        items: list[WebElement] = self.driver.find_elements(By.XPATH, '//div[starts-with(@class, "CartItemWrapper-sc-1owbazd")]')
        cart_button.click()
        return len(items) == 0

    async def checkCart(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
        cart_button.click()
        items: list[WebElement] = self.driver.find_elements(By.XPATH, '//div[starts-with(@class, "CartItemWrapper-sc-1owbazd")]')

        for item in items:
            label: str = item.find_element(By.XPATH, './/div[@class="Header-sc-ki4en3 jrJqNb"]/a/span').text
            item_name: str = item.find_element(By.XPATH, './/a[@class="Content-sc-zw0qkw eWihNR"]/div/div[1]/span').text
            item_size: str = item.find_element(By.XPATH, './/a[@class="Content-sc-zw0qkw eWihNR"]/div/div[2]/span[2]').text
            item_price: str = item.find_element(By.XPATH, './/a[@class="Content-sc-zw0qkw eWihNR"]/div/div[4]/span[2]').text
            item_discount: str = item.find_element(By.XPATH, './/a[@class="Content-sc-zw0qkw eWihNR"]/div/div[3]/span').text
            item_picture: str = item.find_element(By.XPATH, './/a[@class="Content-sc-zw0qkw eWihNR"]/div/div[3]/span"]')
        
        cart_button.click()

    async def compareCarts(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)
        cart_button: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
        cart_button.click()
        items: list[WebElement] = self.driver.find_elements(By.XPATH, '//div[starts-with(@class "CartItemWrapper-sc-1owbazd ")]')
        cart_button.click()
        return len(self.cart) == len(items)
        
    async def cashout(self) -> None:
        func_name = inspect.stack()[0][3]
        print(func_name)
        if self.cash - self.cart_worth >= 0:
            cart_button: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]')))
            cart_button.click()
            cashout_button: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="Wrapper-sc-8so8sv cLunUE"]')))
            cashout_button.click()

            if self.driver.current_url == "https://www.zalando-lounge.pl/checkout/":
                cashout_button: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-container"]/div/div[2]/main/div/div/div[2]/div[6]/div[1]/button')))
                cashout_button.click()
    
    def __repr__(self):
        pass

    def __del__(self):
        pass