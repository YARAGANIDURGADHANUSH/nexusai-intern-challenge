import asyncio
import random
import time
from dataclasses import dataclass


@dataclass
class CustomerContext:
    crm: dict
    billing: dict
    tickets: dict
    data_complete: bool
    fetch_time_ms: float


async def fetch_crm(phone):
    await asyncio.sleep(random.uniform(0.2, 0.4))
    return {"vip": True}


async def fetch_billing(phone):

    await asyncio.sleep(random.uniform(0.15, 0.35))

    if random.random() < 0.1:
        raise TimeoutError("Billing system timeout")

    return {"status": "paid"}


async def fetch_tickets(phone):
    await asyncio.sleep(random.uniform(0.1, 0.3))
    return {"complaints": ["internet", "billing"]}


async def fetch_parallel(phone):

    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_crm(phone),
        fetch_billing(phone),
        fetch_tickets(phone),
        return_exceptions=True
    )

    crm, billing, tickets = results

    data_complete = True

    if isinstance(billing, Exception):
        billing = None
        data_complete = False

    elapsed = (time.perf_counter() - start) * 1000

    return CustomerContext(
        crm,
        billing,
        tickets,
        data_complete,
        elapsed
    )