import asyncio
from asyncio import AbstractEventLoop
from app import botLoop
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from time import sleep


scheduler: BackgroundScheduler = BackgroundScheduler()

def run() -> None:
    try:
        loop: AbstractEventLoop = asyncio.get_event_loop() 
    except RuntimeError as runtime_error:
        if str(runtime_error).startswith('There is no current event loop in thread'):
            loop: AbstractEventLoop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        else:
            raise RuntimeError

    loop.run_until_complete(botLoop())

def setExecutionDate(year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
    trigger: CronTrigger = CronTrigger(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    scheduler.add_job(run, trigger=trigger)
    try:
        while True:
            sleep(0)
    except:
        scheduler.shutdown()

def executeNow() -> None:
    trigger: CronTrigger = CronTrigger(second=1)
    scheduler.add_job(run, trigger)
    scheduler.start()
    try:
        while True:
            sleep(0)
    except:
        scheduler.shutdown()


if __name__ == "__main__":
    executeNow()
