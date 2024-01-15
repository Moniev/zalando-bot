import datetime
import random, string, inspect
from functools import wraps

async def calculateDateFromNow(date: str) -> datetime.datetime | None:
    if 'd' in date and 'h' in date and 'm' in date:
        date: datetime.datetime = datetime.datetime.strptime(date, '%dd %Hh %Mm')
        return datetime.datetime.now() + datetime.timedelta(days=date.day, hours=date.hour, minutes=date.minute)

    if not 'd' in date and 'h' in date and 's' in date:
        date: datetime.datetime = datetime.datetime.strptime(date, '%Hh %Mm %Ss')
        return datetime.datetime.now() + datetime.timedelta(hours=date.hour, minutes=date.minute, seconds=date.second)
    
    if not 'd' in date and not 'h' in date and not 'm' in date:
        return 

async def strToDatetime(date: str) -> datetime.datetime | None:
    if 'd' in date and 'h' in date and 'm' in date:
        date: datetime.datetime = datetime.datetime.strptime(date, '%dd %Hh %Mm')
        return date

    if not 'd' in date and 'h' in date and 's' in date:
        date: datetime.datetime = datetime.datetime.strptime(date, '%Hh %Mm %Ss')
        return date
    
    if not 'd' in date and not 'h' in date and not 'm' in date:
        return 

def generateRandomString(n: int) -> str:
    random_string = ''.join(random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(n))
    return random_string

def registerOperation(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start: datetime.datetime = datetime.datetime.now()
        
        result = func(*args, **kwargs)
        
        end: datetime.datetime = datetime.datetime.now()
        return result
    return wrapper
