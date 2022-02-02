from typing import Tuple, Optional


def something_has_changed(
    old_delta: str,
    delta: str,
    old_longitude: str,
    longitude: str,
    old_latitude: str,
    latitude: str
) -> Optional[Tuple[str, str, str]]:
    new_delta = old_delta
    new_longitude = old_longitude
    new_latitude = old_latitude

    if old_delta != delta:
        new_delta = delta

    elif old_longitude != longitude:
        new_longitude = longitude

    elif old_latitude != latitude:
        new_latitude = latitude

    else:
        return None

    return new_delta, new_longitude, new_latitude


def something_has_changed_for_task_4(
    old_delta: str,
    delta: str,
    old_longitude: str,
    longitude: str,
    old_latitude: str,
    latitude: str,
    old_type_map: str,
    type_map: str
) -> Optional[Tuple[str, str, str, str]]:
    new_delta = old_delta
    new_longitude = old_longitude
    new_latitude = old_latitude
    new_type_map = old_type_map

    if old_delta != delta:
        new_delta = delta

    elif old_longitude != longitude:
        new_longitude = longitude

    elif old_latitude != latitude:
        new_latitude = latitude

    elif old_type_map != type_map:
        new_type_map = type_map

    else:
        return None

    return new_delta, new_longitude, new_latitude, new_type_map
