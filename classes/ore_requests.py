import json
import dataclasses as dataclasses_std
from dataclasses import dataclass
from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass
import datetime
from pydantic.json import pydantic_encoder


import dataclasses
@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: List[int] = dataclasses.field(default_factory=lambda: [0])
    age: Optional[int] = dataclasses.field(
        default=None,
        metadata=dict(title='The age of the user', description='do not lie!')
    )
    height: Optional[List[int]] = Field(None, title='The height in cm', ge=50, le=300)


@dataclass
class SpotPrice:
    Symbol: str
    Value: float


@dataclass
class VolSurface:
    Symbol: str
    Expiry: List[datetime.date]
    Atm: List[float]


@dataclass
class MarketData:
    SpotPrice: Optional[List[SpotPrice]]
    VolSurface: Optional[List[VolSurface]]


@dataclass
class StaticData:
    @dataclass
    class Calendar:
        Symbol: str
        Name: str
        Holiday: List[datetime.date]

    @dataclass
    class CoEntity:
        Symbol: str
        Name: str
        Exchange: Optional[str] = None

    Calendar: Calendar
    CoEntity: List[CoEntity]


@dataclass
class ORE_Request:
    MarketData: MarketData
    StaticData: Optional[StaticData] = None
