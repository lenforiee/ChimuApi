import chimu_api as chimu
import asyncio

async def main():

    api = chimu.AsyncChimuAPI()

    sets = await api.get_set(1)

    for mapa in sets.ChildrenBeatmaps:

        print(f"{mapa.BeatmapId} [{mapa.DiffName}]")
    
    print(sets.Creator)

async def download():

    api = chimu.AsyncChimuAPI()

    file_bytes = await api.download_file(1)

    with open("map.osz", "wb") as filea:
        filea.write(file_bytes)

asyncio.run(main())
asyncio.run(download())