from app.settings import DATABASE_URL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from selenium_stealth import stealth
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from typing import Union
from webdriver_manager.chrome import ChromeDriverManager

def scrapProxy() -> list[str]:
    pass


def createDriver(proxy: bool = False) -> webdriver.Chrome:
    options=Options()
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    
    proxy_ip_port = '20.219.235.172:3129'

    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    if proxy:
        options.add_argument(f"--proxy-server={proxy_ip_port}")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_position(0,0) 
    driver.maximize_window()
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent_rotator.get_random_user_agent()})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    return driver

class Base(DeclarativeBase):
    pass

'''REQUESTS FOR A CONNECTION TO DATABASE'''
def makeAsyncConnection() -> Union[AsyncEngine, bool]:
    try: 
        db = create_async_engine(
            url=DATABASE_URL,
            echo=True,
            poolclass=NullPool
        )
        return db
    except:
        return False

connection = makeAsyncConnection()

'''ASYNC POSTGRES INITIALIZATION'''
async def createDatabase() -> None:
    connection = makeAsyncConnection()
    async with connection.begin() as _connection:
        # from app.models import
        await _connection.run_sync(Base.metadata.drop_all)
        await _connection.run_sync(Base.metadata.create_all)
    await connection.dispose()

'''ASYNC POSTGRES SESSION OBJECT'''
def asyncSessionLoader() -> async_sessionmaker[AsyncSession]:
    session = async_sessionmaker(
        bind=connection,
        expire_on_commit=False
    )
    return session


def run():
    pass