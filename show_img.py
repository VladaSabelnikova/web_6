import pathlib

import requests


def show_img(response: requests.Response) -> pathlib.Path:

    if not response:
        raise requests.ConnectionError

    map_file = pathlib.Path('map.png')
    map_file.write_bytes(response.content)

    return map_file
