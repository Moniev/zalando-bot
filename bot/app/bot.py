from app.crud import CRUD
from app.login import Login
from app.operations import Operations 
from selenium import webdriver

class Bot():
    
    def __init__(self, driver: webdriver.Chrome):
        self.crud: CRUD = CRUD()
        self.proxies: list[str] = []
        self.login: Login = Login(crud=self.crud, driver=driver)    
        self.driver: webdriver.Chrome = driver
        self.operations: Operations | None = Operations(self.driver, self.crud) if self.login.is_logged_in else None

    async def __aenter__(self):
        await self.login.loginUser()

    async def scrapProxies(self):
        pass

    async def testConnection(self, proxy_ip_port: str):
        pass

    async def __aexit__(self, *args):
        await self.login.logoutUser()
        await self.driver.quit()