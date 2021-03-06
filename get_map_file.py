import pathlib
from typing import Optional

from get_response import get_response_from_static_api
from show_img import show_img


def get_map_file(
    longitude: str = '141.318090',
    latitude: str = '-28.514865',
    delta: str = '50.992457',
    type_map: str = 'map',
    pt_type: Optional[str] = None
) -> pathlib.Path:
    response_static = get_response_from_static_api(
        longitude,
        latitude,
        delta,
        type_map,
        pt_type
    )
    map_file = show_img(response_static)
    return map_file
