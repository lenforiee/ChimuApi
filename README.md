# ChimuAPI Python Wrapper
API Wrapper around Chimu.moe API for both synchronous and asynchronous purposes.

## What is it for?
I made this wrapper for Python devs so they can easly access Chimu.moe API both async and sync.

Allowing more people to use it!

## Synchronous Example

```py
import ChimuApi as chimu

def main():

    api = chimu.ChimuAPI()

    sets = api.get_set(1)

    for mapa in sets.ChildrenBeatmaps:

        print(f"{mapa.title} [{mapa.DiffName}]")
    
    print(sets.Creator)

main()
```

## Asynchronous Example

```py
import ChimuApi as chimu
import asyncio

async def main():

    api = chimu.AsyncChimuAPI()

    sets = await api.get_set(1)

    for mapa in sets.ChildrenBeatmaps:

        print(f"{mapa.title} [{mapa.DiffName}]")
    
    print(sets.Creator)

asyncio.run(main())
```

## Contribution
If you feel like you want to help/fix/change something in this package,
just create Issue or Pull Request on GitHub and I'll review it.