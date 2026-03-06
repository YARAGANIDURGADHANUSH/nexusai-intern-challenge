
import asyncio
import random
import time

async def fetch_crm(phone):
    await asyncio.sleep(random.uniform(0.2,0.4))
    return {"vip": True}

async def fetch_billing(phone):
    await asyncio.sleep(random.uniform(0.15,0.35))
    return {"status":"paid"}

async def fetch_tickets(phone):
    await asyncio.sleep(random.uniform(0.1,0.3))
    return {"complaints":["internet slow","billing issue"]}

async def fetch_parallel(phone):

    start=time.perf_counter()

    results=await asyncio.gather(
        fetch_crm(phone),
        fetch_billing(phone),
        fetch_tickets(phone)
    )

    elapsed=(time.perf_counter()-start)*1000

    print("Parallel fetch time:",elapsed)

    return results
