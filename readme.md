# Numbers-client

Python client for json subset of [numbers](http://numbersapi.com/) api.

# Requirements
- python 3.8+

# Usage
``` python
from numbers_client import get_number, NumberType, NumberNotFoundType

print(get_number(1))
```

# API

## `get_number`
``` python
def get_number(number: Union[int, str], *,
               type: NumberType = NumberType.trivia,
               fragment: bool = False,
               notfound: Optional[NumberNotFoundType] = None,
               default: Optional[str] = None,
               min: Optional[int] = None,
               max: Optional[int] = None) -> dict:
```
Get the number from [numbers](http://numbersapi.com/)

## `NumberType`
``` python
class NumberType(str, Enum):
    trivia = "trivia"
    math = "math"
    date = "date"
    year = "year"
```

## `NumberNotFoundType`
``` python
class NumberNotFoundType(str, Enum):
    default = "default"
    floor = "floor"
    ceil = "ceil"
```
