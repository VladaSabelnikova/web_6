from typing import Optional

import requests
from private_data.secrets import GEOCODER_API_KEY


def get_response_from_static_api(
    lon: str = '141.318090',
    lat: str = '-28.514865',
    delta: str = '50.992457',
    type_map: str = 'map',
    pt_type: Optional[str] = None
) -> requests.Response:
    static_api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": type_map
    }

    if pt_type:
        params["pt"] = pt_type
    response = requests.get(static_api_server, params=params)

    return response


def get_response_from_geocoder_api(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    params = {
        "apikey": GEOCODER_API_KEY,  # у вас будет свой
        "geocode": toponym_to_find,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=params)

    return response
