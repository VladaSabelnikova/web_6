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

    check_1 = something_has_changed(
        old_delta,
        delta,
        old_longitude,
        longitude,
        old_latitude,
        latitude,
    )

    if old_type_map != type_map:
        new_type_map = type_map

    elif check_1:
        new_delta, new_longitude, new_latitude = check_1

    else:
        return None

    return new_delta, new_longitude, new_latitude, new_type_map


def something_has_changed_for_task_7(
    old_delta: str,
    delta: str,
    old_longitude: str,
    longitude: str,
    old_latitude: str,
    latitude: str,
    old_type_map: str,
    type_map: str,
    old_pt_type: Optional[str],
    pt_type: Optional[str],
) -> Optional[Tuple[str, str, str, str, str]]:
    new_delta = old_delta
    new_longitude = old_longitude
    new_latitude = old_latitude
    new_type_map = old_type_map
    new_pt_type = old_pt_type

    check_1 = something_has_changed_for_task_4(
        old_delta,
        delta,
        old_longitude,
        longitude,
        old_latitude,
        latitude,
        old_type_map,
        type_map,
    )

    if old_pt_type != pt_type:
        new_pt_type = pt_type

    elif check_1:
        new_delta, new_longitude, new_latitude, new_type_map = check_1

    else:
        return None

    return new_delta, new_longitude, new_latitude, new_type_map, new_pt_type
