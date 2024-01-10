import datetime, random, string, inspect
from app.crud import CRUD
from app.models import Operation

def register(func):
    async def decorator(*args, **kwargs):        
        await func(*args, **kwargs)
        new_operation = Operation(user_id =1, operation_name=func.__name__, success=True)
        await CRUD.add(new_operation)
    decorator.__name__ = func.__name__
    func_signature = inspect.signature(func)
    decorator.__signature__ = func_signature.replace(parameters=tuple(func_signature.parameters.values())[1:])
    return decorator

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

