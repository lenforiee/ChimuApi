import aiohttp
import requests
import orjson
from classes import Beatmap, BeatmapSet

class ChimuAPI:
    """Synchronous ChimuAPI class for making requests"""

    def get_map(self, map_id: int) -> Beatmap:
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

    def get_set(self, set_id: int) -> BeatmapSet:
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

class AsyncChimuAPI:
    """Asynchronous ChimuAPI class for making requests"""

    async def get_map(self, map_id: int):
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

    async def get_set(self, set_id: int) -> BeatmapSet:
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