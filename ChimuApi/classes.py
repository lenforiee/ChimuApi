from dataclasses import dataclass
from typing import Union

@dataclass
class Beatmap:
    """Dataclass for beatmap data"""
    
    BeatmapId: int
    ParentSetId: int
    DiffName: str
    FileMD5: str
    Mode: int
    BPM: float # float just in case
    AR: float
    OD: float
    CS: float
    HP: float
    TotalLength: int
    HitLength: int
    Playcount: int
    Passcount: int
    MaxCombo: int
    DifficultyRating: float
    OsuFile: str
    DownloadPath: str

@dataclass
class BeatmapSet:
    """Dataclass for beatmap set data"""

    SetId: int
    ChildrenBeatmaps: Union[Beatmap, list]
    RankedStatus: int
    ApprovedDate: str
    LastUpdate: str
    LastChecked: str
    Artist: str
    Title: str
    Creator: str
    Source: str
    Tags: str
    HasVideo: bool
    Genre: int
    Language: str
    Favourites: int
    Disabled: bool