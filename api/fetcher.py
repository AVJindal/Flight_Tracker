import requests
from api.config import settings

ROOT_URL = settings.ROOT_URL


def states_accessor():
    # go through the doc api examples
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())


def tracks_accessor():
    url = f""
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())
