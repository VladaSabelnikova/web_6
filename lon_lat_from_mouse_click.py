from typing import Tuple


def get_lon_lat_from_mouse_click(
    pos: Tuple[int, int],
    lon: float,
    lat: float,
    delta: float
) -> Tuple[str, str]:

    degree_per_px = delta / 450

    lon_shift = (pos[0] - 300) * degree_per_px * 1.9
    lat_shift = (pos[1] - 225) * degree_per_px

    new_lon = lon + lon_shift
    new_lat = lat - lat_shift

    print(str(new_lon), str(new_lat))
    return str(new_lon), str(new_lat)
