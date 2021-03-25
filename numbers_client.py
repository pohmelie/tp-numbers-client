from typing import Optional, Union
from enum import Enum

import httpx

__all__ = ("get_number", "NumberType", "NumberNotFoundType")
__version__ = "0.1.0"
version = tuple(map(int, __version__.split(".")))


class NumberType(str, Enum):
    trivia = "trivia"
    math = "math"
    date = "date"
    year = "year"


class NumberNotFoundType(str, Enum):
    default = "default"
    floor = "floor"
    ceil = "ceil"


URL_TEMPLATE = "http://numbersapi.com/{number}/{type}"


def _set_if_not_none(dictionary, name, value):
    if value is not None:
        dictionary[name] = value


def get_number(number: Union[int, str], *,
               type: NumberType = NumberType.trivia,
               fragment: bool = False,
               notfound: Optional[NumberNotFoundType] = None,
               default: Optional[str] = None,
               min: Optional[int] = None,
               max: Optional[int] = None) -> dict:
    url = URL_TEMPLATE.format(number=number, type=type)
    params = {
        "json": True,
    }
    if fragment:
        params["fragment"] = True
    _set_if_not_none(params, "notfound", notfound)
    _set_if_not_none(params, "default", default)
    _set_if_not_none(params, "min", min)
    _set_if_not_none(params, "max", max)

    response = httpx.get(url, params=params)
    response.raise_for_status()
    return response.json()
