import aiohttp
import requests
import orjson
from classes import Beatmap, BeatmapSet

class ChimuAPI:
    """Synchronous ChimuAPI class for making requests"""

    def __init__(self):
        pass

    @staticmethod
    def get_map(map_id: int) -> Beatmap:
        """Gets a beatmap from chimu's API
        Params:
            - map_id: int = map id to be fetched.
        Returns:
            Beatmap class full of beatmap data.
        """

        # We create request first.
        request = requests.get(f"https://api.chimu.moe/v1/map/{map_id}").json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        # Code is 0 means its all good.
        beatmap = Beatmap(
            BeatmapId= request['data']['BeatmapId'],
            ParentSetId= request['data']['ParentSetId'],
            DiffName= request['data']['DiffName'],
            FileMD5= request['data']['FileMD5'],
            Mode= request['data']['Mode'],
            BPM= request['data']['BPM'],
            AR= request['data']['AR'],
            OD= request['data']['OD'],
            CS= request['data']['CS'],
            HP= request['data']['HP'],
            TotalLength= request['data']['TotalLength'],
            HitLength= request['data']['HitLength'],
            Playcount= request['data']['Playcount'],
            Passcount= request['data']['Passcount'],
            MaxCombo= request['data']['MaxCombo'],
            DifficultyRating= request['data']['DifficultyRating'],
            OsuFile= request['data']['OsuFile'],
            DownloadPath= request['data']['DownloadPath']
        )

        # Return it.
        return beatmap

    @staticmethod
    def get_set(set_id: int) -> BeatmapSet:
        """Gets a beatmap set from chimu's API
        Params:
            - set_id: int = set id to be fetched.
        Returns:
            BeatmapSet class full of beatmap set data.
        """

        # We create request first.
        request = requests.get(f"https://api.chimu.moe/v1/set/{set_id}").json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        # This is not gonna be the best code.
        beatmaps = []
        for mapa in request['data']['ChildrenBeatmaps']:
            beatmaps.append(Beatmap(
                BeatmapId= mapa['BeatmapId'],
                ParentSetId= mapa['ParentSetId'],
                DiffName= mapa['DiffName'],
                FileMD5= mapa['FileMD5'],
                Mode= mapa['Mode'],
                BPM= mapa['BPM'],
                AR= mapa['AR'],
                OD= mapa['OD'],
                CS= mapa['CS'],
                HP= mapa['HP'],
                TotalLength= mapa['TotalLength'],
                HitLength= mapa['HitLength'],
                Playcount= mapa['Playcount'],
                Passcount= mapa['Passcount'],
                MaxCombo= mapa['MaxCombo'],
                DifficultyRating= mapa['DifficultyRating'],
                OsuFile= mapa['OsuFile'],
                DownloadPath= mapa['DownloadPath']
            ))

        beatmap_set = BeatmapSet(
            SetId= request['data']['SetId'],
            ChildrenBeatmaps= beatmaps,
            RankedStatus= request['data']['RankedStatus'],
            ApprovedDate= request['data']['ApprovedDate'],
            LastUpdate= request['data']['LastUpdate'],
            LastChecked= request['data']['LastChecked'],
            Artist= request['data']['Artist'],
            Title= request['data']['Title'],
            Creator= request['data']['Creator'],
            Source= request['data']['Source'],
            Tags= request['data']['Tags'],
            HasVideo= request['data']['HasVideo'],
            Genre= request['data']['Genre'],
            Language= request['data']['Language'],
            Favourites= request['data']['Favourites'],
            Disabled= request['data']['Disabled']
        )

        # Return it.
        return beatmap_set

    @staticmethod
    def search(search_params: dict = {}):
        """Search for a Beatmap.
        Params:
            - search_params: dict = Dict of params for search.
        Returns:
            Returns json callback data from request.
        """

        # We create request first.
        request = requests.get("https://api.chimu.moe/v1/search", params= search_params).json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        return request['data']

    @staticmethod
    def download_file(set_id: int, key: str, state: str = "hcaptcha"):
        """Download a Beatmap.
        Params:
            - set_id: int = Set to be downloaded.
            - key: str = API key to download without captcha.
            - state: str = State of verification either of hcaptcha or success.
        Returns:
            Returns file bytes for user to save it.
        """

        # We create request first.
        request = requests.get(f"https://api.chimu.moe/v1/download/{set_id}", params= {
            "k": key,
            "s": state
        })

        if request.status_code != 200:
            raise Exception(f"Map file of ID {set_id} couldnt be fetched!")

        return request.content

