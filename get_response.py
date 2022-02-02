import requests


def get_response_from_static_api(
    lon: str = '141.318090',
    lat: str = '-28.514865',
    delta: str = '50.992457'
) -> requests.Response:
    api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)

    return response
