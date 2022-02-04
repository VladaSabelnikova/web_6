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


def get_postal_code_from_geocoder_response(
    response: requests.Response
) -> str:
    postal_code = ''
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]

    all_data = toponym['metaDataProperty']['GeocoderMetaData'][
                'Address']

    if 'postal_code' in all_data.keys():
        postal_code = all_data['postal_code']

    return postal_code


def get_full_address_from_search_response_geo(
    response: requests.Response
) -> str:
    json_response = response.json()
    location = json_response["features"][0]
    org_address = location["properties"]["GeocoderMetaData"]["text"]

    return org_address


def get_full_address_from_search_response_biz(
    response: requests.Response
) -> str:
    json_response = response.json()
    organization = json_response["features"][0]
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    return org_address
