from typing import Tuple

import pygame_gui

from get_response import get_response_from_geocoder_api
from gets import get_lon_lat_from_geocoder_response, \
    get_full_address_from_geocoder_response, \
    get_postal_code_from_geocoder_response


def create_address_for_label(
    toponym_to_find: str,
    post_code_menu: pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu
) -> Tuple[str, str, str, str]:
    response = get_response_from_geocoder_api(toponym_to_find)
    lon, lat = get_lon_lat_from_geocoder_response(response)
    address = get_full_address_from_geocoder_response(response)

    longitude = lon
    latitude = lat
    pt_type = f'{lon},{lat},pmpnl'

    if post_code_menu.selected_option == 'вкл. postcode':
        p_c = get_postal_code_from_geocoder_response(response)
        address += f' {p_c}'

    return longitude, latitude, pt_type, address
