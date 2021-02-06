from chimu_api import ChimuAPI
import asyncio

def main():

    api = ChimuAPI()

    sety = api.search({ "query": "peppy" })

    print(sety)

main()