class AsyncChimuAPI:
    """Asynchronous ChimuAPI class for making requests"""

    def __init__(self):
        pass

    @staticmethod
    async def get_map(map_id: int):
        """Gets a beatmap from chimu's API
        Params:
            - map_id: int = map ID to be fetched.
        Returns:
            Beatmap class full of beatmap data.
        """

        # Create async session & make request.
        async with aiohttp.ClientSession(json_serialize= orjson.dumps) as session:
            async with session.get(f"https://api.chimu.moe/v1/map/{map_id}") as resp:
                request = await resp.json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        # Code is 0 means its all good.
        beatmap = Beatmap(
            BeatmapId= request['data']['BeatmapId'],
            ParentSetId= request['data']['ParentSetId'],
            DiffName= request['data']['DiffName'],
            FileMD5= request['data']['FileMD5'],
            Mode= request['data']['Mode'],
            BPM= request['data']['BPM'],
            AR= request['data']['AR'],
            OD= request['data']['OD'],
            CS= request['data']['CS'],
            HP= request['data']['HP'],
            TotalLength= request['data']['TotalLength'],
            HitLength= request['data']['HitLength'],
            Playcount= request['data']['Playcount'],
            Passcount= request['data']['Passcount'],
            MaxCombo= request['data']['MaxCombo'],
            DifficultyRating= request['data']['DifficultyRating'],
            OsuFile= request['data']['OsuFile'],
            DownloadPath= request['data']['DownloadPath']
        )

        # return it
        return beatmap

    @staticmethod
    async def get_set(set_id: int) -> BeatmapSet:
        """Gets a beatmap set from chimu's API
        Params:
            - set_id: int = set id to be fetched.
        Returns:
            BeatmapSet class full of beatmap set data.
        """

        # Create async session & make request.
        async with aiohttp.ClientSession(json_serialize= orjson.dumps) as session:
            async with session.get(f"https://api.chimu.moe/v1/set/{set_id}") as resp:
                request = await resp.json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        # This is not gonna be the best code.
        beatmaps = []
        for mapa in request['data']['ChildrenBeatmaps']:
            beatmaps.append(Beatmap(
                BeatmapId= mapa['BeatmapId'],
                ParentSetId= mapa['ParentSetId'],
                DiffName= mapa['DiffName'],
                FileMD5= mapa['FileMD5'],
                Mode= mapa['Mode'],
                BPM= mapa['BPM'],
                AR= mapa['AR'],
                OD= mapa['OD'],
                CS= mapa['CS'],
                HP= mapa['HP'],
                TotalLength= mapa['TotalLength'],
                HitLength= mapa['HitLength'],
                Playcount= mapa['Playcount'],
                Passcount= mapa['Passcount'],
                MaxCombo= mapa['MaxCombo'],
                DifficultyRating= mapa['DifficultyRating'],
                OsuFile= mapa['OsuFile'],
                DownloadPath= mapa['DownloadPath']
            ))

        beatmap_set = BeatmapSet(
            SetId= request['data']['SetId'],
            ChildrenBeatmaps= beatmaps,
            RankedStatus= request['data']['RankedStatus'],
            ApprovedDate= request['data']['ApprovedDate'],
            LastUpdate= request['data']['LastUpdate'],
            LastChecked= request['data']['LastChecked'],
            Artist= request['data']['Artist'],
            Title= request['data']['Title'],
            Creator= request['data']['Creator'],
            Source= request['data']['Source'],
            Tags= request['data']['Tags'],
            HasVideo= request['data']['HasVideo'],
            Genre= request['data']['Genre'],
            Language= request['data']['Language'],
            Favourites= request['data']['Favourites'],
            Disabled= request['data']['Disabled']
        )

        # Return it.
        return beatmap_set

    @staticmethod
    async def search(search_params: dict = {}):
        """Search for a Beatmap.
        Params:
            - search_params: dict = Dict of params for search.
        Returns:
            Returns json callback data from request.
        """

        # Create async session & make request.
        async with aiohttp.ClientSession(json_serialize= orjson.dumps) as session:
            async with session.get("https://api.chimu.moe/v1/search", params= search_params) as resp:
                request = await resp.json()

        if request['code']:
            raise Exception(f"The error was debugged: {request['message']}")

        return request['data']

    @staticmethod
    async def download_file(set_id: int, key: str, state: str = "hcaptcha"):
        """Download a Beatmap.
        Params:
            - set_id: int = Set to be downloaded.
            - key: str = API key to download without captcha.
            - state: str = State of verification either of hcaptcha or success.
        Returns:
            Returns file bytes for user to save it.
        """

        # Create async session & make request.
        async with aiohttp.ClientSession(json_serialize= orjson.dumps) as session:
            async with session.get(f"https://api.chimu.moe/v1/download/{set_id}", params= {
                "k": key,
                "s": state
            }) as resp:

                if resp.status != 200:
                    raise Exception(f"Map file of ID {set_id} couldnt be fetched!")

                request = await resp.read()

        return request
