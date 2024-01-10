from app.settings import DATABASE_URL, manifest_json, background_js
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool
from selenium_stealth import stealth
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from webdriver_manager.chrome import ChromeDriverManager
import zipfile

def createDriver(proxy: bool = False, already_open: bool = False) -> webdriver.Chrome:
    options: Options = Options()
    operating_systems: list[OperatingSystem] = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    software_names: list[SoftwareName] = [SoftwareName.CHROME.value]
    user_agent_rotator: UserAgent = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    
    if proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)
    
    if not already_open:
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
        options.add_argument("--ignore-certificate-errors")
    else:
        options.add_argument("--remote-debugging-port=9222")
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver: webdriver.Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_position(0, 0) 
    driver.maximize_window()
    
    if not already_open:
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent_rotator.get_random_user_agent()})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    if not already_open:
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
def makeAsyncConnection() -> AsyncEngine | None:
    try: 
        db = create_async_engine(
            url=DATABASE_URL,
            echo=True,
            poolclass=NullPool
        )
        return db
    except:
        return 

connection: AsyncEngine = makeAsyncConnection()

'''ASYNC POSTGRES SESSION OBJECT'''
def asyncSessionLoader() -> async_sessionmaker[AsyncSession]:
    session: AsyncSession = async_sessionmaker(
        bind=connection,
        expire_on_commit=False
    )
    return session

'''ASYNC POSTGRES INITIALIZATION'''
async def createDatabase() -> None:
    connection: AsyncEngine = makeAsyncConnection()
    async with connection.begin() as _connection:
        from app.models import Cart, CreditCard, Item, Login, Logout, Operation, OpenDrop, UpcomingDrop, User
        await _connection.run_sync(Base.metadata.drop_all)
        await _connection.run_sync(Base.metadata.create_all)
    await connection.dispose()

async def run(bots: int = 1, proxies: bool = False) -> None:
    from app.bot import Bot
    await createDatabase()
    driver = createDriver()
    bot = Bot(driver=driver)
    if bot.operations is not None:
        await bot.operations.getCartWorth()
        await bot.operations.emptyCart()
        await bot.operations.checkForAlreadyOpenDrops()

    