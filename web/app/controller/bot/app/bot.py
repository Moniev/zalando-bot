from .crud import CRUD
from .login import Login
from .operations import Operations 
from selenium import webdriver

class Bot():
    
    def __init__(self, driver: webdriver.Chrome, id: int):
        self.__id: int = id 
        self.crud: CRUD = CRUD(id=self.id)
        self.driver: webdriver.Chrome = driver
        self.proxies: list[str] = []
        self.login: Login = Login(crud=self.crud, driver=self.driver, id=self.id)   
        self.operations: Operations | None = Operations(driver=self.driver, crud=self.crud, drop_date=None, id=self.id) if self.login.is_logged_in else None

    @property
    def id(self):
        return self.__id

    def __enter__(self):
        return self

    async def __aenter__(self): 
        return self

    async def scrapProxies(self):
        pass

    async def testConnection(self, proxy_ip_port: str):
        pass

    async def __aexit__(self, *args):
        return self
