from typing import Tuple

import requests


def get_lon_lat_from_geocoder_response(
    response: requests.Response
) -> Tuple[str, str]:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coordinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")

    return toponym_longitude, toponym_lattitude


def get_full_address_from_geocoder_response(
    response: requests.Response
) -> str:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]

    full_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]

    return full_address
