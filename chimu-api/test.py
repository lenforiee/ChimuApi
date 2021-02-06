from chimu_api import AsyncChimuAPI
import asyncio

async def main():

    api = AsyncChimuAPI()

    sety = await api.get_set(1)

    print(sety)

asyncio.run(main())
