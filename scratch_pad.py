from classes.ore_requests import *
import json
from pydantic.json import pydantic_encoder

spotPrice_example = SpotPrice("BRN", "100")
volSruface_example = VolSurface("BRN",
                                ["2022-01-01", "2023-01-01"],
                                [0.6, 0.5]
                                )


request_example = ORE_Request(
    MarketData=MarketData([spotPrice_example], [volSruface_example]),
    StaticData=None
)

request_example2 = ORE_Request(
    MarketData=MarketData(VolSurface=[volSruface_example]),
    StaticData=None
)
request_json = json.dumps(request_example, indent=2, default=pydantic_encoder)
print(request_json)

request_recreated = ORE_Request(**json.loads(request_json))

assert True