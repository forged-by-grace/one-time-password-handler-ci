import asyncio
from core.event.consume_event import create_otp_event


async def main():
   await asyncio.gather(create_otp_event())

asyncio.run(main=main())