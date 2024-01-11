import asyncio
from asyncio import AbstractEventLoop
from app import run

def setExecutionDate():
    pass

if __name__ == "__main__":
    loop: AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(run())
